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
import mnist

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

        output = np.zeros((h, w), dtype=np.uint8)

        for i in range(h):
            for j in range(w):
                r,g,b = image.getpixel((j,i))
                output[i, j] = self.average_pixel(r,g,b)

        return output
    
    def average_pixel(self, r, g, b):
        return (r+g+b) / 3
class Conv:
    '''Class to add customizable convulution layers i.e. 3x3, 5x5 and so on'''

    def __init__(self, size, num_filters, padding = 0, variance = 9):

        self.size = size
        self.num_filters = num_filters
        self.padding = padding
        self.filters = np.random.randn(num_filters, size, size) / variance

    def pad_image(self, image):

        image = image.convert("RGB")
        
        greyscale = Greyscaler()
        w, h = image.size

        padding = self.padding

        new_w = w+(padding*2)
        new_h = h+(padding*2)

        output = np.zeros((new_h, new_w), dtype =np.uint8)

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
                    output[i,j] = greyscale.average_pixel(r,g,b)
        return output

    def iterate_regions(self, image):
        '''Generates all size x size image regions using the padded image if wanted.'''

        w, h = image.shape

        offset = (self.size // 2) * 2 
        size = self.size

        for i in range(h-offset):
            for j in range(w-offset):
                im_region = image[i: (i+size), j:(j+size)]
                yield im_region, i, j
    
    def forward(self, input):
        greyscale = Greyscaler()
        if self.padding == 0:
            imgr = greyscale.average(input)
            w, h = input.size
            output = np.zeros((h, w, self.num_filters))
        else:
            imgr = self.pad_image(input)
            w, h = input.size
            offset = (self.size // 2) * 2 
            output = np.zeros((h-offset, w-offset, self.num_filters))

        for im_region, i, j in self.iterate_regions(imgr):
            print(im_region)
            output[i,j] = np.sum(im_region * self.filters, axis=(1,2))

        return output
    
#train_images = Image.fromarray(mnist.train_images())
#train_labels = mnist.train_labels()

im = Image.open("Testimage.png")
conv = Conv(3, 8) 
output = conv.forward(im)
print(output.shape)