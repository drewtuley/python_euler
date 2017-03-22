#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrew.tuley"
__date__ = "$20-Jul-2015 09:17:44$"


def method1():
    sum = 0
    threes = 3
    fives = 5
    while threes < 1000 or fives < 1000:
        if threes < fives:
            sum += threes
            threes += 3
        elif threes == fives:
            sum += threes
            threes += 3
            fives += 5
        else:
            sum += fives
            fives += 5
            # print 'threes={0} fives={1} sum={2}'.format(threes, fives, sum)
    print sum


def method2():
    sum = 0
    x = 3
    while x < 1000:
        if x % 3 == 0 or x % 5 == 0:
            sum += x
        x += 1

    print sum


def method3():
    gaps = [2, 1, 3, 1, 2, 3, 3]
    sum = 3
    x = 3
    idx = 0
    while x + gaps[idx] < 1000:
        x += gaps[idx]
        # print x
        sum += x
        idx += 1
        if idx > 6:
            idx = 0

    print sum


if __name__ == "__main__":
    import timeit

    print (timeit.timeit("method1()", setup="from __main__ import method1", number=1))
    print (timeit.timeit("method2()", setup="from __main__ import method2", number=1))
    print (timeit.timeit("method3()", setup="from __main__ import method3", number=1))
