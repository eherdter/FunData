from torchvision import datasets, transforms, models
import torch
from torch import nn
from torch import optim
import json


def load_data(data_dir):
    
    ''' Defines data directories, defines and applies transforms, loads train and validation datasets with ImageFolder, uses DataLoader to return training and validaton sets. Also returns categories and their names.
        
    '''
    #define data directories
    data_dir = data_dir
    train_dir = data_dir + '/train'
    valid_dir = data_dir + '/valid'
    test_dir = data_dir + '/test'
    
    #define data transforms
    train_transforms = transforms.Compose([transforms.RandomRotation(30),
                                        transforms.RandomResizedCrop(256), 
                                      transforms.CenterCrop(224), 
                                      transforms.ToTensor(), 
                                      transforms.Normalize([0.485, 0.456, 0.406], 
                                                          [0.229, 0.224, 0.225])])

#for testing/validation we only want touse images that arent altered other than normalizing so just resize, crop, and scale to mean color channel                                       
    test_transforms = transforms.Compose([transforms.Resize(256), 
                                      transforms.CenterCrop(224), 
                                      transforms.ToTensor(), 
                                      transforms.Normalize([0.485, 0.456, 0.406], 
                                                          [0.229, 0.224, 0.225])])

    valid_transforms = transforms.Compose([transforms.Resize(256), 
                                      transforms.CenterCrop(224), 
                                      transforms.ToTensor(), 
                                      transforms.Normalize([0.485, 0.456, 0.406], 
                                                          [0.229, 0.224, 0.225])])
                                    
                                      
# TODO: Load the datasets with ImageFolder
    train_data = datasets.ImageFolder(train_dir, transform=train_transforms)
    valid_data  = datasets.ImageFolder(valid_dir, transform=valid_transforms)
    #test_data = datasets.ImageFolder(test_dir, transform=test_transforms)
                                   

# TODO: Using the image datasets and the trainforms, define the dataloaders
    trainloader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
    validloader = torch.utils.data.DataLoader(valid_data, batch_size=64, shuffle=True)
    #testloader = torch.utils.data.DataLoader(test_data, batch_size=64, shuffle=True)
    
   
    #define label mapping
    with open('cat_to_name.json', 'r') as f:
        cat_to_name = json.load(f)
        
    return train_data, trainloader, validloader, cat_to_name