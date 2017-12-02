import tensorflow as tf


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')


x = tf.constant([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3,
                 4, 4, 4, 4.0], shape=(1, 4, 4, 1))
W = tf.constant([1, 1, 1, 1, 2, 2, 2, 2.0], shape=(2, 2, 1, 2))
h_conv1 = conv2d(x, W)  # shape (1,4,4,2)

b = tf.constant([1, 2], dtype="float")

with tf.Session() as sess:
    sess.run(h_conv1)
