# Cost 함수의 모양을 보자
# Convex 형태일 경우에 Decent 함수ㄹ르 이용해서 Global minimaze를 찾을 수 있다

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
# reduce_sum  : 수식 뒤에 m 으로 나누는 부분이 빠져있어서 sum만 함
cost = tf.reduce_sum(tf.pow(hyporthesis-y, 2))/(m)

# 변수 초기화
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

# W값 변경해가면서 값을 plot에 출력
for i in range(-30, 50):
    # W 값 : -3 ~ 5 사이의 값을 입력
    print(i*0.1, sess.run(cost, feed_dict={W:i*0.1}))

    # plot data
    x_data.append(i*0.1)
    y_data.append(sess.run(cost, feed_dict={W:i*0.1}))

# plot 출력
pt.plot(x_data, y_data, 'ro')
pt.xlabel('W')
pt.ylabel('Cost')
pt.show()

