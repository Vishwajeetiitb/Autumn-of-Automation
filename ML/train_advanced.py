# %% [code]
import tensorflow as tf
import pandas as pd
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense,Dropout,Activation,Flatten,Conv2D,MaxPool2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# %% [code]
path = os.path.join("Advanced_Assignment_Dataset/")
training_data = []
training_data2 = []
for img in os.listdir(path):
    img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
    a1 = "up" in str(img)
    a2= "left" in str(img)
    a3 = "right" in str(img)
    a4 = "straight" in str(img)
    b1 = "neutral" in str(img)
    b2 = "sad" in str(img)
    b3 = "happy" in str(img)
    b4 = "angry" in str(img)
    c1 = "open" in str(img)
    c2 = "sunglasses" in str(img)
    class_num = np.array([a1*1 ,a2*1 ,a3*1, a4*1])
    class_num2 = np.array([c1*1,c2*1])
    training_data.append([img_array ,class_num]) 
    training_data2.append([img_array ,class_num2]) 
    

# %% [code]


X = []
Y = []
for feature, label in training_data:
#     print(feature.shape)
    X.append(feature)
    Y.append(label)

X = np.array(X).reshape(-1, 120, 128, 1)
y = np.array(Y)
X = X/255.0
# print(X.shape)
model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(len(class_num)))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(X, y, batch_size=32, epochs=20, validation_split=0.3)

# %% [code]

X = []
Y = []
for feature, label in training_data2:
#     print(feature.shape)
    X.append(feature)
    Y.append(label)

X = np.array(X).reshape(-1, 120, 128, 1)
y = np.array(Y)
X = X/255.0
model2 = Sequential()

model2.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model2.add(Activation('relu'))
model2.add(MaxPooling2D(pool_size=(2, 2)))

model2.add(Conv2D(256, (3, 3)))
model2.add(Activation('relu'))
model2.add(MaxPooling2D(pool_size=(2, 2)))

model2.add(Conv2D(256, (3, 3)))
model2.add(Activation('relu'))
model2.add(MaxPooling2D(pool_size=(2, 2)))


model2.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model2.add(Dense(64))

model2.add(Dense(len(class_num2)))
model2.add(Activation('sigmoid'))

model2.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model2.fit(X, y, batch_size=32, epochs=20, validation_split=0.3)

# %% [code]

# %% [code]
