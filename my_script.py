__author__ = 'dima'

import sys


def tir(mega_ball, dropd):
    out_mega_ball = {number: number == mega_ball for number in range(10)}
    out_balls = {number: number in dropd for number in range(1, 43)}
    return out_mega_ball, out_balls


def main(in_balls):
    mg = int(in_balls[0])
    balls = [int(x) for x in in_balls[1:]]
    a, b = tir(mg, balls)
    print(a)
    print(b)

if __name__ == '__main__' and len(sys.argv) > 1:
    main(sys.argv[1:])
