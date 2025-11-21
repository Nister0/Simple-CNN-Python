'''
https://victorzhou.com/blog/intro-to-cnns-part-1/
Greyscaler. - its implemented in Pillow but i want to be minimal.
3x3 conv layer - transforms layer for example find edges
2x2 pooling layer - downscale image
softmax layer -> turn output into probabilities
'''

from PIL import Image 
import numpy as np 

class Greyscaler:
    def __init__(self):
        pass

    def average(self, image):
        ''' the average function converts RGB Images to Greyscale
            Based on the Average of each color.
            Easy to implement but not optimal
        '''
        h, w = image.shape

        output = np.zeros((h, w), dtype=tuple(int))

        for i in range(h):
            for j in range(w):
                r, g, b = image.getpixel((i, j))
                avg = (r+g+b) // 3
                output[i, j] = (avg, avg, avg)
                
        return output