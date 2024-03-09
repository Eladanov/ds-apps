import argparse
from collections import defaultdict, Counter
import cv2
from fuzzywuzzy import fuzz
from itertools import combinations # not mandatory
import imutils
from imutils import build_montages, paths
import os
import matplotlib.pyplot as plt
import networkx as nx
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import re
import seaborn as sns

from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import OneHotEncoder
import string

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer
from sklearn.base import BaseEstimator, TransformerMixin
import xgboost
from xgboost import cv, XGBClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
from tensorflow.keras.models import load_model


train_data_dir = 'images/train'
image_dir = 'images/train'
image_size = (128, 128)

train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2
)

test_datagen = ImageDataGenerator(rescale=1.0/255.0)


train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=image_size,
    batch_size=32,
    class_mode='categorical',
    subset='training'
)


validation_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=image_size,
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(image_size[0], image_size[1], 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.2),
    Dense(6, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

num_epochs = 10
model.fit(train_generator, epochs=num_epochs, validation_data=validation_generator)

test_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=image_size,
    batch_size=32,
    class_mode='categorical',
    subset='validation'
)

eval_result = model.evaluate(test_generator)
print("Test Loss:", eval_result[0])
print("Test Accuracy:", eval_result[1])

model.save('cnn_model.h5')

model = load_model('cnn_model.h5')
result = dict()
base = {'cakes_cupcakes_snack_cakes_score': 0,
        'candy_score': 1,
        'chips_pretzels_snacks_score': 2,
        'chocolate_score': 3,
        'cookies_biscuits_score': 4,
        'popcorn_peanuts_seeds_related_snacks_score': 5}
        
main_folder_path = "images/test"


photos = os.listdir(main_folder_path)

for photo in photos:
    photo_name = os.path.splitext(photo)[0]
    photo_path = os.path.join(main_folder_path, photo)
    try:
        image = tf.keras.preprocessing.image.load_img(photo_path, target_size=image_size)
        image_array = tf.keras.preprocessing.image.img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0) / 255.0
        probs = model.predict(image_array)[0]
    except:
        continue
    base['cakes_cupcakes_snack_cakes_score'] = probs[0]
    base['candy_score'] = probs[1]
    base['chips_pretzels_snacks_score'] = probs[2]
    base['chocolate_score'] = probs[3]
    base['cookies_biscuits_score'] = probs[4]
    base['popcorn_peanuts_seeds_related_snacks_score'] = probs[5]
    result[photo_name] = base
            
photos_probs = pd.DataFrame.from_dict(result, orient='index')
photos_probs.to_csv('photos_test_probs.csv',index_label='idx')
