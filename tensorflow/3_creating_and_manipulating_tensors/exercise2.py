#
# Exercise #2: Simulate 10 rolls of two dice.
#

# Create a dice simulation, which generates a 10x3 2-D tensor in which:

# Columns 1 and 2 each hold one throw of one six-sided die (with values 1–6).
# Column 3 holds the sum of Columns 1 and 2 on the same row.
# For example, the first row might have the following values:

# Column 1 holds 4
# Column 2 holds 3
# Column 3 holds 7
# You'll need to explore the TensorFlow documentation (https://www.tensorflow.org/api_guides/python/array_ops) to solve this task.

import tensorflow as tf

g = tf.Graph()

with g.as_default():
  dices = tf.Variable(tf.random_uniform([10, 2], minval=1, maxval=7, dtype=tf.int32))
  
  dices_sum = tf.reduce_sum(dices, axis=1, keepdims=True) # The second parameter axis=1 reduces 1 the dimension of the 2-D Tensor to get the sum
  tensor_10x3_2D = tf.concat(axis=1, values=[dices, dices_sum])


  with tf.Session() as sess:
    initialization = tf.global_variables_initializer()
    sess.run(initialization)
    print(tensor_10x3_2D.eval())