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
    def __init__(self, size, num_filters, padding = False, variance = 9):
        self.size = size
        self.num_filter = num_filters
        self.padding = padding
        self.variance = variance
        self.filters = np.randn(num_filters, size, size) / variance

    def iterate_regions(self, image):
        

    
im = Image.open("Testimage.png")
#im.show()
greyscale = Greyscaler()
grey_output = greyscale.average(im)
imgr = Image.fromarray(grey_output, "RGB")
