library(AppliedPredictiveModeling)
library(tidyverse)

data("segmentationOriginal")

segdata <- segmentationOriginal %>% filter(Case == "Train")

cellID <- segdata$Cell
class <- segdata$Class
case <- segdata$Case

segdata <- segdata %>% select(-c(Cell, Class, Case))


#original data contains status columns that are binary versions of the predicts. remove these
# They contain the word Status

statusColNums <- grep("Status", names(segdata))

segdata <- segdata %>% select(-c(statusColNums))

# Transformations ####

#some features in this dataset have significant skew
# use a package to calculate skewness of each features
library(e1071)

#look at skew for one predictor
skewness(segdata$AngleCh1)

#predictors are numeric columns to can use skewness in apply function

skewValues <- apply(segdata, 2, skewness)
head(skewValues)

#use hist to visualize distribution of each - non skewed - stat will be close to 0
# quite a bit of skew so we need to transform the data

# use Box-Cox transformation - caret package will determine and also apply the transformation

# to det