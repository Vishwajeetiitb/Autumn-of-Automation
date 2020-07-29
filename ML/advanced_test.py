import tensorflow as tf
logits = [[4.0, 2.0, 1.0], [0.0, 5.0, 1.0]]
labels = [[1.0, 0.0, 0.0], [0.0, 0.8, 0.2]]
a = tf.nn.softmax(logits=logits)
print(a)