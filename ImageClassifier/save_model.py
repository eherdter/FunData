import torch

def save_model(model, train_data, optimizer, epochs, dir_name, hidden_units):
    #save mapping of classes to the indices to the model
    model.class_to_idx = train_data.class_to_idx
    
    #create check point
    checkpoint ={'features': model.features,
        'input_size': model.classifier[0].in_features,
            'output_size' : 102,
            'hidden_layers': [hidden_units, 256],
             'epochs': epochs,
            'optimizer': optimizer.state_dict,
             'class_indices': model.class_to_idx,
            'state_dict': model.state_dict()
            }

    #torch.save(checkpoint, 'checkpoint_from_fxn.pth') #'checkpoint.pth'
    torch.save(checkpoint, dir_name) 