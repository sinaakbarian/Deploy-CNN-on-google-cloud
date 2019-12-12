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
from model import *


#This is a pretrained model from https://keras.io/applications/

model,preprocess_input,decode_predictions,model_name=load()
print(model_name)

def pretrained_model_prediction(model,model_name,preprocess_input,decode_predictions,X,Y,img):
# read and prepare image
  img=imresize(img,(X,Y))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)

  preds = model.predict(x)
  results=decode_predictions(preds, top=5)[0]
  return results[0]

def create_blank(input,size,rgb_color=(255, 255, 255)):
    image = np.zeros((size, size, 3), np.uint8)
    random_width=random.randint(0,size-input.shape[1])
    random_height=random.randint(0,size-input.shape[0])
    
    color = tuple(reversed(rgb_color))
    image[:] = color
    image[random_height:random_height+input.shape[0],random_width:random_width+input.shape[1]]=input
    return image
    
app = Flask(__name__)

@app.route('/')
def index():
	
	return render_template("index.html")

@app.route('/wait/',methods=['GET','POST'])
def wait():
	
	if request.method == 'POST':
		if 'file' not in request.files:
		    return render_template("index.html")
		file = request.files['file']
		if file.filename == '':
			return render_template("index.html")
		else:
			print(file)
			filename = secure_filename(file.filename)
			in_memory_file = io.BytesIO()
			file.save(in_memory_file)
			input = np.asarray(Image.open(in_memory_file,mode='r').convert('RGB'))

			Result=pretrained_model_prediction(model,model_name,preprocess_input,decode_predictions,299,299,input)[1]
			
			return render_template("predict.html",result=str(Result))
if __name__ == '__main__':
    app.run()
