import tensorflow as tf
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

# model.load_weights("intermediate_checkpoint/")
model = tf.keras.models.load_model("model.h5")
img = cv2.imread("test_glass1.jpg",cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(128,120))
a  = np.array(img,).reshape(-1, 120, 128, 1)
plt.imshow(img,cmap='gray')
is_sunglass = model.predict(a)[0][0]
print(is_sunglass)
if is_sunglass < 0.5:
	text = " not present"
else:
	text = " present"
plt.title("Sunglass"+text)
plt.show()
