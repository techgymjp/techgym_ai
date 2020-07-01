# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:34:48 2019

@author: n.aoi
"""

import cv2
import numpy as np
from keras.utils import Sequence
from post_processing import pad_image

class SlidingWindowGenerator(Sequence):
    def __init__(self, img_path, image_size, window_size, stride, batch_size, transform=None):
        self.img_path = img_path
        self.image_size = image_size
        self.height, self.width = window_size
        self.stride = stride
        self.batch_size = batch_size
        self.transform = transform

        self.img = cv2.imread(self.img_path)
        assert self.img is not None
        
        self.img = self.img[:,:,::-1] # convert to RGB
        self.left_top_coordinates = [(x1, y1) for x1 in range(0, self.img.shape[1], self.stride) for y1 in range(0, self.img.shape[0], self.stride)]
    
    def __len__(self):
        return int(np.ceil(len(self.left_top_coordinates)/self.batch_size))
    
    def __getitem__(self, idx):
        left_top = self.left_top_coordinates[idx*self.batch_size:(idx+1)*self.batch_size]
        batch_x = np.array([self._preprocess(self.img[y1:y1+self.height, x1:x1+self.width, :]) for x1, y1 in left_top])
        
        return left_top, batch_x

    def _preprocess(self, img):
        preprocessed = pad_image(img, (self.height, self.width))
        preprocessed = cv2.resize(preprocessed, self.image_size[:-1])
        if self.transform is not None:
            preprocessed = self.transform[0](preprocessed)
        return preprocessed

if __name__ == '__main__':
    img_path = 'competition_data/val_images/test_05_1.jpg'
    image_size = (512,512,3)
    window_size = (300, 300)
    stride = 300
    batch_size = 32
    gen = SlidingWindowGenerator(img_path, image_size, window_size, stride, batch_size)
    for data in gen:
        print(data[1].shape)