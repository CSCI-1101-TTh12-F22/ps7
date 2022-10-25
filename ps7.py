import PySimpleGUI as sg
import tkinter as tk
import BCImage3
import math


# I've provided two functions for you to try and that
# you can use as a guide for when you write your own.

# Reminder: In every pixel
# * the red (r) component is index 0
# * the green (g) component is index 1
# * the blue (b) component is index 2


# ~~~~~~~~~~~~~~~~~~~~~
# COLORSWITCH FUNCTION
# ~~~~~~~~~~~~~~~~~~~~~

# * replace the red value (i.e., index 0) with green value
# * replace green value (i.e., index 1) with blue value
# * replace blue value (i.e., index 2) with red value

def colorswitch(im):

    # height is the number of rows of pixels in the image
    height=len(im) 

    # width is the number of columns of pixes in the image
    width = len(im[0])

    # for every row...
    for row in range(height):

        # for each pixel in that row (i.e., each column)
        for col in range(width):

            # get the pixel using row, col
            pixel=im[row][col]

            # save out the value of each component of the pixel
            # r(ed)=0, g(reen)=1, b(lue)=2
            r=pixel[0]
            g=pixel[1]
            b=pixel[2]

            # In the red component, put the green value.
            im[row][col][0] = g

            # In the green component, put the blue value.
            im[row][col][1] = b

            # In the blue component, put the red value.
            im[row][col][2] = r

    # return the altered image        
    return im



# ~~~~~~~~~~~~~~~~~~~~~
# MIRROR FUNCTION
# ~~~~~~~~~~~~~~~~~~~~~

# Here we will create a new image rather than altering the old image.

# In each row, we copy the first pixel in the input image to the
# last pixel in the output image. We copy the second pixel in the
# input image to the second-to-last pixel in the output image, etc.
# Then we return the new image.

def flip_horizontal(im):
    height = len(im)
    width = len(im[0])

    # Create an empty list that will contain the new image.
    # Will will append each new row to this list.
    # We will call this new image our "output image".
    newim=[] 

    # Consider every "input row" in the the original image.
    for row in range(height):

        # Create an empty list that will contain the new "output row".
        newrow=[]

        # For each pixel in the input row, you'll put that
        # pixel in the output row exactly as far away from the end
        # as it was from the beginning in the input row.
        for col in range(width):

            # Example: Imagine the column number is 4, and the total number
            # of columns is 100. Your new row should have whatever
            # was in column 4 in the input (i.e., the 5th from the beginning)
            # appear in column 95 (i.e., the 5th from the end).
            # How would you get 95 using 100 and 4?
            # 100-1-4 = 95 ===>  width-1-col
            
            newrow.append(im[row][width-1-col])

        # Once you have created your new output row, append it to your output image.    
        newim.append(newrow)

    # return your new image    
    return newim



# ~~~~~~~~~~~~~~~~~~~
# GREYSCALE FUNCTION
# ~~~~~~~~~~~~~~~~~~~

# In each pixel, replace each individual r, g, or b value with the
# average of all three values for that pixel.

# Use the colorswitch() function as a guide. In other words, you can
# basically copy and paste the colorswitch() function here, and then
# just update the last three lines of code (not comments) to set each
# component of each pixel to the average of r, g, and b for that pixel.

def greyscale(im):

    ## INSERT YOUR CODE HERE!

  
    return im


# ~~~~~~~~~~~~~~~~~~~
# MONOCHROME FUNCTION
# ~~~~~~~~~~~~~~~~~~~

# Use the colorswitch() function as a guide. In other words, you can
# basically copy and paste the colorswitch() function here, and then
# just update the last few lines of code (not comments).
# To make an image monochrome, take each pixel and sum all three components.
# If the sum exceeds some threshold, set the pixel to [255, 255, 255] for
# white. Otherwise, set the pixel to [0,0,0] for black.
# You can experiment with different thresholds to pick the one you like best.

def monochrome(im):

    ## INSERT YOUR CODE HERE!

  
    return im


# ~~~~~~~~~~~~~~~~~~~~~~~~
# UPSIDE DOWN FUNCTION
# ~~~~~~~~~~~~~~~~~~~~~~~~

# This time use the mirror function as a guide, but instead of
# swapping pixels across an imaginary vertical line through the middle,
# swap them across an imagine horizontal line through the middle.

# You will create a new image, just as I did in mirror().
# Use the mirror() code as a guide.

def upsidedown(im):

    ## INSERT YOUR CODE HERE!

  
    return im


# ~~~~~~~~~~~~~~~~~~~
# PIXELATE FUNCTION
# ~~~~~~~~~~~~~~~~~~~

# This is *optional*. No extra credit will be given. It's just here for fun.
# See the problem set for details.



# ~~~~~~~~~~~~~~~~~~~~~~
# ADDING BUTTONS TO GUI
# ~~~~~~~~~~~~~~~~~~~~~~

# Below, effects is a  dictionary, with each item consisting of an
# effect name  (a string that appears on the button) and a function
# that implements the effect.  To add a new effect, you have to write
# the function above and then add a new pair to the dictionary.

effects={'Color Switch':colorswitch,'Mirror':flip_horizontal}


#________________________________________________________________

# DO NOT CHANGE ANYTHING BELOW THIS LINE!

#________________________________________________________________

# The Graphical User Interface.

# This uses the PySimpleGUI package, which is somewhat simpler to work
# with than the standard tkinter GUI for Python.  However, we have to (?)
# import tkinter directly in order to have access to the PhotoImage data
# type.

# The functions getPixels and setPixels, for reading the image file into
# a 3D array, and for rendering it on the canvas, were originally
# dveloped by now-retired Prof. Bill Ames, and updated for Python 3 by
# Howard Straubing. 


def draw(imarray):
    photo=tk.PhotoImage(height=len(imarray),width=len(imarray[0]))
    BCImage3.setPixels(photo,imarray)
    canvas.TKCanvas.image=photo
    canvas.TKCanvas.create_image(400,300,image=photo)

# create the buttons associated with effects.  There will be a maximum
# of 12 buttons in each row, and a maximum of 24 effects.

button_names=list(effects.keys())
row1=[sg.Button(button_names[j]) for j in range(min(12,len(button_names)))]
row2=[sg.Button(button_names[j]) for j in range(12,min(24,len(button_names)))]


layout=[[sg.Canvas(size=(800,600),key='CANVAS')],[sg.Text('Filename:'),\
        sg.Input(key='FileName'), sg.FileBrowse(key='FileBrowse'),\
         sg.Button('Load'),sg.Button('Exit')],
        row1,row2]

window = sg.Window('Photoshop', layout)
window.Finalize()
canvas = window['CANVAS'] 


    
while True:
    event, values = window.read()
    
        
    if event=='Load':
        filename=values['FileName']
        s=BCImage3.getPixels(filename)
        draw(s)
    elif event in button_names:
        effect=effects[event]
        s=effect(s)
        draw(s)
        
    elif event in (None, 'Exit'):   # if user closes window or clicks cancel
        window.close()
        break
