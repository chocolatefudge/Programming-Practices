'''
2019/11/21
From https://github.com/hunkim/DeepLearningZeroToAll/

Logistic Classification with using TensorFlow.
Same with lab5_1 with using another data from file. 
'''

import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
import numpy as np
import math
tf.disable_v2_behavior()

data = np.loadtxt('../data/data-03-diabetes.csv', delimiter = ',', dtype = np.float32)

#Data sets provided
x_data = data[:,0:-1]
y_data = data[:,[-1]]

length = len(x_data[0])

X = tf.placeholder(tf.float32, shape=[None, length])
Y = tf.placeholder(tf.float32, shape = [None, 1])

W = tf.Variable(tf.random_normal([length,1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name = "bias")

#Sigmoid y = 1/(1+exp(-x)) used to fit values between 0 and 1.
hypothesis = tf.sigmoid(tf.matmul(X, W)+b)

#Cost function is designed to compare values when y=1 or y=0.
cost = tf.reduce_mean(-Y*tf.log(hypothesis)-(1-Y)*tf.log(1-hypothesis))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

#These variables are for testing the result.
#Accuracy checks whether our model has successfully classified given data by comparing it to each y.
predicted = tf.cast(hypothesis>0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(200000):
    cost_val, _= sess.run([cost, train], feed_dict={X:x_data, Y:y_data})
    if step%10000==0:
        print("Step: ", step, "Cost: ", cost_val)

h, p, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:x_data, Y:y_data})
print("\nHypothesis: ", h, "\nPredicted: ", p, "\nAccuracy: ", a)
