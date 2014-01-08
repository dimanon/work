__author__ = 'dima'

import sys


def tir(mega_ball, dropd):
    mega_ball = {number: number == mega_ball for number in range(10)}
    six_of_42 = {number: number in dropd for number in range(1, 43)}
    return mega_ball, six_of_42


def main(balls):
    print(tir(int(balls.pop(0)), [int(ball) for ball in balls]))

if __name__ == '__main__' and len(sys.argv) > 1:
    main(sys.argv[1:])
