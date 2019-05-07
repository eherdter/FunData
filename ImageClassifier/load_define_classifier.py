from torchvision import datasets, transforms, models
from torch import nn
from torch import optim

def load_define_class(learning_rate, arch, hidden_units):
    
    ''' Loads a pretrained model. Defines classifier. Applies classifier to pretrained model.
    Defines loss criterion and optimizer. 
        
    '''
    if arch == 'vgg19':
        model = models.vgg19(pretrained=True)
    if arch == 'vgg13':
        model = models.vgg13(pretrained=True)
    #First, freeze the parameters of the feature so we dont update them accidentally
    for param in model.parameters():
        param.requires_grad=False
    
    #replace the pre loaded model classifier with a classifier for this application
    #input number must be 25088 for VGG19,
    #assign two hidden layers
    #use the Relu activation function
    #then dropout before going through another linear combination
    classifier = nn.Sequential(nn.Linear(model.classifier[0].in_features, hidden_units),
                           nn.ReLU(),
                           nn.Dropout(0.2),
                           nn.Linear(hidden_units, 256),
                           nn.ReLU(),
                           nn.Linear(256, 102),
                           nn.LogSoftmax(dim=1))
    
    
#assign classifier to the model and assign loss criterion and assign optimizer  
    model.classifier = classifier
    criterion = nn.NLLLoss()
    optimizer = optim.Adam(model.classifier.parameters(), learning_rate) 
    
    return model, criterion, optimizer, hidden_units

    
