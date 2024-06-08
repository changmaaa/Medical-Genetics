#!/usr/bin/env python3

#딕셔너리에 파일 저장
dic={}
f=open("Homo_sapiens_gene_Synonyms.txt","r")
while True:
    line = f.readline().strip()
    if not line: break
    if "GeneID" in line : continue #헤더 정보는 생략하고 저장
    tmp=line.split("\t")
    dic[tmp[0]]=[tmp[1],tmp[2].split("|")]#key=gene id, value=[symbol, synonyms list], synonyms list는 split을 통해 생성된다.
f.close()

#실행 코드
while True:
    geneID=input("gene ID : ")
    if geneID == "stop": break
    if geneID not in dic.keys():
        print(geneID,"is not in file")
        break
    symbol=dic[geneID][0]
    synonyms=dic[geneID][1]
    if "-" in synonyms : #synonyms 없는 경우
        sy_num=0
    else:
        sy_num=len(synonyms)
    print("gene ID {0} : symbols is {1} and the number of synonyms is {2}".format(geneID,symbol,sy_num))
