#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:32:32 2019

@author: sakbarian
"""

import keras

if __name__ == '__main__':
  #InceptionResNetV2
  model=keras.applications.inception_resnet_v2.InceptionResNetV2(include_top=True, weights='imagenet', input_tensor=None, input_shape=None, pooling=None, classes=1000)
  model.save_weights("./InceptionResNetV2_weights.h5")
  print("Model is saved")
