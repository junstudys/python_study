# -*- coding:utf-8 -*-
x = "There are %d types of people." % 10 #可以直接用数字
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary,do_not) #变量传入，再赋值给y作为新的字符变量

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y
hilarious = False
joke_evaluation = "Isn'y that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w+e #使用+进行拼接
