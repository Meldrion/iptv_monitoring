#!/usr/bin/python

import io
from PIL import Image
import picamera
import time


def analyse_images(image01,image02):
    pixel_tuple = (0,0)
    pixel01 = image01.getpixel(pixel_tuple)
    pixel02 = image02.getpixel(pixel_tuple)
    print("Image01: {} and Image02: {}".format(pixel01,pixel02))

image01 = None
image02 = None

switch_flag = False

MAX_IMAGES = 2
counter = 0

camera = picamera.PiCamera()
camera.resolution = (1024, 768)


while True:
    if not switch_flag:
        stream01 = io.BytesIO()
        camera.capture(stream01, format='jpeg')
        stream01.seek(0)        
        image01 = Image.open(stream01)
    else:
        stream02 = io.BytesIO()
        camera.capture(stream02, format='jpeg')
        stream02.seek(0)              
        image02 = Image.open(stream02)
    
    if image01 is not None and image02 is not None:
        analyse_images(image01,image02)
    
    time.sleep(0.5)
    switch_flag = not switch_flag

