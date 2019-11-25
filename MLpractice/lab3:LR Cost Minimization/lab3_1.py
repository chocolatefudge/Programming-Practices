'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

To minimize the cost in linear regression, graph has to be in convex form.
By changing W values and plotting W-cost in 2-D, we can check if it's convex or not. 
'''
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

#values for X and Y
X = [1,2,3]
Y = [1,2,3]

#trainable variables
W = tf.placeholder(tf.float32)

#hypothesys and cost calculated by MSE
hypothesys = W*X
cost = tf.reduce_mean(tf.square(hypothesys - Y))

sess = tf.Session()
sess.run(tf.global_variables_initializer())

#Arrays for different W and cost values 
W_val = []
cost_val = []

#Assign different W for each step, calculate current W and cost values and save to array. 
for step in range(-30, 50):
	temp_W = step*0.1
	curr_W, curr_cost = sess.run([cost, W], feed_dict = {W:temp_W})
	W_val.append(curr_W)
	cost_val.append(curr_cost)

#Plot W and cost to graph and display. 
plt.plot(cost_val, W_val)
plt.show()
