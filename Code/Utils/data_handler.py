#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@author: gowrisankar
@date: 19/04/2022
'''

import os
import cv2
import logging
import matplotlib.pyplot as plt

Data_Path = os.path.join('./../Data')

def load_images(data_dir, Data_Path = Data_Path):
    image_array = []
    for img in sorted(os.listdir(os.path.join(Data_Path, data_dir))):
        img = os.path.join(Data_Path, data_dir, img)
        logging.info("Reading Image: {0}".format(img))
        print("Reading Image: {0}".format(img))
        
        img = cv2.imread(img)
        image_array.append(img)

    return image_array

def play_images(image_array):
    for img in image_array:
        #b,g,r = cv2.split(img) # Changing the order from bgr to rgb so that matplotlib can show it
        #img = cv2.merge([r,g,b])
        cv2.imshow('Frames', img)
        cv2.waitKey(1)

def test_play_images(data_dir = None):
    data_dir = 'sample_Stereo_conveyor_without_occlusions/left'
    play_images(load_images(data_dir))    
    data_dir = 'sample_Stereo_conveyor_without_occlusions/right'
    play_images(load_images(data_dir))    

    return

if __name__ == '__main__':
    test_play_images()