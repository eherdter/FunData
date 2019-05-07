import argparse
import load_data 
import load_define_classifier as ldc
import save_model
import torch
from torch import nn
from workspace_utils import active_session

 

def train(data_dir, dir_name='checkpoint.pth', epochs=5, learning_rate=0.001, gpu=True, arch='vgg19', hidden_units=1024):
    print(learning_rate)
    print(epochs)

    #load and transform data
    print('Loading training and validation data.')
    train_data, trainloader, validloader, cat_to_name = load_data.load_data(data_dir)
    #load pre trained model (vgg19), define classifier, loss criterion and optimizer
    #print('Loading pre-trained model vgg19.')
    model, criterion, optimizer, hidden_units = ldc.load_define_class(learning_rate, arch, hidden_units)
    print('Loaded pre-trained model.')
    #define device, if cuda is set as true try gpu else use cpu
    if gpu: #try to find a gpu if available
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        device= torch.device("cpu")    
    #move model to device 
    model.to(device);
    
    print('Preparing to train....')
    
    with active_session():
        epochs=epochs #determine how many passes
        steps=0 #keep track of the steps made
        running_loss = 0 #assign an acculumator for loss
        print_every=5 #determine at what frequency to print an average loss (if print_ever >1)
    
        print('Looping through epochs.')
#now, loop through the epochs
        for epoch in range(epochs):
    #MAKE TRAINING PASS
            for data, labels in trainloader: #for every batch of batch size in the trainloader data
                steps +=1 #start accumulating the steps 
        #move the data and the labels to the gpu device if its available
                data = data.to(device)
                labels = labels.to(device)
        
        #now write the training loop
        
                optimizer.zero_grad() #zero out the gradients to start out the loop (they accumulate from previous steps if we dont do this)
                logps = model.forward(data) #make a forward pass through the network aka model(data)
                loss = criterion(logps, labels) # use network output to calculate loss
                loss.backward() #make a backward pass (back propogation) to calculate gradients
                optimizer.step() #make a step with the optimizer to update the weights for each node in each layer
        
                running_loss += loss.item() #keep track of training loss here
        
    # DROP OUT OF TRAINING LOADER AND TEST ACCURACY ON VALIDATION SET
                if steps % print_every == 0: #to operate at an average
                    validation_loss = 0
                    accuracy =0
                    model.eval() #turn our model to evaluation (turns any dropout off)
        
                    with torch.no_grad(): #Turn off gradients for validation- we arent training here so we dont need to calculate gradients
                        for data, labels in validloader:
                
                            data = data.to(device) #transfer data and the labels to the gpu device if its available
                            labels = labels.to(device)
                            logps = model.forward(data) #get log probs of validation data
                            batch_loss = criterion(logps, labels) #get the loss of the specific batch
                
                            validation_loss += batch_loss.item() #accumulate the loss from each bach into the validation loss 
                
                        #calculate accuracy
                            ps = torch.exp(logps) #exponentiate the log probs to get the probabilities
                            top_p, top_class = ps.topk(1, dim=1) #get the top probability and the top class a predicition
                            equals = top_class == labels.view(*top_class.shape) #check for equality
                            accuracy +=torch.mean(equals.type(torch.FloatTensor)).item() # accumulatetheaccuracy
        
                #print stats
                    print(f"Epoch {epoch+1}/{epochs}.. "
                    f"TrainLoss: {running_loss/print_every:.3f}.. "
                     f"Validation loss: {validation_loss/len(validloader):.3f}.."
                     f"Validation Acc: {accuracy/len(validloader):.3f}")
        
                    running_loss = 0
                    model.train() #return model back to training mode     
    #save model
        print('Finished training. Saving checkpoint.')
        save_model.save_model(model, train_data, optimizer, epochs, dir_name, hidden_units) ###
        print('Checkpoint saved.')
          
def main():
    # Initialize the parser
    parser = argparse.ArgumentParser()
    # Add the positional parameter
    parser.add_argument('data_dir')
    parser.add_argument('--dir_name', default='checkpoint.pth', help='assign directory and model checkpoint name. Defualt is checkpoint.pth')
    parser.add_argument('--epochs', type=int, default=5, help='Default is 3.')
    parser.add_argument('--learning_rate', type=float, default=0.001, help='Default is 0.001.')
    parser.add_argument('--gpu', default=True, help='train on gpu if available' )
    parser.add_argument('--arch', default='vgg19', help='chose either vgg19 or vgg13')
    parser.add_argument('--hidden_units', default=1024, type=int, help='select number of hidden units for second hidden layer. Must be more than 256')
  
    # Parse the arguments
    args = parser.parse_args()
    print(args)
    
    #train the model using the data_directory 
    print(train(args.data_dir, args.dir_name, args.epochs, args.learning_rate, args.gpu, args.arch, args.hidden_units))
   
if __name__ == '__main__':
    main()


