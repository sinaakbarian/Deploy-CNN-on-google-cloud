#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:32:32 2019

@author: sakbarian
"""

from flask import Flask, render_template,request
from flask import Flask, flash, request, redirect, url_for
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import sys 
import os
import random
from PIL import Image
import io
from werkzeug.utils import secure_filename
global model, graph
import numpy as np
import keras.models
from keras.models import model_from_json
from scipy.misc import imread, imresize,imshow
import tensorflow as tf
from keras.preprocessing import image

def load():
#InceptionResNetV2
  with open('InceptionResNetV2_architecture.json', 'r') as f:
                  model = model_from_json(f.read())
  model.load_weights('InceptionResNetV2_weights.h5')
  preprocess_input=keras.applications.inception_resnet_v2.preprocess_input
  decode_predictions=keras.applications.inception_resnet_v2.decode_predictions
  model_name="InceptionResNetV2"
  
  return model,preprocess_input,decode_predictions,model_name
