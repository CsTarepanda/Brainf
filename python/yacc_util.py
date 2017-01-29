#!/usr/bin/python3
def to(p):
    p[0] = p[1]


# tmp
import itertools
count = itertools.count(1)
def this(p):
    p[0] = "T%d" % next(count)
    return p[0]


def print_expr(p):
    print("%s :(%s %s %s)" % (this(p), p[2], p[1], p[3]))


def unary_op(p):
    print("%s :(%s %s)" % (this(p), p[1], p[2]))
