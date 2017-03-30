#!/usr/bin/env python
# -*- coding: utf-8 -*
f = file('file/data.txt')
# data = f.read()
# data = f.readline()
data = f.readlines()
print data
f.close()
