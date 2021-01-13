from Cimpl import *

def red_channel(image):
    """Creates a copy of the original image and a new colour and applies the new 
    red filter over the copy of the image for each pixel by setting the blue and green colouring to 0
    (Cimpl.Image, Cimpl.Image) -> Cimpl.Image
    >>>red_image=red_channel(original_image)
    red_image
    """
    red_image=copy(image)
    for x,y,(r,g,b) in image:
        red=create_color(r,0,0) 
        set_color (red_image, x, y, red)   
    return red_image    

def green_channel(image):
    
    """Returns a copy of the original image and applies a green filter over the
    copied image as the red and blue pixels ar set to 0
    (Cimpl.Image, Cimpl.Image) -> Cimpl.Imagee
    >>> green_image = green_channel(original_image)
    green_image
    """
    
    green_image=copy(image)
    for x,y,(r,g,b) in image:
        green=create_color(0,g,0) 
        set_color (green_image, x, y, green)   
    return green_image

def blue_channel(image):
    
    """Returns a copied image of the original image and a blue applied filter
    (Cimpl.Image, Cimpl.Image) -> Cimpl.Image
    >>> blue_image = blue_channel(original_image)
    blue_image
    """
    blue_image=copy(image)
    for pixel in image:
        x,y,(r,g,b)=pixel
        blue_colour=create_color(0,0,b) 
        set_color (blue_image, x, y, blue_colour)   
    return blue_image

def combine (image1,image2,image3): 
    
    """Returns an image combined of three filtered images of red, green and blue 
    and combines the three rgb pixels 
    (Cimpl.Image,Cimpl.Image,Cimpl.Image) -> Cimpl.Image
    >>>combined_image=combine(red_image,green_image,blue_image)
    combined_image
    """
    combined_image = copy (image1)
    width=get_width(image1)
    height=get_height(image1)
    for x in range(width):
        for y in range(height):
            r1,g1,b1= get_color(image1, x, y)
            r2,g2,b2= get_color(image2, x, y)
            r3,g3,b3= get_color(image3, x, y)  
            new_colour = create_color(r1+r2+r3, g1+g2+g3, b1+b2+b3)
            set_color (combined_image,x,y,new_colour)   
    return combined_image

def two_tone(image:Image,colour1:str,colour2:str)->Image:
    
    """Returns the copy of the original image with an applied two-toned filter based
    on the original image's brightness
    >>>two_toned_image=two_tone(original_image,'black','cyan')
    two_toned_image
    """
    
    if colour1=='black':
        colour1=(0,0,0)
    elif colour1=='white':
        colour1=(255,255,255)
    elif colour1=='red':
        colour1=(255,0,0)
    elif colour1=='lime':
        colour1=(0,255,0)     
    elif colour1=='blue':
        colour1=(0,0,255)     
    elif colour1=='yellow':
        colour1=(255,255,0)    
    elif colour1=='cyan':
        colour1=(0,255,255)  
    elif colour1=='magenta':
        colour1=(255,0,255) 
    elif colour1=='gray':
        colour1=(128,128,128)  
        
    if colour2=='black':
        colour2=(0,0,0)
    elif colour2=='white':
        colour2=(255,255,255)
    elif colour2=='red':
        colour2=(255,0,0)
    elif colour2=='lime':
        colour2=(0,255,0)     
    elif colour2=='blue':
        colour2=(0,0,255)     
    elif colour2=='yellow':
        colour2=(255,255,0)    
    elif colour2=='cyan':
        colour2=(0,255,255)  
    elif colour2=='magenta':
        colour2=(255,0,255) 
    elif colour2=='gray':
        colour2=(128,128,128)        
    
    two_toned_image=copy(image)
    for x,y,(r,g,b) in image:
        brightness = (r+g+b)//3
        if brightness<=127:
            new_color=create_color(colour1[0],colour1[1],colour1[2])
        else:
            new_color=create_color(colour2[0],colour2[1],colour2[2])
        set_color(two_toned_image,x,y,new_color)  
    return two_toned_image   

def three_tone(image:Image,colour1:str,colour2:str,colour3:str)->Image:
    
    """Returns a copy of the original image with an applied three-toned filter
    on all pixels of the image based on each pixel's brightness
    >>>three_toned_image=three_tone(original_image,'magenta','cyan','yellow')
    three_toned_image
    """
    
    if colour1=='black':
        colour1=(0,0,0)
    elif colour1=='white':
        colour1=(255,255,255)
    elif colour1=='red':
        colour1=(255,0,0)
    elif colour1=='lime':
        colour1=(0,255,0)     
    elif colour1=='blue':
        colour1=(0,0,255)     
    elif colour1=='yellow':
        colour1=(255,255,0)    
    elif colour1=='cyan':
        colour1=(0,255,255)  
    elif colour1=='magenta':
        colour1=(255,0,255) 
    elif colour1=='gray':
        colour1=(128,128,128)  
        
    if colour2=='black':
        colour2=(0,0,0)
    elif colour2=='white':
        colour2=(255,255,255)
    elif colour2=='red':
        colour2=(255,0,0)
    elif colour2=='lime':
        colour2=(0,255,0)     
    elif colour2=='blue':
        colour2=(0,0,255)     
    elif colour2=='yellow':
        colour2=(255,255,0)    
    elif colour2=='cyan':
        colour2=(0,255,255)  
    elif colour2=='magenta':
        colour2=(255,0,255) 
    elif colour2=='gray':
        colour2=(128,128,128)    
        
    if colour3=='black':
        colour3=(0,0,0)
    elif colour3=='white':
        colour3=(255,255,255)
    elif colour3=='red':
        colour3=(255,0,0)
    elif colour3=='lime':
        colour3=(0,255,0)     
    elif colour3=='blue':
        colour3=(0,0,255)     
    elif colour3=='yellow':
        colour3=(255,255,0)    
    elif colour3=='cyan':
        colour3=(0,255,255)  
    elif colour3=='magenta':
        colour3=(255,0,255) 
    elif colour3=='gray':
        colour3=(128,128,128)
        
    three_toned_image=copy(image)
    for x,y,(r,g,b) in image:
        brightness = (r+g+b)//3
        if brightness<=84:
            new_color=create_color(colour1[0],colour1[1],colour1[2])
        
        elif 85<=brightness<=170:
            new_color=create_color(colour2[0],colour2[1],colour2[2])
            
        else:
            new_color=create_color(colour3[0],colour3[1],colour3[2])
        set_color(three_toned_image,x,y,new_color)  
    return three_toned_image

FILENAME=('miss_sullivan.jpg')
original_image=load_image(FILENAME)
show(original_image)

red_image=red_channel(original_image)
show(red_image)
save_as(red_image,'red_image.jpg')

green_image=green_channel(original_image)
show(green_image)
save_as(green_image,'green_image.jpg')

blue_image=blue_channel(original_image)
show(blue_image)
save_as(blue_image,'blue_image.jpg')

combined_image=combine(red_image,green_image,blue_image)
show(combined_image)
save_as(combined_image,'combined_image.png')

two_toned_image=two_tone(original_image,'lime','magenta')
show(two_toned_image)
save_as(two_toned_image,'two_toned_image.png')

three_toned_image=three_tone(original_image,'cyan','magenta','yellow')
show(three_toned_image)
save_as(three_toned_image,'three_toned_image.png')
