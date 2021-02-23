# 1051Project
Digital Image Processing Project

Contact Information:
____________________

Project Leader: Dorothy Tran
E-mail: dorothytran@cmail.carleton.ca


Description:
____________

The project contains three programs that will digitally process an image of choice. The interactive user interface file is a text-based system that allows the user to apply image filters as the filters are cumulative, onto an image of the user's choice. The user will manually input filters into the python shell as the program includes saving and loading features. The batch user interface file is a file-based system that allows users to combine different letters which are assigned filters, to be applied onto the image of their choice based on the created text file by the user. The images will be then applied and saved as new images.

The project is made up of three files:

T15_image_filters.py 		 Python script containing 13 digital image processing filters

T15_batch_ui.py			 Python script that runs the File-Based System to apply filters on images

T15_interactive_ui.py		 Python script that runs the Text-Based System user input to apply filters


Installation:
_____________

To successfully run the program, the user must install Python 3.8.1 or later versions for their programming environment, as well as the latest version of Pillow. External modules required for the program is the Cimpl Library Version 1.04 created by Carleton University. The minimum system requirements to run the interface are an operating system of Windows 7 or higher and OS X 10.7 for Mac. The user is also recommended to use a processor of 5th generation or later. 


Usage:
______

1. Launch a programming environment of choice. (Preferably Wing 101)

3. Open the file, "T15_interactive_ui.py" for the Text-Based system and the file, "T15_batch_ui.py" for the File-Based system.

3. Once the file chosen is open, locate the green arrow on the toolbar of the programming environment and run the program.

4. If the "T15_interactive_ui.py" file is executed, a menu containing a list of valid commands will launch in the python shell on the bottom right of the screen.
	- Load an image by typing "L" into the python shell and pressing Enter
	- A directory will be launched on your screen and you must select an image file from the directory that you want to apply filters onto
	- Using the valid commands listed in the python shell, the filter of choice may be applied to the image selected by typing the letter into the python shell (ie. 3, T, H, P)
	- When satisfied with the filtered image, type "S" into the python shell to save the image into your directory
	- If you are not satisfied with the filtered image created, type "Q" into the python shell to quit the program and you may restart by rerunning the program referring to step 3

5. If the "T15_batch_ui.py" file is executed, you must create a text file by opening Notepad.
	- Within the notepad, type the name of the selected image file you want to filter
	- Click the space bar and name the new filtered image
	- Indicate the desired filters you want to apply onto the selected image by clicking the space bar and entering the filters you want with the following options:
		
			"2" : Two-Tone Filter
			"3" : Three- Tone Filter
			"X" : Extreme Contrast Filter
			"T" : Sepia Tinting Filter
			"E" : Edge Detection Filter
			"I" : Improved Edge Detection Filter
			"V" : Vertical Flip
			"H" : Horizontal Flip
	
6. With the created text file containing your desired filters, run the program by locating the green arrow on the toolbar of the programming environment.
	- Within the python shell, it will ask to input the file name of the batch file created.
	- Enter the name of the batch file you created into the shell and click Enter
	- When the program is executed, the new filtered images will be saved into your directory as you may view your new filtered images


Credits:
________

== Filter Functions ==

Red Filter Function: Kian Zalzalah
Green Filter Function: Joahkim Vaudrin-Moisan
Blue Filter Function: Dorothy Tran
Combined RGB Filter Function: Dorothy Tran
Two-toned Filter Function: Dorothy Tran
Three-toned Filter Function: Dorothy Tran
Extreme Contrast Filter Function: Kian Zalzalah
Sepia tone Filter Function: Joahkim Vaudrin-Moisan
Adjust Component Function: Kian Zalzalah
Posterized Filter Function: Kian Zalzalah
Edge Detection Filter Function: Dorothy Tran
Improved Edge Detection Filter Function: Dorothy Tran
Vertical Flip Filter Function: Joahkim Vaudrin-Moisan
Horizontal Flip Filter Function: Joahkim Vaudrin-Moisan

== Filter Test Functions ==

Red Filter Test Function: Kian Zalzalah
Green Filter Test Function: Joahkim Vaudrin-Moisan
Blue Filter Test Function: Dorothy Tran
Combined RGB Filter Test Function: Dorothy Tran
Two-toned Filter Test Function: Joahkim Vaudrin-Moisan
Three-toned Filter Test Function: Joahkim Vaudrin-Moisan
Extreme Contrast Filter Test Function: Dorothy Tran
Sepia tone Filter Test Function: Kian Zalzalah
Posterized Filter Test Function: Dorothy Tran
Edge Detection Filter Test Function: Kian Zalzalah
Improved Edge Detection Filter Test Function: Kian Zalzalah
Vertical Flip Filter Test Function: Dorothy Tran
Horizontal Flip Filter Test Function: Dorothy Tran

== User Interface Functions ==

User Interface Function: Dorothy Tran
Apply Filter Function: Dorothy Tran
Batch User Interface Function: Joahkim Vaudrin-Moisan and Kian Zalzalah


License:
________

Copyright 2020 Dorothy Tran, Kian Zalzalah & Joakhim Vaudrin-Moisan. All rights reserved.

