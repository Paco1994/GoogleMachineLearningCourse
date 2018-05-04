import tensorflow as tf

with tf.Graph().as_default():
  # Create an 8x2 matrix (2-D tensor).
  matrix = tf.constant([[1,2], [3,4], [5,6], [7,8],
                        [9,10], [11,12], [13, 14], [15,16]], dtype=tf.int32)

  # Reshape the 8x2 matrix into a 2x8 matrix.
  reshaped_2x8_matrix = tf.reshape(matrix, [2,8])
  
  # Reshape the 8x2 matrix into a 4x4 matrix
  reshaped_4x4_matrix = tf.reshape(matrix, [4,4])

  # Reshape the 8x2 matrix into a 1x16 matrix
  reshaped_1x16_matrix = tf.reshape(matrix, [1,16])

  with tf.Session() as sess:
    print ("Original matrix (8x2):")
    print (matrix.eval())
    print ("Reshaped matrix (2x8):")
    print (reshaped_2x8_matrix.eval())
    print ("Reshaped matrix (4x4):")
    print (reshaped_4x4_matrix.eval())
    print ("Reshaped matrix (1x16):")
    print (reshaped_1x16_matrix.eval())