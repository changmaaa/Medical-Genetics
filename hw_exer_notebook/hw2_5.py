#!/usr/bin/env python
# -*- coding: utf-8 -*-

#사용자 입력값 저장
input_str = input("input : ") # index : 1 ~ 7

##변수 초기화
my_arr= ['Ala','Phe','Cys','Gly','Val','Met', 'Trp'] # index : 0 ~ 6
#입력 받은 숫자를 리스트로 저장한 뒤, int 자료형으로 바꿈
idx_list = list(map(int, input_str.split(",")))
arr_len = len(my_arr) # 7
result_list=[]

# 결과를 리스트에 저장
# append 함수는 입력 순서대로 저장하기 때문에
for idx in idx_list:
    if 1<= idx <= arr_len:
    #if 1<= idx and idx <= arr_len:
        result_list.append(my_arr[idx-1])
    else:
        result_list.append("Error")

idx_len = len(idx_list)
for aa_idx in range(idx_len):
    #마지막 아미노산은 \n 포함하여 출력
    if aa_idx == idx_len-1:
        print(result_list[aa_idx])
    else:
        print(result_list[aa_idx],end=", ")