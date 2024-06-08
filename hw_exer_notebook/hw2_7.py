#!/usr/bin/env python
# -*- coding: utf-8 -*-

#사용자 입력값 저장
input_str = input("Input Sequence is : ")
input_list = input_str.split(" ")

#DNA 시퀀스파일 저장
f = open("DNA_seq.txt","r")
DNA_seq = f.readline()
f.close()

##결과 출력 코드
print("Frequency of each sequence is :")
for motif in input_list:
    #변수 초기화, motif 마다 길이랑 갯수가 다르므로
    m_len = len(motif)
    count = 0
    repeat = len(DNA_seq)-m_len #
    for idx in range(repeat):
        if motif == DNA_seq[idx : idx+m_len]:
            count += 1
    print("{} occurs {} times".format(motif,count))
