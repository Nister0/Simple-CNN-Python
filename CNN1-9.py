'''
Project Based on:
https://victorzhou.com/blog/intro-to-cnns-part-1/

Implemented:
Greyscaler. - its implemented in Pillow but i want to be minimal.
              So im implementing it manually 

Planned: 
other greyscalers
3x3 conv layer - transforms layer for example find edges
2x2 pooling layer - downscale image
softmax layer -> turn output into probabilities
'''

from PIL import Image 
import numpy as np 

class Greyscaler:
    #class to greyscale images
    def __init__(self):
        pass

    def average(self, image):
        ''' 
        the average function converts RGB Images to Greyscale
        Based on the Average of each color.
        Easy to implement but not optimal
        '''

        '''ensure image is RGB so getpixel returns an (r,g,b) tuple'''
        image = image.convert("RGB")

        w, h = image.size

        output = np.zeros((h, w, 3), dtype=np.uint8)

        for i in range(h):
            for j in range(w):
                r, g, b = image.getpixel((j, i))
                avg = (r + g + b) // 3
                output[i, j] = (avg, avg, avg) 
                '''maybe i will make the output a 1d array as i only need one value to optimize the storage and runspeed'''
        return output
    
class Conv:
    '''Class to add customizable convulution layers i.e. 3x3, 5x5 and so on'''

    def __init__(self, size, num_filters, padding = 0, variance = 9):

        self.size = size
        self.num_filter = num_filters
        self.padding = padding
        self.variance = variance
        self.filters = np.random.randn(num_filters, size, size) / variance

    def pad_image(self, image):
        
        w, h = image.size

        padding = self.padding

        new_w = w+(padding*2)
        new_h = h+(padding*2)

        output = np.zeros((new_h, new_w, 3), dtype =np.uint8)

        for i in range(new_h):
            for j in range(new_w):
                if i < padding:
                    output[i,j] = (0,0,0)
                elif i >= new_h-padding:
                    output[i,j] = (0,0,0)
                elif j < padding: 
                    output[i,j] = (0,0,0)
                elif j >= new_w-padding:
                    output[i,j] = (0,0,0)
                else:
                    r,g,b = image.getpixel((j-padding, i-padding))
                    output[i,j] = (r,g,b)
                    '''same as in the greyscaler -> 1d array.'''
        return output


    def iterate_regions(self, image):
        '''Generates all size x size image regions using the padded image if wanted.'''

        w, h = image.size

        offset = (self.size // 2) * 2 

        for i in range(h-offset):
            for j in range(w-offset):
                get_region = False


        return get_region

im = Image.open("Testimage.png")
#im.show()

'''Tests for the Greyscale class and functions.'''
greyscale = Greyscaler()
grey_output = greyscale.average(im)
imgr = Image.fromarray(grey_output)
#imgr.show()

'''arr = np.zeros((5,5,3), dtype = np.uint8)
for i in range(5):
    for j in range(5):
        if (i+j) % 2 == 0:
            arr[i, j] = (255, 55, 255)
        else:
            arr[i,j] = (50, 100, 255)

testimg = Image.fromarray(arr)'''

'''Test for the padding function'''
conv = Conv(3, 1, 1)
impadded = Image.fromarray(conv.pad_image(imgr))
#impadded.show()