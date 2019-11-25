'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

Multivariable Linear Regression in Tensorflow
Used Matrix method to easily manipulate multidimentional data. 
'''

import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
import numpy as np
tf.disable_v2_behavior()


x_data = [[73., 93., 89., 96., 73.], [80., 88., 91., 98., 66.], [75., 93., 90., 100., 70.]]
y_data = [[152.], [185.], [180.], [196.], [142.]]

X = tf.placeholder(tf.float32, shape = [None, 3])
Y = tf.placeholder(tf.float32, shape = [None, 1])

W = tf.Variable(tf.random_normal([3, 1]), name = 'weight1')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

hypothesis = tf.matmul(X, W)+b

cost = tf.reduce_mean(tf.square(hypothesis-Y))

#small learning rate 
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

#Matrix X has to be transposed since each row represents one set of x1, x2, x3. 
for step in range(2000):
	cost_val, h_val, _ = sess.run([cost, hypothesis, train], feed_dict = {X:np.transpose(x_data), Y:y_data})
	if step%20==0:
		print(step, "Cost: ", cost_val, "Hypothesis: ", h_val)