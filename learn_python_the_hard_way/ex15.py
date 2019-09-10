# -*- coding:utf-8 -*-
from sys import argv #导入模块

script, filename = argv #参数解包

txt = open(filename) #open函数用于打开一个文件

print "Here's your file %r:" % filename
print txt.read() #file.read() file.readline()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
