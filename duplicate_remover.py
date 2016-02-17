#!/usr/bin/env python

import os
from PIL import Image
from random import randint

'''
1. Open first image
2. Get image dimensions (in px) of first image
3. Generate 10 random points within dimensions of first image
4. Get r,g,b values at those 10 random points
'''
# 1. open first image
first_image = \
    Image.open('/Users/shua387/Desktop/test_folder/test_image.jpg')

# 2. get image dimensions
width_first, height_first = first_image.size

first_image_points = []

# 3. generate N (= 10) random points within the image
for i in range(1, 11):
    # generate a random point dimension within image
    rand_width_pixel = randint(0, width_first)
    rand_height_pixel = randint(0, height_first)

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
    Image.open('/Users/shua387/Desktop/test_folder/test_image_copy.jpg')

# 6. Get/check dimensions
width_second, height_second = second_image.size

second_rgb_values = []

if width_second == width_first and height_second == height_first:
    # get r,g,b values at generated points and store in list
    for point in first_image_points:
        second_rgb_values.append(second_image.getpixel(point))

# 8. check to see if r,g,b values match between images
for i in range(1, 10):
    if first_rgb_values[i] == second_rgb_values[i]:
        # 9. Remove second image
        os.remove('/Users/shua387/Desktop/test_folder/test_image_copy.jpg')

first_image.close()
second_image.close()
