'''
2019/11/21
From https://github.com/hunkim/DeepLearningZeroToAll/

Basic Softmax Classification in Tensorflow.
Unlike simple logistic classification, there can be variaty of y values(standards) to fit in.
In this case, we use softmax method to fit in the hypothesis values and evaluate cost function.
'''

import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
import numpy as np
import math
tf.disable_v2_behavior()

x_data = [[1, 2, 1, 1],
          [2, 1, 3, 2],
          [3, 1, 3, 4],
          [4, 1, 5, 5],
          [1, 7, 5, 5],
          [1, 2, 5, 6],
          [1, 6, 6, 6],
          [1, 7, 7, 7]]
y_data = [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 1, 0],
          [0, 1, 0],
          [0, 1, 0],
          [1, 0, 0],
          [1, 0, 0]]

X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape = [None, 3])

W = tf.Variable(tf.random_normal([4, 3]), name="weight")
b = tf.Variable(tf.random_normal([3]), name = "bias")

#Used softmax method in TensorFlow
hypothesis = tf.nn.softmax(tf.matmul(X, W)+b)

#Cost function is sum of -ylog(H(x)).
cost = tf.reduce_mean(-tf.reduce_sum(Y*tf.log(hypothesis), axis=1))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2000):
    sess.run([train], feed_dict={X:x_data, Y:y_data})
    if step%20==0:
        print(step, sess.run([cost], feed_dict={X:x_data, Y:y_data}))

#Checking which argument is maximum in given input data. 
a = sess.run(hypothesis, feed_dict={X:[[1,100,7,8]]})
print(a, sess.run(tf.arg_max(a,1)))
