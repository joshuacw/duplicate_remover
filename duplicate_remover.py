#!/usr/bin/env python

import shutil
from PIL import Image
from random import randint
from decimal import Decimal, getcontext
getcontext().prec = 3

'''
1. Open first image
2. Get image dimensions (in px) of first image
3. Generate 10 random points within dimensions of first image
4. Get r,g,b values at those 10 random points
'''
# 1. open first image
first_image = \
    Image.open('/Users/shua387/Desktop/test_folder/test_image_rect.jpg')

# 2. get first image dimensions
width_first, height_first = first_image.size

first_image_points = []

# 3. generate N (= 10,000) random points within the image
for i in range(1, 10001):
    # generate a random point dimension within image
    rand_width_pixel = randint(0, width_first - 1) 
    # script doesn't like right edge of pixels for some reason
    rand_height_pixel = randint(0, height_first - 1) 
    # nor the bottom edge

    first_image_points.append((rand_width_pixel, rand_height_pixel))

first_rgb_values = []

# 4. get r,g,b values at generated random points and store in list
for point in first_image_points:
    # get r,g,b values at random pixel dimension
    first_rgb_values.append(first_image.getpixel(point)) 
            

'''
5. Open second image
6. Check if same dimensions as first image
7. Get r,g,b values at points generated above
8. Check to see if the r,g,b values match those of first image
9. Remove image from library
'''

# 5. open second image
second_image = \
    Image.open(\
    '/Users/shua387/Desktop/test_folder/test_image_rect_sm.jpg')

# 6. Get/check dimensions of second image
width_second, height_second = second_image.size

second_image_points = []

def n_times_tuple(n, tup):
    return tuple([n*i for i in tup])

# 7. get points at "proportionalized" points
for point in first_image_points:
    second_image_points.append(n_times_tuple((float(width_second) / float(width_first)), point))

second_rgb_values = []

if width_second == width_first and height_second == height_first:
    # get r,g,b values at generated points and store in list
    for point in first_image_points:
        second_rgb_values.append(second_image.getpixel(point))
elif height_second / int(width_second) == height_first / int(width_first): 
    # get r,g,b values at generated points and store in list
    for point in second_image_points:
        second_rgb_values.append(second_image.getpixel(point))

# 8. check to see if r,g,b values (mostly) match between images
def identical_rgb(rgb_values1, rgb_values2):
    counter = 0
    for i in range(len(rgb_values1)):
        if rgb_values1[i] == rgb_values2[i]:
            counter += 1 
    return counter

# 9. remove second image if identical
if identical_rgb(first_rgb_values, second_rgb_values) >= 9250:
    shutil.move(\
    '/Users/shua387/Desktop/test_folder/test_image_rect_sm.jpg',\
    '/Users/shua387/.Trash')

first_image.close()
second_image.close()
