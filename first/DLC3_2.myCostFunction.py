import tensorflow as tf

x_data = [1.0, 2.0, 3.0 ]
y_data = [1.0, 2.0, 3.0 ]

# W, x, y 설정
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

hyporthesis = W * X

cost =  tf.reduce_mean( tf.square(hyporthesis - Y) )

# minimize
decent = W - tf.mul(0.1, tf.reduce_mean(tf.mul((tf.mul(W,X) - Y), X)))
update = W.assign(decent)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for step in range(20):
    sess.run(update, feed_dict={X:x_data, Y:y_data})
    print (step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W))

