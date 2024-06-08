#!/usr/bin/env python 

import sys # 라이브러리 import

# 파일 및 각 score 를 argv로 받아옴
root_dir = "/home/share/medicalgenetics/"

file_path = root_dir + sys.argv[4]
match = int(sys.argv[1])
mismatch = int(sys.argv[2])
indel= int(sys.argv[3])

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
for i in range(seq_len) :
    # 각 단어를 하나씩 받아와서 저장
    word1 = line1[i]
    word2 = line2[i]
    # 먼저 - 이 있는지 확인하여 indel을 계산
    if word1 == "-" or word2 == "-" :
        score += indel
    # indel이 아닌 경우 mismatch와 match인 경우를 각각 비교해서 score에 더함
    else : 
        if word1 == word2 :
            score += match
        else :
            score += mismatch
#최종 score 출력
print(score)
