import tensorflow as tf
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

# model.load_weights("intermediate_checkpoint/")
positon_model = tf.keras.models.load_model("position_model.h5")
Sunglasses_model = tf.keras.models.load_model("sunglasses_model.h5")
img = cv2.imread("test_glass2.jpg",cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(128,120))
a  = np.array(img).reshape(-1, 120, 128, 1)
plt.imshow(img)
is_sunglass = Sunglasses_model.predict(a)[0][0]
print(is_sunglass)
if is_sunglass < 0.5:
	text = " not present"
else:
	text = " present"
positon = positon_model.predict(a)
print(positon)

plt.title("Sunglass"+text)
plt.show()
