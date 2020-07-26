# %% [code]
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
import pandas as pd
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt



# %% [code]
data_dir = "Intermediate_Assignment_Dataset/"
path = os.path.join(data_dir)
training_data = []
for img in os.listdir(path):
    img_array = cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
    if "Yes" in str(img):
        class_num = 1
    else:
        class_num = 0
    training_data.append([img_array ,class_num])
   
    

# %% [code]
X = []
Y = []
for feature, label in training_data:
#     print(feature.shape)
    X.append(feature)
    Y.append(label)

X = np.array(X).reshape(-1, 120, 128, 1)
y = np.array(Y)

# %% [code]


X = X/255.0

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


# %% [code]
model.fit(X, y, batch_size=32, epochs=10, validation_split=0.3)

# %% [code]
model.save("model.h5")
