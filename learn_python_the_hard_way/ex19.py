# -*- coding:utf-8 -*-
# 定义函数
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) #直接传入数字参数


print "Or,we can use variables from our script:"
amount_of_cheese = 10 #变量赋值
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #先给变量赋值，变量的内容再传参到函数


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) #函数内参数先运算，再传参数


print "And we can combine the two ,variables and math:"
cheese_and_crackers(amount_of_cheese + 100,
amount_of_crackers + 1000) #函数里参数先变量运算，再传参数
