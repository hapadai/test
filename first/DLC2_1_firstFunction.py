import tensorflow as tf


def world():
	hello = tf.constant('Hello!, Tensor-Flow')
	hello1 = tf.constant('')

	sess = tf.Session()

	print(hello)  # Tensor("Const:0", shape=(), dtype=string)

	print()

	# 한글이 문제없이 될까요? 잘 되네요 () Python3에서는 필수입니다
	# run을 통해서만 실행이 된다
	print(sess.run(hello))


def operation():
	sess = tf.Session()

	a = tf.constant(2)
	b = tf.constant(3)

	c = a + b

	# Everything is operation!
	print (c)

	# Action은 run 을 통해서 실행
	print (sess.run(c))

def basicOperation():
	a = tf.constant(2)
	b = tf.constant(3)

	with tf.Session() as sess:
		print("a =2, b=3")
		print("Addition with constants: %i" % sess.run(a+b))
		print("Multiplication with constants: %i" % sess.run(a*b))


def placeholder():
	a = tf.placeholder(tf.int16)
	b = tf.placeholder(tf.int16)

	add = tf.add(a, b)
	mul = tf.mul(a, b)

	with tf.Session() as sess:
		print("Add %i" % sess.run(add, feed_dict={a:2, b:3}))
		print("Mul %i" % sess.run(mul, feed_dict={a:2, b:5}))

def TensorBoard():
	a = tf.placeholder(tf.int16)
	b = tf.placeholder(tf.int16)

	add = tf.add(a, b)
	mul = tf.mul(a, b)

	sess = tf.Session()
	print("Add %i" % sess.run(add, feed_dict={a: 2, b: 3}))
	print("Mul %i" % sess.run(mul, feed_dict={a: 2, b: 5}))

	# deprecated and will be removed after 2016-11-30.
	# Start: TensorBoard 그래프용 로그 기록
	tf.merge_all_summaries()
	tf.train.SummaryWriter("/Users/hapadai/Desktop/src/tensorflowlogs", sess.graph)
	# Finish: TensorBoard 그래프용 로그 기록

# world()

#operation()

#basicOperation()

#placeholder()

TensorBoard()


