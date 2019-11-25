'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

For given train datas, process them for linear regression. 
Minimizing optimizer is used to minimize the cost value. 
After running for many steps, cost converges to 0 and W, b value is evaluated more precisely. 

'''

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#datas for x and y
x_train = [1,2,3]
y_train = [2,4,6]

#trainable variables
W = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

#hypothesys and cost calculated by MSE
hypothesys = W*x_train+b
cost = tf.reduce_mean(tf.square(hypothesys - y_train))

#optimize to minimize cost value
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

#open a session and initialize global variables. 
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#machine learning process for 30000 steps. check values for W and b in certain iterations
for step in range(30000):
	sess.run(train)
	if step%300==0:
		print(step, sess.run(cost), sess.run(W), sess.run(b))

