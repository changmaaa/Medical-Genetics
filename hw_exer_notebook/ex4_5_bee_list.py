#!/usr/bin/env python 

# regular expression을 선언
import re

check = '\(?([\w\s,\.\-\&]*),\s(\d{4})\)?'

# 파일을 디렉토리 설정
file_path = "/home/share/medicalgenetics/bee_list.txt"

f = open(file_path, "r")

#파일을 불러와서, tab을 기준으로 split, 두번째 부분만 regular expression 적용. 
#findall()을 사용하여 regular expression을 만족하는 모든걸 리스트로 받고, author_year에 이중리스트 형태로 저장
author_year = []
while True : 
    line = f.readline().strip()
    if line == "" : break
    aut_year_tmp = line.split("\t")[1]
    result = re.findall(check, aut_year_tmp)
    if result != [] :
        author_year.append(result[0])
f.close()

####################################################################################################

#author_year에서 author에 해당하는 부분만 author_list에 저장
author_list = []
for tmp in author_year :
    author_list.append(tmp[0])

# &가 있는 경우와 없는 경우로 나눠서, 여러명이면 &를 기준으로 split으로 나눠서 진행.
# author 이름을 key, 나온 횟수가 value인 dictionary에 저장
# key가 이미 존재하는 key이면 val을 1로 입력, 이미 존재하는 key이면 value를 1 증가
author_cnt_dict = {}

for author_tmp in author_list : 
    if "&" in author_tmp :
        list_tmp = author_tmp.split(" & ")
        for author in list_tmp : 
            if author not in author_cnt_dict : 
                author_cnt_dict[author] = 1
            else :
                author_cnt_dict[author] += 1
    else : 
        author = author_tmp
        if author not in author_cnt_dict : 
            author_cnt_dict[author] = 1
        else :
            author_cnt_dict[author] += 1

# 최대값을 저장하는 변수를 0으로 설정
max_val = 0

# key를 하나씩 보면서 value가 max_val보다 큰 경우, key와 value를 각각 max_author와 max_val에 저장
for key in author_cnt_dict.keys() :
    if author_cnt_dict[key] > max_val :
        max_author = key
        max_val = author_cnt_dict[key]

# 결과 출력
print(max_author, ":", max_val,"times")

####################################################################################################

#author_year에서 year에 해당하는 부분만 year_list에 저장
year_list = []
for tmp in author_year :
    year_list.append(tmp[1])

# 연도를 key, 나온 횟수가 value인 dictionary에 저장
# key가 이미 존재하는 key이면 val을 1로 입력, 이미 존재하는 key이면 value를 1 증가
year_cnt_dict = {}
for year in year_list :
    if year not in year_cnt_dict :
        year_cnt_dict[year] = 1
    else : 
        year_cnt_dict[year] += 1

# 최대값을 저장하는 변수를 0으로 설정
max_val = 0

# key를 하나씩 보면서 value가 max_val보다 큰 경우, key와 value를 각각 max_author와 max_val에 저장
for key in year_cnt_dict :
    if year_cnt_dict[key] > max_val :
        max_idx = key
        max_val = year_cnt_dict[key]

# 결과 출력
print("Most represented years :", max_idx)