# FunData

A repository to store R scripts and Python Notebooks for data science projects I have worked on outside of my dissertation research.

## Contents:
1. **Image Classifier** : A command line application that classifies images.
> **train.py**  within _Image Classifier_ trains a PyTorch VGG19 (default) neural net on a dataset of flower images. **predict.py** predicts the class of a new image using the saved trained model. The application can run on either CPU or GPU.

>Basic usage: `python train.py flowers`- Prints out training loss, validation loss, and validation accuracy as the network trains.

>Options:  
 1.Set directory to save checkpoints: `python train.py data_dir --save_dir save_directory`    
 2.Choose architecture: `python train.py data_dir --arch "vgg13"`    
 3.Set hyperparameters: `python train.py data_dir --learning_rate 0.01 --hidden_units 512 --epochs 20`    
 4.Use GPU for training: `python train.py data_dir --gpu`  

>Predict flower name from an image with **predict.py** along with the probability of that name. Pass in a single image /path/to/image and return the flower name and class probability.

>Basic usage: `python predict.py /path/to/image`   - default checkpoint is called

>Options:  
1.Return top KK most likely classes: `python predict.py input --top_k 3`  
2.Use a mapping of categories to real names: `python predict.py input  --category_names cat_to_name.json`  
3.Use GPU for inference:  `python predict.py input checkpoint --gpu`  



2. **Idenfify Customer Segments**: A project to identify customer segments for a mail order company in Germany.
> **Identify_Customer_Segments.ipynb** is a project where I used unsupervised machine learning techniques to identify customer segments for a mail-order company in Germany. I performed extensive data exploration, cleaning, feature engineering and re-encoding before I applied Principal Components Analysis (PCA) and Kmeans clustering. The data that I used for this project was provided by Udacity partners at Bertelsmann Arvato Analytics. Because they are proprietary, they are not included here.

3. **FordGoBike**: A project to make insights about rider usage for the Ford GoBike bike share in California.
>**FordGoBikeData_AnalysisVisualization.ipynb** and **FordGoBikeData_VisualizationPresentaton** is an exploration of the Ford GoBike data collected in San Francisco in 2018. This .ipynb notebook will include any necessary wrangling and visualizations to gain insight about trends in rider usage. The slide deck will communicate the main findings of the exploration/analysis using data visualization with Matplotlib and Seaborn.

4. **WeRateDogsTwitter**: An analysis of the WeRateDogs Twitter feed.
>**wrangle_act.ipynb** (in the _WeRateDogs_Twitter_ folder, with raw data) was an assignment where I was tasked to address quality and tidyness issues associated with the twitter archive from WeRateDogs twitter feed. I also performed an exploratory analysis of the tweets and accompanying dataset that included a prediction for the dog breed referenced in each tweet.

5. An analysis of A/B test results using bootstrap simulation and regression analysis.
>**AnalyzeABtestResults.ipynb** (in the _AnalyzeABTestResults_ folder, with raw data) was an assignment where I was tasked to analyze some A/B testing data using bootstrap simulation hypothesis testing and regression methods. I used numpy, pandas, statsmodels.api, and patsy.

6. An exploration into GapMinder data using pandas and matplotlib.
>**GDP_ChildMortality_FemaleEducation_GapMinder.ipynb** (in the _InvestigateGapMinder_ folder, with raw data) is a mini data exploration project using Numpy, Pandas, and Matplotlib.   
