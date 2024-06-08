#!/usr/bin/env python 

# 코돈 테이블 딕셔너리로 저장
ref = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
       "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
       "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
       "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
       "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
       "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
       "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
       "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
       "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
       "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
       "UAA":  "", "CAA": "Q", "AAA": "K", "GAA": "E",
       "UAG":  "", "CAG": "Q", "AAG": "K", "GAG": "E",
       "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
       "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
       "UGA":  "", "CGA": "R", "AGA": "R", "GGA": "G",
       "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }
    
# sequence length 길이가 3의 배수일때까지 sequence 입력받음
while True : 
    seq = input("RNA : ")
    seq_len = len(seq)
    if seq_len % 3 == 0 : break
    else : print("retry, sequence length is",seq_len)

# sequence를 idx를 3씩 늘려가면서 한번에 3개씩 보면서 대문자로 바꿈.
# 딕셔녀러의 key값으로 조회해서 value를 이어서 한줄로 출력
idx = 0
while True :
    if idx >= len(seq) : break
    codon = seq[idx:idx+3].upper()
    amino = ref[codon]
    print(amino,end="")
    idx += 3
print()