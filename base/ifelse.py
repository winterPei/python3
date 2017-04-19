#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#ifelse的例子 判断年龄范围
num = input('age: ')
age = int(num)
if age >= 20:
	print('your age  is',age)
	print('adult')
elif age>=6:
	print('your age is',age)
	print('teenager')
else:
	print('kid')