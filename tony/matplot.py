import matplotlib.pyplot as plt

def line():
    xs = [1, 2, 3, 4, 5]
    ys = [1, 2, 3, 4, 5]

    plt.plot(xs, ys)
    plt.show()



def Spot():
    xs = [1, 2, 3, 4, 5]
    ys = [1, 2, 3, 4, 5]

    # 파란점을 찍는다
    plt.plot(xs, ys, 'o')
    plt.show()

def redSpot():
    xs = [1, 2, 3, 4, 5]
    ys = [1, 2, 3, 4, 5]

    # 파란점을 찍는다
    plt.plot(xs, ys, 'ro')
    plt.show()


def redSpotLim():
    xs = [1, 2, 3, 4, 5]
    ys = [1, 2, 3, 4, 5]

    plt.plot(xs, ys, 'ro')
    plt.xlim(-10, 16)
    plt.ylim(0, 16)
    plt.show()

def Lim():
    xs = [1, 2, 3, 4, 5]
    ys = [1, 2, 3, 4, 5]

    plt.plot(xs, ys, 'ro')
    plt.xlim(0, 6)
    plt.ylim(0.9, 6)
    plt.show()


def Label():
    xs = [1, 2, 3, 4, 5]
    ys = [1, 2, 3, 4, 5]

    plt.plot(xs, ys, 'ro')
    plt.xlim(0, 6)
    plt.ylim(0.1, 6)
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.show()


def Test():

    xs = [1, 2, 3, 4, 5]
    ys = [1, 2, 3, 4, 5]

    plt.plot()
#line()
#Spot()
#redSpot()
#redSpotLim()
#Lim()
Label()
