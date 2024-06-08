#!/usr/bin/env python 

# input path 설정
file_path = "/home/share/medicalgenetics/humanDNAsample.dna"

# 파일을 열어서 헤더가 아닌 부분만 seq에 추가
f = open(file_path, 'r')

seq = ""
while True : 
    line = f.readline().strip()
    if not line : break
    if line[0] != "#" and line[0] != ">" :
        seq += line

f.close()

# 4개씩 indexing 하여 seq_list에 저장
seq_list = []
for i in range(len(seq)-4) :
    temp = seq[i:i+4]
    seq_list.append(temp)

# 각 seq부분을 key로 하여, 딕셔너리 key에 없는 seq이면 value를 1로 해주고, 이미 존재하면 value를 1을 더해줌
subseq_dict = {}
for temp in seq_list :
    if temp not in subseq_dict.keys() :
        subseq_dict[temp] = 1
    else : 
        subseq_dict[temp] += 1

#operator 함수를 써서 value를 기준으로 subseq_dict를 sorting, 이중리스트 형태로 반환 받는다
import operator
sorted_list = sorted(subseq_dict.items(), key=operator.itemgetter(1), reverse=True)

#sorted된 이중리스트인 sorted_list를 한줄씩 출력
for tmp_list in sorted_list : 
    print(tmp_list[0],tmp_list[1])