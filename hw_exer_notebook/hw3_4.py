#!/usr/bin/env python

##Variant initialization
vcf_fname="sample1.vcf"
annotation_fname="sample1_annotation.tsv"
result_fname="sample1_short.vcf"
variant_dic={}

##read annotation file
f=open(annotation_fname,"r")
for line in f.read().splitlines():
    if "Coordinate" in line: continue
    variant_list = line.split("\t")
    chr=variant_list[2]
    coordinate=variant_list[3]
    key="chr"+chr+":"+coordinate
    #print(key)
    variant_dic[key]=1
f.close()

##read vcf file and extract data
with open(vcf_fname,"r") as f, open(result_fname,"w") as fw:
    for line in f.read().splitlines():
        if "#" in line :
            fw.write(line+"\n")
        else:
            vcf_variant = line.split("\t")
            chr = vcf_variant[0]
            pos = vcf_variant[1]
            vcf_key=chr+":"+pos
            #print(key)
            if variant_dic.get(vcf_key) != None:
                fw.write(line+"\n")
                
                
#아이디어 :  annotation 정보를 "chr1:1237399" 와 같은 형태로 딕셔너리에 저장했다. 
#이때 value 값은 1로 의미없는 숫자를 넣어사용했다.
#리스트에서 찾는 것 보다 딕셔너리에서 get함수 사용하는 것이 더 빠르기 때문이다.
#즉, 메모리 용량(의미없는 숫자를 저장)을 감수할만한 속도 차이가 있기 때문이다.