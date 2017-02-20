# feature 가 여러 개인 데이터의 경우
# 변수가 여러 개인 경우에 처리하는 공식 : 공식에 변수가 하나 늘어난 느낌

import tensorflow as tf

x1_data = [1, 0, 3, 0, 5]
x2_data = [0, 2, 0, 4, 0]
y_data = [1,2,3,4,5]

w1 = tf.Variable( tf.random_uniform([1], -1.0, 1.0))
w2 = tf.Variable( tf.random_uniform([1], -1.0, 1.0))
b  = tf.Variable( tf.random_uniform([1], -1.0, 1.0))

hyporthesis = w1 * x1_data + w2 * x2_data + b

cost = tf.reduce_mean(tf.square( hyporthesis - y_data ))

optimizer = tf.train.GradientDescentOptimizer(0.1)
train = optimizer.minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(2000):
    print(step, sess.run(w1), sess.run(w2), sess.run(cost) )
    sess.run(train)

