#!/usr/bin/env python
# -*- coding: utf-8 -*-

##변수 초기화
#사용자 입력값 저장
input_str = input("Palindrome check: ")

up_input_str = input_str.upper() #대문자로 통일
half_len = len(up_input_str)//2 #2로 나눈 몫 저장
flag = True #True : palindrome, 

##palindrome 판단하는 코드
for idx in range(half_len):
    start_base = up_input_str[idx]
    end_base = up_input_str[-idx-1]
    
    #하나라도 서로 다른 문자가 있으면 아래 실행
    if start_base != end_base:
        flag=False
        #print(start_base, end_base)
        
##결과 출력
if flag:  #True : palindrome  
    print("Yes, {} is a palindrome".format(input_str))
else:   #False : not a palindrome
    print("Error! It is not a palindrome")