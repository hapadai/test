import tensorflow as tf
import matplotlib.pyplot as pt

def plotData(x, y):
    x_result.append(x)
    x_result.append(y)

def plotShow():
    pt.plot(x_result, y_result, 'ro')
    pt.show()

x_data = [1.0, 2.0, 3.0]
y_data = [1.0, 2.0, 3.0]

x_result = []
y_result = []

# W, b 값을 random 시작
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.random_uniform([1], -1.0, 1.0))

# X, Y 값 placeholder
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# My hypothesis
hypothesis = tf.mul(W, X) + b

# cost
cost = tf.reduce_mean(tf.square(hypothesis - Y))

# Minimize :
a = tf.Variable(0.1)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)

# 모든 변수 초기화
init = tf.initialize_all_variables()

# Launch the graph
sess = tf.Session()
sess.run(init)

# Learning : Fit the line - tensorflow liner regression
for step in range(1000):
    sess.run(train, feed_dict={X:x_data, Y:y_data})
    print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run(W), sess.run(b))

    x_result.append(sess.run(W))
    y_result.append(sess.run(b))

plotShow()

print (sess.run(hypothesis, feed_dict={X:5}))
print (sess.run(hypothesis, feed_dict={X:3.5}))

