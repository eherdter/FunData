from PIL import Image
import numpy as np
import torch

def process_image(image_path):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an PyTorch tensor
        
    '''
    with Image.open(image_path) as img:

        #get initial image size
 #get initial image size
        current_width, current_height = img.size
    
        #resize the images where shortest side is 256, maintaining aspect ratio
        if current_width < current_height:
            new_height = int(current_height *256 / current_width)
            image = img.resize((256, new_height))
            
        else:
            new_width = int(current_width * 256/ current_height)
            image = img.resize((new_width, 256))
                            
     
        #crop
        precrop_width, precrop_height = img.size
        left = (precrop_width - 244)/2
        top = (precrop_height - 224)/2
        right = (precrop_width + 224)/2
        bottom = (precrop_height + 224)/2
   
        img = img.crop((left, top, right, bottom))
    
    #normalize
        img = np.array(img)
        
    #convert values to floats between 0-1
        img = img/(255.0)
    
    #normalize
        mean = np.array([0.485, 0.456, 0.406])
        std = np.array([0.229, 0.224, 0.225])
        img =  (img - mean)/std

    #transpose
     #reorder dimensions https://stackoverflow.com/questions/43829711/what-is-the-correct-way-to-change-image-channel-ordering-between-channels-first
        img = img.transpose((2,0, 1)) 
        
        #convert to pytorch tensor , make sure its a double tensor
        img = torch.from_numpy(img).double()
        img= img.type(torch.DoubleTensor)
        return img
