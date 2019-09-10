# -*- coding:utf-8 -*-
from sys import argv

script, input_file = argv

#定义函数
def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print line_count, f.readline()

current_file = open(input_file) #打开文件

print "First let's print the whole file:\n"

print_all(current_file) #print_all函数传参，打印出文件内容

print "Now let's rewind, kind of like a tape."

rewind(current_file) #rewind函数传参，文件指针偏移到开头

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line +1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)
