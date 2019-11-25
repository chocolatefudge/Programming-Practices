'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

Multivariable Linear Regression in Tensorflow
Brute-Force method not using matrix. 
'''

import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#Write data as array type
x1_data = [73., 93., 89., 96., 73.]
x2_data = [80., 88., 91., 98., 66.]
x3_data = [75., 93., 90., 100., 70.]
y_data = [152., 185., 180., 196., 142.]

#Placeholders for data
x1 = tf.placeholder(tf.float32)
x2 = tf.placeholder(tf.float32)
x3 = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#Weight also consists of 3 variables.
w1 = tf.Variable(tf.random_normal([1]), name = 'weight1')
w2 = tf.Variable(tf.random_normal([1]), name = 'weight2')
w3 = tf.Variable(tf.random_normal([1]), name = 'weight3')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

#Calculate hypothesis based on weights and input data
hypothesis = x1*w1+x2*w2+x3*w3+b

#cost evaluation
cost = tf.reduce_mean(tf.square(hypothesis-Y))

#small learning rate 
#If high rate such as 0.01, cost diverges due to gradient value. 
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-5)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2000):
	cost_val, h_val, _ = sess.run([cost, hypothesis, train], feed_dict = {x1:x1_data, x2:x2_data, x3:x3_data, Y:y_data})
	if step%20==0:
		print(step, "Cost: ", cost_val, "Hypothesis: ", h_val)