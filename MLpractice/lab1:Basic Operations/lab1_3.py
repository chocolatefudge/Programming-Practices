'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

Instead of assigning a value to node(tensor) first, 
first declare a placeholder. 
While running a session, assign values to each placeholder. 
'''

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

node1 = tf.placeholder(tf.float32)
node2 = tf.placeholder(tf.float32)
node3 = node1+node2

sess = tf.Session()

print(sess.run(node3, feed_dict={node1:3, node2:4}))
print(sess.run(node3, feed_dict={node1:[3,4,5], node2:[4,5,6]}))
