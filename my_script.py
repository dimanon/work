__author__ = 'dima'


def tir(mega_ball, dropd):
    mega_ball = {number: number == mega_ball for number in range(10)}
    balls = {number: number in dropd for number in range(1, 43)}
    return mega_ball, balls

balls = [10, 21, 24, 31, 40, 42]
mg = 5
a, b = tir(mg, balls)
print(a)
print(b)
exit = ''
while exit != 'exit':
    mg = int(input("Input megaball: "))
    balls = [int(ball) for ball in input("Input balls , :").split(',')]
