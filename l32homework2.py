#!/usr/bin/env python
# -*- coding: utf-8 -*
isMore = True
string = ''
while isMore:
    print 'please input the text u wants to save:'
    string += raw_input() + '\n'
    print 'more text do u want to input?(y/n)'
    more = raw_input()
    if more != 'y':
        isMore = False
file = file('file/inputText.txt', 'w')
file.write(string)
file.close()
