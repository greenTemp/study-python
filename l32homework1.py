#!/usr/bin/env python
# -*- coding: utf-8 -*
f = file('file/data.txt')
data = f.read()
f2 = file('file/data2.txt', 'w')
f2.write(data)
f.close()
f2.close()
