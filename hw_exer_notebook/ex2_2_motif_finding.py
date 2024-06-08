#!/usr/bin/env python 

#파일을 불러와서 seq에 붙여가면서 저장
file_path = "/home/share/medicalgenetics/DNA_seq.txt"
f = open(file_path, "r")

seq = ""
while True : 
    line = f.readline().strip()
    if not line : break
    seq += line
f.close()

# usr_input = "CAAGTTACA AGTTACAAG"

# motif를 입력받아서 split으로 나눠 하나씩 리스트에 넣어서 저장
usr_input = input("motif : ")
motif_list = usr_input.split(" ")

# seq와 motif를 입력받아 motif 위치를 반환하는 함수
def motif_finder(seq, motif) :
    seq_len = len(seq)
    motif_len = len(motif)
    motif_idx = []
    # indexing을 통해 seq_temp에 6개씩만 잘라서 저장, motif와 같은지 비교, 같으면 index를 저장
    for i in range(seq_len-motif_len) :
        seq_tmp = seq[i:i+motif_len]
        if seq_tmp == motif : 
            motif_idx.append(str(i+1))
    
    return motif_idx

# motif이름과 리스트를 입력받아 출력하는 함수
def motif_print(motif_list,motif) :
    print(motif, "is in")
    #리스트를 join으로 합쳐서 하나의 string으로 출력
    print_str = ','.join(motif_list)
    print(print_str)

# motif를 하나씩 seq와 비교해서, 그 결과를 출력하는걸 위에서 선언한 함수로 실행
for motif in motif_list :
    answer = motif_finder(seq,motif)
    motif_print(answer, motif)