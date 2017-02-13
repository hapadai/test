import tensorflow as tf
import matplotlib.pyplot as pt

# x, y 선언
x = [1., 2., 3.]
y = [1., 2., 3.]
m = n_samles = len(x)

# plot x, y 선언
x_data = []
y_data = []

# W 선언
W = tf.placeholder(tf.float32)

# My hyporthesis : y = Wx
hyporthesis = tf.mul(W, x)

# cost function
cost = tf.reduce_mean(tf.pow(hyporthesis-y, 2))/(m)

# 변수 초기화
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# W값 변경해가면서 값을 plot에 출력
for i in range(-30, 50):
    print(i*0.1, sess.run(cost, feed_dict={W:i*0.1}))
    x_data.append(i*0.1)
    y_data.append(sess.run(cost, feed_dict={W:i*0.1}))

# plot 출력
pt.plot(x_data, y_data, 'ro')
pt.xlabel('W')
pt.ylabel('Cost')
pt.show()

