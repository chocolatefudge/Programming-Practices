'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

Same version as lab2_1, but placeholder&feed method is used. 
This method has advantage when feeding different values at runtime, or checking purpose. 
'''

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

#trainable variables
W = tf.Variable(tf.random_normal([1]), name = 'weight')
b = tf.Variable(tf.random_normal([1]), name = 'bias')

#hypothesys and cost calculated by MSE
hypothesys = W*X+b
cost = tf.reduce_mean(tf.square(hypothesys - Y))

#optimize to minimize cost value
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

#Running with feeding variables to X and Y
for step in range(3000):
	cost_v, W_v, b_v, _ = sess.run([cost, W, b, train], feed_dict = {X:[1,2,3], Y:[3,4,5]})
	if step%30==0:
		print(step, cost_v, W_v, b_v)

#Test run
print(sess.run(hypothesys, feed_dict = {X:5}))