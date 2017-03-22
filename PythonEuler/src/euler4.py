#! /usr/bin/python
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "andrew.tuley"
__date__ = "$20-Jul-2015 13:26:01$"


def is_palindrome(product):
    ret = True
    try:
        pro = str(product)
        x = 0
        y = len(pro) - 1
        while y - x > -1:
            if pro[x] == pro[y]:
                x += 1
                y -= 1
            else:
                ret = False
                break

    except:
        ret = False

    return ret


def product_generator():
    num1 = 999
    while num1 > 99:
        num2 = 999
        while num2 > 99:
            yield num1, num2
            num2 -= 1
        num1 -= 1


if __name__ == "__main__":
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """

    for n1, n2 in product_generator():
        product = n1 * n2
        if is_palindrome(product):
            print 'n1={0}, n2={1}, product={2}'.format(n1, n2, product)
            break
