# ECOR1051 Milestone 2 P6: Final Test Function Code
# Lab Session: L-1A
# Team 15: The Brogrammers
# Date of Submission: March 26, 2020

# Team Members:
# Dorothy Tran 101141902
# Kian Zalzalah 101148652
# Joahkim Vaudrin-Moisan 101153491

from Cimpl import *
from unit_testing import check_equal
from T15_image_filters import *

def test_red(original,new)->None:
    
    """Author: Kian Zalzalah 101148652
    Checks if new image shares the same red colour for each pixel and if there 
    is any green or blue present. If so, the test will pass and the red filter will
    be proven as a correct filter
    >>>test=test_red(original_image,red_image)
    The Red Filter Passed the Test
    """
    width=get_width(original)
    height=get_height(original)
    for x in range (width):
        for y in range (height):
            r1,g1,b1=get_color(original,x,y)
            r2,g2,b2=get_color(new,x,y)
            if (r1==r2) and (g2!=0) and (b1!=0):
                return ('The Red Filter Failed the Test')
            return ('The Red Filter Passed the Test')


def testing_green(original_image, new)->None:
    
    """Author: Joahkim Vaudrin-Moisan 101153491
    Return if all the pixels on the image are green and identifies the pixels 
    that are not.
    >>> testing_green(original, green_image)
    The Green Filter Passed the Test
    """
    width=get_width(original_image)
    height=get_height(original_image)
    for x in range (width):
        for y in range (height):
            r1,g1,b1=get_color(original_image,x,y)
            r2,g2,b2=get_color(new,x,y)
            if (r2!=0) and (g2!=g1) and (b2!=0):
                return ('The Green Filter Failed the Test at', (x,y))
            return('The Green Filter Passed the Test')                  


def test_blue(original,new)->None:
    
    """Author: Dorothy Tran 101141902
    Function tests each pixel of the image if the new filtered image only has
    blue pixels
    >>> test=test_blue(original_image,blue_image)
    The Blue Filter Passed the Test
    """
    width=get_width(original)
    height=get_height(original)
    for x in range (width):
        for y in range (height):
            r1,g1,b1=get_color(original,x,y)
            r2,g2,b2=get_color(new,x,y)
            if (r2!=0) and (g2!=0) and (b1!=b2):
                return ('The Blue Filter Failed the Test at', x,y)
            return ('The Blue Filter Passed the Test')
 
        
# Dorothy Tran 101141902
def test_combine (original,new)->None:
    
    """Author: Dorothy Tran 101141902
    Function tests if each pixel of the image is combined of three rgb 
    filtered images and returns if the test successfully passed
    >>>test_combine(original_image,combined_image)
    The Combined Filter Passed the Test
    """   
    fail=False
    for pixel in new:
        x, y, (r, g, b) = pixel
        r1,g1,b1= get_color(original,x,y)
        r2,g2,b2= get_color(new,x,y)
        if ((r1!=r2) and (g1!=g2) and (b1!=b2)):
            fail=True
            print ("The Combined Filter Failed at",x,y)
    if fail==False:
        print ("The Combined Filter Passed the Test")         


def test_two_tone()-> None:
    
    """Author: Joahkim Vaudrin-Moisan 101153491
    Return if the pixels have the correct colour configuration, 
    being the first colour if the average RGB value is lower than 128 and the
    latter if the average is 128 or above.
    >>>test_two_tone()
    Checking pixel @(0,0) PASSED
    ------
    Checking pixel @(1,0) PASSED
    ------
    """
    original = create_image(2, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(155, 203, 180))
    
    expected = create_image(2, 1)
    set_color(expected, 0, 0,  create_color(255, 0, 255))
    set_color(expected, 1, 0,  create_color(255, 255, 0))
    
    actual_filtered_image = two_tone(original, 'magenta', 'yellow')
    for x, y, col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ',' + str(y) +')',
                    col, get_color(expected, x, y))


def test_three_tone() -> None:
    
    """Author: Joahkim Vaudrin-Moisan 101153491
    Return if the pixels have the correct colour configuration, 
    being the first colour if the average RGB value is lower than 85, the 
    middle colour if the average is between 85 and 170, and the latter if
    the average is 171 or above.
    >>>test_three_tone()
    Checking pixel @(0,0) PASSED
    ------
    Checking pixel @(1,0) PASSED
    ------
    Checking pixel @(2,0) PASSED
    ------
    """    
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(155, 203, 180))
    set_color(original, 2, 0,  create_color(75, 100, 100))
    
    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(255, 0, 255))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(255, 255, 0))
    
    actual_filtered_image = three_tone(original, 'magenta', 'yellow', 'black')
    for x, y, col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ',' + str(y) +')',
                    col, get_color(expected, x, y))

      
def test_extreme()->None:
    
    """Author: Dorothy Tran 101141902
    Returns a 3x1 image created with the applied extreme contrast filter and 
    tests if the first six pixels are filtered with the expected rgb values
    >>> test_extreme()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    """
    
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(125, 90, 129))
    set_color(original, 2, 0,  create_color(113, 157, 182))

    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0,0,0))
    set_color(expected, 1, 0,  create_color(0, 0, 255))
    set_color(expected, 2, 0,  create_color(0, 255, 255))    

    contrast_image=extreme_contrast(original)
    for x, y, col in contrast_image: 
        check_equal('Checking pixel @(' + str(x)+ ', ' +str(y) + ')',
                     col,get_color(expected, x, y))  
        
        
def test_sepia() -> None:
    
    '''Author:Kian Zalzalah 101148652
    Tests the detect edges filter by passing a new image through the filter
    with expected values to ensure properties of filter are correct.
    >>> test_sepia()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    '''
    original_image = create_image(3, 1)
    set_color(original_image, 0, 0,  create_color(0, 0, 0))
    set_color(original_image, 1, 0,  create_color(127, 127, 127))
    set_color(original_image, 2, 0,  create_color(255, 255, 255))

    expected_image = create_image(3, 1)
    set_color(expected_image, 0, 0,  create_color(0, 0, 0))
    set_color(expected_image, 1, 0,  create_color(146, 127, 107))
    set_color(expected_image, 2, 0,  create_color(255, 255, 237))
     
    sepiated = sepia(original_image)
    for x, y, col in sepiated:  
        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected_image, x, y))
 

def test_posterize()->None:
    
    """Author: Dorothy Tran 101141902
    Returns a 3x1 image created with the applied posterized filter and tests if
    the first three pixels are filtered with the expected rgb values
    >>> test_posterize()   
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    """
    
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(145, 120, 136))
    set_color(original, 2, 0,  create_color(113, 157, 134))   
    
    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(31,31,31))
    set_color(expected, 1, 0,  create_color(159, 95, 159))
    set_color(expected, 2, 0,  create_color(95, 159, 159))   

    posterized_image=posterize(original)
    for x, y, col in posterized_image: 
        check_equal('Checking pixel @(' + str(x)+ ', ' +str(y) + ')',
                     col,get_color(expected, x, y))

        
def test_detect_edges() -> None:
    
    """Author: Kian Zalzalah 101148652
    Tests the detect edges filter by passing a new image through the filter
    with expected values to ensure properties of filter are correct.
    >>>test_detect_edges()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    """
    original_image = create_image(2, 2)
    set_color(original_image, 0, 0, create_color(44, 44, 44))
    set_color(original_image, 0, 1, create_color(200, 200, 200))
    set_color(original_image, 1, 0, create_color(144, 144, 144))
    set_color(original_image, 1, 1, create_color(200, 200, 200))
    
    expected_image = create_image(2, 2)
    set_color(expected_image, 0, 0, create_color(0, 0, 0))
    set_color(expected_image, 0, 1, create_color(255, 255, 255))
    set_color(expected_image, 1, 0, create_color(0, 0, 0))
    set_color(expected_image, 1, 1, create_color(255, 255, 255))
    
    detected_image = detect_edges(original_image, 10)
    for x, y, col in detected_image:
        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_image, x, y))        
        
       
def test_detect_edges_better() -> None:
    
    """Author: Kian Zalzalah 101148652
    Tests the improved detect edges filter by passing a new image through the filter
    with expected values to ensure properties of filter are correct.
    >>>test_detect_edges_better()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    """
    original_image = create_image(2, 2)
    set_color(original_image, 0, 0, create_color(44, 44, 44))
    set_color(original_image, 0, 1, create_color(200, 200, 200))
    set_color(original_image, 1, 0, create_color(144, 144, 144))
    set_color(original_image, 1, 1, create_color(200, 200, 200))
    
    expected_image = create_image(2, 2)
    set_color(expected_image, 0, 0, create_color(255, 255, 255))
    set_color(expected_image, 0, 1, create_color(200, 200, 200))
    set_color(expected_image, 1, 0, create_color(255, 255, 255))
    set_color(expected_image, 1, 1, create_color(200, 200, 200))
    
    detected_image_better = detect_edges_better(original_image, 10)
    for x, y, col in detected_image_better:
        
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_image, x, y))
    
   
def test_flip_vertical()-> None: 
   
    """Author: Dorothy Tran 101141902  
    Returns a 3x1 image and tests to see if each pixel of the image is
    vertically flipped when filter is applied respect to the x axis
    >>>test_flip_vertical() 
    Checking pixel at (0, 0): PASSED
    ------
    Checking pixel at (1, 0): PASSED
    ------
    Checking pixel at (2, 0): PASSED
    ------
    """
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(125, 90, 129))
    set_color(original, 2, 0,  create_color(113, 157, 182))    
    
    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(113,157,182))
    set_color(expected, 1, 0,  create_color(125, 90, 129))
    set_color(expected, 2, 0,  create_color(0, 0, 0))     

    vertically_flipped_image=flip_vertical(original)
    for x, y, col in vertically_flipped_image: 
        check_equal('Checking pixel at (' + str(x)+ ', ' +str(y) + '):',
                     col,get_color(expected, x, y))   


def test_flip_horizontal()->None:
    
    """Author: Dorothy Tran 101141902 
    Returns a 3x1 image and tests to see if each pixel of the image is horizontally respect to the y axis
    flipped comparing to the original image
    >>>test_flip_horizontal()  
    Checking pixel at (0, 0): PASSED
    ------
    Checking pixel at (1, 0): PASSED
    ------
    Checking pixel at (2, 0): PASSED
    ------
    """
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(125, 90, 129))
    set_color(original, 2, 0,  create_color(113, 157, 182))
    
    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0,0,0))
    set_color(expected, 1, 0,  create_color(125, 90, 129))
    set_color(expected, 2, 0,  create_color(113, 157, 182))    
  
    horizontal_flipped_image=flip_horizontal(original)
    for x, y, col in horizontal_flipped_image: 
        check_equal('Checking pixel at (' + str(x)+ ', ' +str(y) + '):',
                     col,get_color(expected, x, y))    
        

# MAIN CODE
test=test_red(original_image,red_image)
print(test)
print('------')
test=testing_green(original_image,green_image)
print(test)
print('------')
test=test_blue(original_image,blue_image)
print(test)
print('------')
test_combine(original_image,combined_image)
print('------')
print()
print('Testing the Two Tone Filter:')
test_two_tone()
print()
print('Testing the Three Tone Filter:')
test_three_tone()
print()
print('Testing the Extreme Contrast Filter:')
test_extreme() 
print()
print('Testing the Sepia Tone Filter:')
test_sepia()
print()
print('Testing the Posterized Filter:')
test_posterize()
print()
print('Testing the Edge Detection Filter:')
test_detect_edges()
print()
print('Testing the Improved Edge Detection Filter:')
test_detect_edges_better()
print()
print('Testing the Vertical Flip Filter:')
test_flip_vertical()
print()
print('Testing the Horizontal Flip Filter:')
test_flip_horizontal()    