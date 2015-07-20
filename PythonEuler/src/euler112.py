#! /usr/bin/python
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="andrew.tuley"
__date__ ="$20-Jul-2015 15:02:11$"


increasing=1
decreasing=-1
unknown=0

def is_bouncy(number):
    bouncy = False
    
    if number<100:
        return False
    
    snum=str(number)
    v=snum[0]
    x=1
    if snum[x] > v:
        state=increasing
    elif snum[x] < v:
        state=decreasing
    else:
        state=unknown

    while x < len(snum):
        if snum[x] > v: 
            if state == decreasing:
                bouncy=True
                break
            state=increasing
        elif snum[x] < v:
            if state == increasing:
                bouncy=True
                break
            state=decreasing
        v = snum[x]
        x += 1
        
    if state == unknown:
        bouncy = False
        
    return bouncy

if __name__ == "__main__":
    """
    Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

    Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

    We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

    Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. 
    
    In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

    Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

    Find the least number for which the proportion of bouncy numbers is exactly 99%.
    """
    

    x=1
    bouncy=0
    stable=0
    while x <= 2178000:
        if is_bouncy(x):
            bouncy += 1
        else:
            stable += 1
        if stable*99 == bouncy*1:
            print 'x={0} bouncy {1} not-bouncy {2}'.format(x, bouncy, stable)
        
        x += 1
    #print 'bouncy {0} not-bouncy {1}'.format(bouncy, stable)
    