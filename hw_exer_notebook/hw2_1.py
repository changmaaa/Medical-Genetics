#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    #사용자 입력값 저장
    input_str = input("Cracked DNA sequence : ")
    #exit 입력받으면 종료
    if input_str=="exit" : break
    
    #숫자 제거한 뒤, input_str에 다시 저장
    for sub_str in input_str:
        if sub_str.isdigit():
            input_str=input_str.replace(sub_str,"")
    print("Original DNA sequence : "+input_str)