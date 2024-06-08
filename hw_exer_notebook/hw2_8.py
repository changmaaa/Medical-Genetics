#!/usr/bin/env python
# -*- coding: utf-8 -*-

##결과 생성 코드, search fram 함수 만들어서 사용
def search_fram(seq): #frame+1,+2,+3,-1,-2,-3 에 해당하는 시퀀스를 입력으로 받는다
    ##변수 초기화
    STEP=3 #codon 길이가 3이므로
    sub_seq="" #fram 에서 읽어본 codon을 임시 저장한다.
    flag=False  
    start_codon="atg"
    end_codon=["tag","tga","taa"]
    
    #frame으로부터 codon을 읽어온다.
    for idx in range(0,len(seq), STEP):
        sub_seq = seq[idx:idx+STEP]
         #첫번째 atg 코돈에 대해서만 flag를 True로 바꾸고, result 변수를 초기화 한다.
         #두번째 atg 부터는 start codone이 아닌 methionine이므로,
        if sub_seq == start_codon and flag==False:
            flag=True
            result=""
        #첫번째 end codon 을 만날때까지, 모든 sub seq를 result에 저장한다.
        if flag:
            result +=sub_seq
            if sub_seq in end_codon:
                if len(result)>6: 
                    return result
                ##start codon 뒤에 바로 end codon이 있는 경우,ORF 조건을 만족하지 않으므로
                #그 다음 atg 코돈을 찾도록 flag를 False로 바꿔준다.
                else:
                    flag=False 
    #모든 조건을 만족하지 않는, 즉 ORF 가 없는 경우 None
    return None 

##변수 초기화
DNA_seq=""
with open("BRCA2_DNAsequence.txt","r") as f, open("BRCA2_DNA.txt","w") as fw:
    for char in f.read(): #Character
        if char.isalpha():
            DNA_seq+=char
            fw.write(char)

FRAME1=DNA_seq[0:] #fram +1
FRAME2=DNA_seq[1:] #fram +2
FRAME3=DNA_seq[2:] #fram +3

#complement
com_base={"a":"t","c":"g","g":"c","t":"a"}
com_seq=""
for base in DNA_seq:
    com_seq += com_base[base]
re_com_seq = com_seq[::-1]

FRAME4=re_com_seq[0:] #fram -1
FRAME5=re_com_seq[1:] #fram -2
FRAME6=re_com_seq[2:] #fram -3


FRAME_dic={
    "FRAM +1": search_fram(FRAME1),
    "FRAM +2": search_fram(FRAME2),
    "FRAM +3": search_fram(FRAME3),
    "FRAM -1": search_fram(FRAME4),
    "FRAM -2": search_fram(FRAME5),
    "FRAM -3": search_fram(FRAME6),  
}

##결과 출력 코드
max_length=0 #가장 긴 ORF 길이 
max_frame="" #가장 긴 ORF 갖는 frame 이름
for key in FRAME_dic:
    ORF=FRAME_dic[key]
    ##결과 출력
    print(key,ORF)
    length=len(ORF)
    ##가장 긴 시퀀스 찾는 과정
    if max_length < length:
        max_length=length
        max_frame=key    

print("The ORF of the longest length is at ",max_frame)
print(FRAME_dic[max_frame])
