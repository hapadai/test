import tensorflow as tf

X = [1.0, 2.0, 3.0]
Y = [1.0, 2.0, 3.0]

W = tf.Variable(0.)

hyporthesis = W * X

cost = tf.reduce_mean( tf.square(hyporthesis - Y) )

optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

wOp = W.assign(-3.0)
sess.run(wOp)

for step in range(10):
    print(step, sess.run(cost), sess.run(W))
    sess.run(train)

#print(step, sess.run(W))
