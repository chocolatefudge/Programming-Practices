'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

Declaring a constant(float)
making node(tensor) as a sum of two other nodes.
Just printing a constant which results in printing a tensor. 
Running a session and getting a result. 
'''

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print("node1: ", node1)

sess = tf.Session()
print("sess.run([node1, node2]): ", sess.run([node1, node2]))
print("sess.run(node3): ", sess.run(node3))