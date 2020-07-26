import tensorflow as tf
tf.compat.v1.disable_eager_execution()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

my_feature = ([1.0, 2.0,  3.0,  4.0,  5.0,  6.0,  7.0,  8.0,  9.0, 10.0, 11.0, 12.0])
my_label   = ([5.0, 8.8,  9.6, 14.2, 18.8, 19.5, 21.4, 26.8, 28.9, 32.0, 33.8, 38.2])

learning_rate=0.01
epochs=10
my_batch_size=12
plt.plot(my_feature,my_label,'o')
# plt.show()

X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)
W = tf.Variable(np.random.rand(),name = "weights")
B = tf.Variable(np.random.rand(),name = "bias")


#pred = W*X + B
pred = tf.add(tf.multiply(W,X),B)
cost = tf.reduce_mean((pred-Y)**2)
optimizer = tf.compat.v1.train.GradientDescentOptimizer(learning_rate).minimize(cost)
init = tf.compat.v1.global_variables_initializer()