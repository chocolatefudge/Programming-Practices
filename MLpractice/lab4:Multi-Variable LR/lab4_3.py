'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

Loading data from .csv file using numpy
Same as lab 4_2 in other progress.
'''

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import numpy as np 

data = np.loadtxt('../data/data-01-test-score.csv', delimiter = ',', dtype = np.float32)
x_data = data[:,0:-1]
y_data = data[:, [-1]]

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

for step in range(2000):
	cost_val, h_val, _ = sess.run([cost, hypothesis, train], feed_dict = {X:x_data, Y:y_data})
	if step%20==0:
		print(step, "Cost: ", cost_val, "Hypothesis: ", h_val)


print("My scores 70, 80, 90 -> ", sess.run([hypothesis], feed_dict = {X:[[70, 80, 90]]}))