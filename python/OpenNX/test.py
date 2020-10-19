# nx: threaded

try:
    import numpy
except:
    print("Something wrong definetly happened")
import SimpleITK as sitk
#import numpy

def main():
    image = sitk.ReadImage('C:/Users/Bruker/Desktop/Panda.jpg')
    #Get the position of the starting pixel
    #Never actually used in this code, but could be useful for other projects
    origin = image.GetOrigin()
    
    #Width and height in number of pixels
    width = image.GetWidth()
    height = image.GetHeight()

    #Standard block size
    block_dim = 1
    
    #Iterate through all the pixels
    #for x in range(0,width):
    #   for y in range(0,height):
    
    for x in range(0,width):
        for y in range(0,height):
            
            #This returns a tuple of the rgb code in a specific pixel
            pixel = image.GetPixel(x,y)
            print(pixel)

            #If black -> creae a block
            if pixel != (255,255,255):
                print("")
main()