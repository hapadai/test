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

# Minimize
# cost function을 GradientDescentOptimizer을 써서 train한다는 것은
# W 값을 임의로 정하고 x, y Data을 넣어서 계산해서 cost을 계산한다
# 실제로는 W, cost 2차 방정식에서 특정 값에서의 기울기를 정해서 W의 이동 크기를 자동으로 계산한다
# y = y - 기울기

a = tf.Variable(0.1)  # Laring rate, alpha
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

# Brfore starting, initialize the variables
init = tf.initialize_all_variables()

# Launach the graph.
sess = tf.Session()
sess.run(init)

# Fit the liner Line
for step in range(10):
	sess.run(train)
	#if step % 20 == 0:

	print (step, sess.run(cost), sess.run(W), sess.run(b), sess.run(hyporthesis))

	x_result.append(sess.run(W))
	y_result.append(sess.run(b))


pt.plot(x_result, y_result, 'ro')
pt.show()

#print(x_result)

#for setp1 in range(1001):

    #pt.plot(x_result, y_result)
    #pt.show()