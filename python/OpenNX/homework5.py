# nx: threaded

from shapes.block import Block

import SimpleITK as sitk
import math

import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences

import numpy

#I couldn't get this code to work due to errors importing some modules in SimpleITK.
#NX can find the library itself, but not some of the files 


def main():

    #Creates an image object that can be analyzed
    
    image = sitk.ReadImage('C:/Users/Bruker/Desktop/Panda.jpg')
    #Get the position of the starting pixel
    #Never actually used in this code, but could be useful for other projects
    origin = image.GetOrigin()
    print("marker")
    print(origin)
    #Width and height in number of pixels
    width = image.GetWidth()
    height = image.GetHeight()
    print(width)
    print(height)

    #Standard block size
    block_dim = 1
    
    #Iterate through all the pixels
    #for x in range(0,width):
    #   for y in range(0,height):
    for x in range(0,width):
        oneblock = 0
        lastblockblack = False
        start_x = x
        start_y = 0
        for y in range(0,height,3):
            
            #This returns a tuple of the rgb code in a specific pixel
            pixel = image.GetPixel(x,y)
            print(pixel)

            #If black -> creae a block
            if pixel == (0,0,0) and lastblockblack==True:
                #The block will be placed somewhere on in the x-y-frame corresponding to the pixel position
                oneblock+=3
            elif pixel == (0,0,0) and lastblockblack==False:
                lastblockblack = True
                oneblock+=3
                start_y = y
            elif pixel != (0,0,0) and lastblockblack==True:
                lastblockblack = False
                block = Block(start_x+block_dim, 0, start_y+block_dim, 
                    block_dim, block_dim, oneblock, color = "Black")
                block.initForNX()
                oneblock = 0
            else:
                pass
    return 0

main()