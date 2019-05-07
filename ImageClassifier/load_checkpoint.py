import torch
from torchvision import datasets, transforms, models 
from torch import nn

def load_checkpoint(dir_name):
    checkpoint= torch.load(dir_name)
    #checkpoint= torch.load(chkpt_name, map_location=lambda storage, loc: storage)
    #model.features = checkpoint['features']
    print('Loading pretrained model to serve as a shell.')
    model = models.vgg19(pretrained=True)
    print('Loading in features from trained model.')
    model.features = checkpoint['features']
    print('Loding in classifier and weights from trained model.')
    model.classifier = nn.Sequential(nn.Linear(checkpoint['input_size'], checkpoint['hidden_layers'][0]),
                           nn.ReLU(),
                           nn.Dropout(0.2),
                           nn.Linear(checkpoint['hidden_layers'][0], checkpoint['hidden_layers'][1]),
                           nn.ReLU(),
                           nn.Linear(checkpoint['hidden_layers'][1], checkpoint['output_size']),
                           nn.LogSoftmax(dim=1))
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_indices']
    #model.features = checkpoint['features']
    
    return model