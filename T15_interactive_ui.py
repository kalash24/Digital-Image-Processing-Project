# ECOR1051 Milestone 3 P8: Interactive User Interface
# Lab Session: L-1A
# Team 15: The Brogrammers
# Date of Submission: April 2, 2020

# Team Members:
# Dorothy Tran 101141902
# Kian Zalzalah 101148652
# Joahkim Vaudrin-Moisan 101153491

from Cimpl import *
from T15_image_filters import *

def user_interface()->str:
    """Author: Dorothy Tran
    .......
    L)oad imagee S)ave as
    2)-tone 3)-tone X)treme contrast T)int sepia P)osterize
    E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip
    Q)uit

    : 
    """
    print ('L)oad imagee S)ave as')
    print ('2)-tone 3)-tone X)treme contrast T)int sepia P)osterize')
    print ('E)dge detect I)mproved edge detect V)ertical flip H)orizontal flip')
    print ('Q)uit')
    print()
    input_filter=input(': ',).upper()
    return input_filter

commands = ['L','S','2','3','X','T','P','E','I','V','H','Q']

def apply_filter(selected_filter:int)->Image:
    """Author: Dorothy Tran
    .......
    
    >>>input_filter=user_interface()
    >>>apply_filter(input_filter)  
    """
    image_loaded = False  
    if selected_filter == commands[11]:
        image = None
        print('No Image Loaded')
        selected_filter = user_interface()  
        
    while selected_filter != commands[11]:
        if selected_filter in commands:
            if selected_filter == commands[0]:
                image_loaded = True
                image = load_image(choose_file())
                show(image)
                
            elif selected_filter == commands[1]:
                new_image = copy(image)
                save_as(new_image,'filtered_image.jpg')              
                
            elif selected_filter == commands[2]:
                new_image = copy(image)
                two_toned = two_tone(new_image,'yellow','cyan')
                show(two_toned)
            
            elif selected_filter == commands[3]:
                new_image = copy(image)
                three_toned = three_tone(new_image,'yellow','cyan','magenta')
                show(three_toned)
                
            elif selected_filter == commands[4]:
                new_image = copy(image)
                contrast_image = extreme_contrast(new_image)
                show(contrast_image)
                
            elif selected_filter == commands[5]:
                new_image = copy(image)
                sepia_tone = sepia(new_image) 
                show(sepia_tone)
                
            elif selected_filter == commands[6]:
                new_image = copy(image)
                posterized_image = posterize(new_image)
                show(posterized_image)
            
            elif selected_filter == commands[7]:
                new_image = copy(image)
                threshold=input('Enter a Threshold Value: ')
                edge_detection = detect_edges(new_image,int(threshold))
                show(edge_detection)
                                        
            elif selected_filter == commands[8]:
                new_image = copy(image)
                threshold=input('Enter a Threshold Value: ')
                improved_edge_detection = detect_edges_better(new_image,int(threshold)) 
                show(improved_edge_detection)
                
            elif selected_filter == commands[9]:
                new_image = copy(image)
                vertical_flip_image = flip_vertical(new_image) 
                show(vertical_flip_image)
                
            elif selected_filter == commands[10]:
                new_image = copy(image)
                horizontal_flip_image = flip_horizontal(new_image) 
                show(horizontal_flip_image)
    
            elif image_loaded != True:
                print ('No Image Loaded')
            selected_filter = user_interface()
            
        else:
            print('No Such Command')
            selected_filter = user_interface()
                 
input_filter=user_interface()
apply_filter(input_filter)        
        