#!/usr/bin/env python
# -*- coding: utf-8 -*-

# seq1 = "CCCCCCAATTGTAACAATCGTCGTAGACCGTG"
# seq2 = "ACCGCAGTCCGTGACTTTCGTCCTACGCATAG"

#인풋 입력받아서 저장,
seq1=input("seq1 : ")
seq2=input("seq2 : ")

#변수 초기화
seq1_list=list(seq1.upper())
seq2_list=list(seq2.upper())
l=len(seq1_list)#문제에서 같은 길이의 시퀀스를 입력받는다고 가정했으므로, len(seq2_list)도 가능하
idx=0
result=0

#결과 생성 코드
while True:
	if idx >= l : break
	if seq1[idx] != seq2[idx] : result+=1
	idx+=1
print("total length : ",l)
print("mismatch count : ",result)	
