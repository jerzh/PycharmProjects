from __future__ import division
import math
from graphics import *

s = 30
x_min = -10
y_min = -10
x_max = 10
y_max = 10
win = GraphWin("euler_method", s * (x_max - x_min), s * (y_max - y_min))


def f(x, y):
    return x + y


def scaled(x, y):
    return Point(s * (x - x_min), s * (y_max - y))


def calc_shift(length, x, y):
    slope = f(x, y)
    if slope != float("inf"):
        x_shift = length / math.sqrt(1 + slope ** 2)
        y_shift = slope * x_shift
    else:
        x_shift = 0
        y_shift = length
    return x_shift, y_shift


length_shift = 5.0 / s
step = 1
for j in xrange(y_min, y_max, step):
    for i in xrange(x_min, x_max, step):
        shift = calc_shift(length_shift, i, j)
        Line(scaled(i - shift[0], j - shift[1]), scaled(i + shift[0], j + shift[1])).draw(win)

x0 = 0
y0 = 1
length_shift = 2.0 / s
x1 = x0
y1 = y0
while x_min <= x1 <= x_max and y_min <= y1 <= y_max:
    scaled(x1, y1).draw(win)
    shift = calc_shift(length_shift, x1, y1)
    x1 -= shift[0]
    y1 -= shift[1]

x1 = x0
y1 = y0
while x_min <= x1 <= x_max and y_min <= y1 <= y_max:
    scaled(x1, y1).draw(win)
    shift = calc_shift(length_shift, x1, y1)
    x1 += shift[0]
    y1 += shift[1]

win.getMouse()
win.close()
