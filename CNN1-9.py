'''
Project Based on:
https://victorzhou.com/blog/intro-to-cnns-part-1/

Implemented:
Greyscaler. - its implemented in Pillow but i want to be minimal.

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
        ''' the average function converts RGB Images to Greyscale
            Based on the Average of each color.
            Easy to implement but not optimal
        '''
        # ensure image is RGB so getpixel returns an (r,g,b) tuple
        image = image.convert("RGB")
        w, h = image.size
        output = np.zeros((h, w, 3), dtype=np.uint8)

        for i in range(h):
            for j in range(w):
                r, g, b = image.getpixel((j, i))
                avg = (r + g + b) // 3
                output[i, j] = (avg, avg, avg)

        return output
    
class Conv:
    #Class to add customizable convulution layers 
    def __init__(self, size, num_filters, padding = 0, variance = 9):
        self.size = size
        self.num_filter = num_filters
        self.padding = padding
        self.variance = variance
        self.filters = np.randn(num_filters, size, size) / variance

    def pad_image(self, image):
        
        h,w = image.size

        padding = self.padding

        size = self.size

        new_h, new_w = h+size, w+size

        padded_image = np.zeros((new_h, new_w, 3), dtype =np.uint8)

        for i in range(new_h):
            for j in range(new_w):
                if i <= padding:
                    padded_image[i,j] = (0,0,0)
                elif i >= new_h-padding:
                    padded_image[i,j] = (0,0,0)
                elif j <= padding: 
                    padded_image[i,j] = (0,0,0)
                elif j >= new_w-padding:
                    padded_image[i,j] = (0,0,0)
                else:
                    r,g,b = image.getpixel((j, i))
                    padded_image[i,j] = (r,g,b)

        return Image.fromarray(padded_image, "RGB")


    def iterate_regions(self, image):
        '''
        Generates all size x size image regions using the padded image.
        '''
        pass    

im = Image.open("Testimage.png")
#im.show()
greyscale = Greyscaler()
grey_output = greyscale.average(im)
imgr = Image.fromarray(grey_output, "RGB")
