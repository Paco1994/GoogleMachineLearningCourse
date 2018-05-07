import tensorflow as tf

g = tf.Graph()
with g.as_default():
  # Create a variable with the initial value 3.
  v = tf.Variable([3])

  # Create a variable of shape [1], with a random initial value,
  # sampled from a normal distribution with mean 1 and standard deviation 0.35.
  w = tf.Variable(tf.random_normal([1], mean=1.0, stddev=0.35))
  
  with tf.Session() as sess:
    initialization = tf.global_variables_initializer()
    sess.run(initialization)
    # Now, variables can be accessed normally, and have values assigned to them.
    print ("V --> {0}".format(v.eval()))
    print ("W --> {0}".format(w.eval()))

    assignment = tf.assign(v, [7])
    # The variable has not been changed yet!
    print ("V (Assign [Not runned]) --> {0}".format(v.eval()))

    # Execute the assignment op.
    sess.run(assignment)
    # Now the variable is updated.
    print ("V (Assign [Runned]) --> {0}".format(v.eval()))