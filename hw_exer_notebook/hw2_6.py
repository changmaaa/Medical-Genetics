#!/usr/bin/env python
# -*- coding: utf-8 -*-

##변수 초기화
#사용자 입력값 저장
input_str1 = input("input string 1 : ")
input_str2 = input("input string 2 : ")

##정답 문자열 생성하는 코드
str1_len=len(input_str1)
result_str1 = input_str1 + input_str2
result_str2 = " " * str1_len + input_str2 #str1 길이만큼의 공백

##결과 출력
print(result_str1)
print(result_str2)