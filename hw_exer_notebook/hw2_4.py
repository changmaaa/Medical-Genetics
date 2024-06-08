#!/usr/bin/env python
# -*- coding: utf-8 -*-

##변수 초기화
#사용자 입력값 저장
input_str = input("What is the string to repeat? ")
input_re = input("How many time you want to repeat? ")

##결과 출력
result = input_str*int(input_re)
print("Our output is {}".format(result))