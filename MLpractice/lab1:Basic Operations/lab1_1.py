'''
2019/11/18
From https://github.com/hunkim/DeepLearningZeroToAll/

Importing the tensorflow package
declaring a constant
opening a session
running a session
'''


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

hello = tf.constant("Hello, Tensorflow!")
sess = tf.Session()

print(sess.run(hello))