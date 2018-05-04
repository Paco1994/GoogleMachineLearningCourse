### Exercise #1: Reshape two tensors in order to multiply them.

# The following two vectors are incompatible for matrix multiplication:

#   *  `a = tf.constant([5, 3, 2, 7, 1, 4])`
#   *  `b = tf.constant([4, 6, 3])`

# Reshape these vectors into compatible operands for matrix multiplication.
# Then, invoke a matrix multiplication operation on the reshaped tensors.

import tensorflow as tf



with tf.Graph().as_default():
  a = tf.constant([5, 3, 2, 7, 1, 4])
  b = tf.constant([4, 6, 3])

  # Reshape the [6] vector into a 2-D 2x3 tensor.
  reshaped_2x3_tensor = tf.reshape(a, [2,3])

  # Reshape the [3] vector into a 2-D 3x1 tensor.
  reshaped_3x1_tensor = tf.reshape(b, [3,1])

  # Reshape the 8x2 matrix into a 3-D 2x2x4 tensor.
  axb_tensor = tf.matmul(reshaped_2x3_tensor, reshaped_3x1_tensor)
  

  with tf.Session() as sess:
    print ("Original vector(a)[6]:")
    print (a.eval())
    print ("Original vector(b)[3]:")
    print(b.eval())
    print ("Reshaped a to 2-D tensor (2x3):")
    print (reshaped_2x3_tensor.eval())
    print ("Reshaped b to 2-D tensor (3x1):")
    print (reshaped_3x1_tensor.eval())
    print ("2-D tensor multiplied:")
    print (axb_tensor.eval())