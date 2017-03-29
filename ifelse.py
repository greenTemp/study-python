#!/usr/bin/env python
#-*- coding: utf-8 -*
print 'please input x:'
x = input()
print 'please input y:'
y = input()

if x == 0:
    if y == 0:
        print 'origin'
    elif y > 0:
        print 'y+'
    else:
        print 'y-'
elif x > 0:
    if y == 0:
        print 'x+'
    elif y > 0:
        print '1'
    else:
        print '2'
else:
    if y == 0:
        print 'x-'
    elif y > 0:
        print '4'
    else:
        print '3'
