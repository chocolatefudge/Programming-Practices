'''
2019/11/21
From https://github.com/hunkim/DeepLearningZeroToAll/

Fancy version of Softmax Classification in Tensorflow.
'''

import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
import numpy as np
import math
tf.disable_v2_behavior()

data = np.loadtxt('../data/data-04-zoo.csv', delimiter = ',', dtype = np.float32)

#Data sets provided
x_data = data[:,0:-1]
y_data = data[:,[-1]]

len_x = len(x_data[0])

classes = 7
#For each Y values, convert it to one_hot matrix
#ex, y=0 => [1000000]
X = tf.placeholder(tf.float32, shape=[None, len_x])
Y = tf.placeholder(tf.int32, shape = [None, 1])
Y_one_hot = tf.one_hot(Y, classes)
#shape becomes ?,7
Y_one_hot = tf.reshape(Y_one_hot, [-1, classes])

W = tf.Variable(tf.random_normal([len_x, classes]), name="weight")
b = tf.Variable(tf.random_normal([classes]), name = "bias")

hypothesis = tf.nn.softmax(tf.matmul(X, W)+b)

cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y_one_hot)
cost = tf.reduce_mean(cost_i)

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

prediction = tf.argmax(hypothesis, 1)
correct_prediction = tf.equal(prediction, tf.argmax(Y_one_hot, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(20000):
        sess.run(optimizer, feed_dict={X:x_data, Y:y_data})
        if step%100==0:
            cost_v, accu = sess.run([cost, accuracy], feed_dict={X:x_data, Y:y_data})
            print("Cost: ", cost_v, "Accuracy: ", accu)
