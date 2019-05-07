import argparse
import load_checkpoint as lcp
import process_image as pi
import torch
from PIL import Image
import numpy as np
import json
 


def predict(image_path, dir_name='checkpoint.pth', topk=1, category_names=False, gpu=True):
    
    ''' Loads a previously trained model from filepath, processes an image from image_path
        and makes prediction for that image. 
        Returns topk classes.
        
    '''
    #load previously trained model
    model = lcp.load_checkpoint(dir_name) #'checkpoint_from_fxn.pth'
    
    #process the image 
    p_im = pi.process_image(image_path)
    print('Image has been processed.')
    #define a device 
    
    if gpu: #try to find a gpu if available
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        device= torch.device("cpu")
    #https://discuss.pytorch.org/t/input-type-torch-cuda-doubletensor-and-weight-type-torch-cuda-           floattensor-should-be-the-same/22704
    
    #move the image to device
    img = p_im.to(device=device, dtype=torch.float)
    
    #move the model to device
    model=model.to(device)
    
    #turn to model eval stage
    model.eval()
    with torch.no_grad():
    
        #https://discuss.pytorch.org/t/expected-stride-to-be-a-single-integer-value-or-a-list/17612/3
        img.unsqueeze_(0) #add a batch number to a single picture so that shape is now [batch number,b,c,d]
        
        #make prediction
        print('Image has been passed to model. Wait for prediction.')
        log_ps = model(img)
        #get probabalities
        ps= torch.exp(log_ps)
        
        #get the topk predictions
        top_p, top_index = ps.topk(topk, dim=1)
        
        #convert tho index and ps to array
        index = top_index.data.cpu().numpy()[0]
        probs = top_p.data.cpu().numpy()[0]
        print(f"Probabilities of each prediction is/are {probs}.")
        
        #convert the index to the class
        mydict = model.class_to_idx
        
        keys = []
        for index in index:
            for key, value in mydict.items():
                if value == index:
                    keys.append(key)
        print(f"Index of flower species prediction is/are {keys}.")
        
        #if a user supplies a category name
        if category_names:
            with open(category_names, 'r') as f:
                cat_to_name = json.load(f)             
       # 
            names=[]
            for key in keys:
                for number, flower in cat_to_name.items():
                    if number == key:
                        names.append(flower)
            print(f"Names of flower species prediction is/are {names}.")

    

def main():
    # Initialize the parser
    parser = argparse.ArgumentParser()
    # Add the positional parameter
    parser.add_argument('path_to_image')
    parser.add_argument('--dir_name', default='checkpoint.pth')
    parser.add_argument('--topk', type=int, default=1)
    parser.add_argument('--category_names', default=False)
    parser.add_argument('--gpu', default=True)

    # Parse the arguments
    args = parser.parse_args()
    print(args)
    
    #predict using the data_directory 
    print(predict(args.path_to_image, args.dir_name, args.topk, args.category_names, args.gpu))
   
if __name__ == '__main__':
    main()


