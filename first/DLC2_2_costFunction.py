import tensorflow as tf
import matplotlib.pyplot as pt

x_data = [1,2,3]
y_data = [1,2,3]

x_result = []
y_result = []

# Weight(가중치) 예상치
# -1 ~ 1 사이의 랜덤 값으로 제한
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

# my hyporthesis   h(x) = W * x + b : linear Regression
hyporthesis = W * x_data + b

# Cost function
cost = tf.reduce_mean(tf.square(hyporthesis - y_data))

#Minimize
a = tf.Variable(0.1)  # Learing rate, alpha
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

# Brfore starting, initialize the variables
init = tf.initialize_all_variables()

# Launach the graph.
sess = tf.Session()
sess.run(init)

# Fit the liner Line
for step in range(1001):
	sess.run(train)
	#if step % 20 == 0:

	print (step, sess.run(cost), sess.run(W), sess.run(b))

	x_result.append(sess.run(W))
	y_result.append(sess.run(b))


pt.plot(x_result, y_result, 'ro')
pt.show()

#print(x_result)

#for setp1 in range(1001):

    #pt.plot(x_result, y_result)
    #pt.show()