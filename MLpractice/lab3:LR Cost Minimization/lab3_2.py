'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

Calculating gradient manually and applying it for linear regression.
Compute gradient by derivative of cost function. 
Apply gradient to new W value by substracting the gradient multiplied by learning rate. 
'''
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#values for X and Y
X = [1,2,3]
Y = [1,2,3]

#trainable variables
W = tf.Variable(tf.random_normal([1]), name = 'weight')

#hypothesys and cost calculated by MSE
hypothesys = W*X
cost = tf.reduce_mean(tf.square(hypothesys - Y))

#running session and initializing global variables
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#Assigning learning rates, gradient and descent values. 
learning_rate = 0.1
gradient = learning_rate*tf.reduce_mean((W*X-Y)*X)
descent = W - gradient

#updating W value
update = W.assign(descent)

#Iterating for 20 cycles
for i in range(20):
	sess.run(update)
	print(i, sess.run(cost), sess.run(W))
