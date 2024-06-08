#!/usr/bin/env python 

import sys # 라이브러리 import

root_dir = "/home/share/medicalgenetics/" 

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
    # 이전 줄에서 읽은 key값이 바뀌지 않았으므로, 해당 key의 value에 line을 이어서 붙여준다.
    else : 
        file_dict[key] += line

f.close()

#비교할 두 서열을 file_list에 저장
file_list = []
for key in file_dict :
    file_list.append(file_dict[key])

#비교할 두 서열을 각자 문자열 형태로 저장
line1 = file_list[0]
line2 = file_list[1]

# 비교할 문자열 길이를 설정하고, match개수를 저장할 score와 match+mismatch를 저장할 total 변수 선언
seq_len = len(line1)
score = 0
total = 0
for i in range(seq_len) :
    word1 = line1[i]
    word2 = line2[i]
    # indel이면 아무 동작 취하지 않음
    if word1 == "-" or word2 == "-" :
        continue
    else : 
        # match면 score와 total 둘다 1씩 증가
        if word1 == word2 :
            score += 1
            total += 1
        # mismatch면 total만 1 증가
        else :
            total += 1

print(score/total)