# Decent 알고리즘을 직접 구현한다

import tensorflow as tf
import matplotlib.pyplot as pt

x_data = [1., 2., 3.]
y_data = [1., 2., 3.]

m = len(x_data)

x_plot = []
y_plot = []

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W = tf.Variable(tf.random_uniform([1], -10, 10))

# My hyporthesis
hyporthesis = W * X

# cost
cost = tf.reduce_mean( tf.pow((hyporthesis-Y), 2) )

# Decent 알고리즘
# decent = W - 기울기
a = tf.Variable(0.1)
decent = W -  tf.mul(a, tf.reduce_mean( tf.mul((hyporthesis-Y), X) ) )
update = W.assign(decent)

# session
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# run
for step in range(200):
    sess.run(update, feed_dict={X:x_data, Y:y_data})
    print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W))

