__author__ = 'dima'

import sys


def tir(mega_ball, dropd):
    out_mega_ball = {number: number == mega_ball for number in range(10)}
    out_balls = {number: number in dropd for number in range(1, 43)}
    return out_mega_ball, out_balls


def main(in_balls):
    print(tir(int(in_balls[0]), [int(x) for x in in_balls[1:]]))

if __name__ == '__main__' and len(sys.argv) > 1:
    main(sys.argv[1:])
