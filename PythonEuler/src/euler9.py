#! /usr/bin/python
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrew.tuley"
__date__ = "$21-Jul-2015 10:19:28$"


def generator():
    a = 1
    while a < 1000:
        b = a
        while b < 1000:
            c = b
            while c <= 1000 - (a + b):
                if a + b + c == 1000:
                    yield a, b, c
                c += 1
            b += 1
        a += 1


if __name__ == "__main__":
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc
    """

for a, b, c in generator():
    if a ** 2 + b ** 2 == c ** 2:
        print 'a={0},b={1},c={2} a*b*c={3}'.format(a, b, c, a * b * c)
        break
