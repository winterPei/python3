#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#sum = 0
#for x in [1,2,3,4,5,6,7,8,9,10]:
#	sum = sum + x
#print(sum)

#range(x)生成序列 从0开始小于当前x
#sum = 0
#for x in range(101):
#	sum = sum + x
#print(sum)

#while循环
#sum = 0
#n = 99
#while n > 0:
#	sum = sum + n
#	n = n - 2
#print(sum)

#break的使用
#n = 1
#while n<=100:
#	if n > 10:
#		break
#	print(n)
#	n = n + 1
#print('END')

#continue的使用
n = 0
while n < 10:
	n = n + 1
	if n%2 == 0 :
		continue
	print(n)