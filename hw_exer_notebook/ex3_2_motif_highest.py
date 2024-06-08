#!/usr/bin/env python 

# sys.argv로 motif dir, dna_dir, cutoff score 입력
import sys 
motif_dir = sys.argv[1]
dna_dir = sys.argv[2]

#file dir 설정
root_dir = "/home/share/medicalgenetics/ex3/"
motif_dir = root_dir + sys.argv[1]
dna_dir = root_dir + sys.argv[2]

#dna파일을 한줄씩 읽으면서 header ">"로 시작하지 않으면 한줄씩 dna sequence 뒤에 붙여줌
dna_f = open(dna_dir, "r")

dna_seq = ""
while True : 
    line = dna_f.readline().strip()
    if not line : break
    if line[0] != ">" :
        dna_seq += line

dna_f.close()

# motif 파일을 한줄씩 받아와서, A,C,G,T를 key로 하는 딕셔너리에 저장
motif_f = open(motif_dir, "r")

ACGT_dict = {}
ACGT = ["A","C","G","T"]

i = 0 # ACGT의 Index 
while True : 
    line = motif_f.readline().strip()
    if not line : break
    ACGT_dict[ACGT[i]] = line.split("\t") # 각 염기에 해당하는 score를 리스트 형태로 저장
    i += 1

motif_f.close()

max_score = 0 # 현재 가장 높은 score를 저장하는 변수
# indexing으로 seq_tmp를 6개씩 뽑아와서 ACGT_dict를 사용하여 score 계산
for i in range(len(dna_seq)-6) :
    pos = 0 # seq_tmp에서 현재 보고 있는 위치를 저장하는 변수
    score = 1 # 계속 점수를 곱해주므로 1로 시작
    seq_tmp = dna_seq[i:i+6] # 현재 보고 있는 seq 6개
    for nuc in seq_tmp : # nuc는 seq_tmp에서 하나의 염기
        # 현재 보고 있는 염기(nuc)을 key로, seq_tmp에서의 위치(pos)를 value에서의 index로 사용해서 score에 곱해줌
        score *= float(ACGT_dict[nuc][pos])
        pos += 1 # 다음 포지션을 보기위해서 pos 1증가
    # 계산한 score가 이전에 본 score보다 높으면, max_score를 score로 update, seq을 max_seq에 저장
    if score > max_score : 
        max_score = score
        max_seq = seq_tmp

print("Sequence with Max Score :", max_seq, "\nScore :", max_score)
