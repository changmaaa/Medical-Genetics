#!/usr/bin/env python
# -*- coding: utf-8 -*-

##변수 초기화
aa_dic={} #Amino Acid count dictionary

while True:
    #사용자 입력값 저장
    input_str = input("Amino Acid sequence: ")
    #exit 입력받으면 종료
    if input_str=="exit" : break
    
    ##딕셔너리를 이용한 아미노산 갯수 세는 코드
    for aa in input_str:
        #key값이 있으면 실행 
        if aa_dic.get(aa):
            aa_dic[aa]+=1
    
        #key값이 없으면 실행
        else:
            aa_dic[aa]=1
            
    ##결과 출력하는 코드      
    print("Frequency of Each Amino Acid is : ")
    #마지막 아미노산 end aa에 저장
    end_aa=list(aa_dic.keys())[-1]
    for aa, count in aa_dic.items():
        if aa == end_aa:
            #마지막 아미노산은 \n 포함하여 출력
            print("{}:{}".format(aa, count))
        else:
            print("{}:{}".format(aa, count),end=", ")
            
            
    #딕셔너리는 입력한 순서대로 저장되기 때문에,
    #마지막으로 저장한 key값이 마지막에 있다.
    #리스트에서 마지막원소는 -1 인덱스를 갖는다.