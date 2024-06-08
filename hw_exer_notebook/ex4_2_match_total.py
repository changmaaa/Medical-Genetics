#!/usr/bin/env python 


root_dir = "/home/share/medicalgenetics/" # 라이브러리 import

import sys 

# 파일을 argv로 받아옴
file_path = root_dir + sys.argv[1]

# 파일을 동물 이름을 key, 나머지 서열을 value로 저장하는 dictionary로 저장
f = open(file_path, 'r')

file_dict = {}

while True : 
    line = f.readline().strip()
    if not line : break
    # 동물이름은 > 로 시작하므로 동물이름이면 key로 저장하고, value를 아무것도 없는 문자열로 저장
    if line[0] == ">" :
        key = line[1:]
        file_dict[key] = ""
    else : 
        # 이전 줄에서 읽은 key값이 바뀌지 않았으므로, 해당 key의 value에 line을 이어서 붙여준다.
        file_dict[key] += line

f.close()

#비교할 두 서열을 file_list에 저장
file_list = []
for key in file_dict :
    file_list.append(file_dict[key])

#비교할 두 서열을 각자 문자열 형태로 저장
line1 = file_list[0]
line2 = file_list[1]

# 비교할 문자열 길이를 설정하고, 처음 score 설정
seq_len = len(line1)
score = 0
# match인 경우만 score를 추가
for i in range(seq_len) :
    word1 = line1[i]
    word2 = line2[i]
    if word1 == word2 :
        score += 1
# match/seq_len으로 계산
print(score/seq_len)