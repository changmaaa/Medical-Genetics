#!/usr/bin/env python

##Variant initialization
f_name="OMIM_genemap2_2021_11.txt"
input_phenotypes="Autosomal recessive"
lower_input_phenotypes=input_phenotypes.lower()
count_dic={}
result_fname="AutosomalRecessive_Gene.txt"

##read file and print result
# 아이디어 : 입력 받은 phenotypes과 문자열로 받은 파일 한줄을 모두 소문자로 통일시킴으로써
# 문장안에 phenotypes이 있는 경우(Pseudoautosomal recessive)를 고려하였다.
with open(f_name,"r") as f, open(result_fname,"w") as fw:
    for line in f.read().splitlines():
        lower_line=line.lower()
        if lower_input_phenotypes in lower_line:
            gene_list = line.split("\t")
            chr = gene_list[0]
            start = gene_list[1]
            end = gene_list[2]
            approved_symbols = gene_list[8]
            entrez = gene_list[9]
            ensembl = gene_list[10]
            phenotypes=gene_list[12]
            new_line = "{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(chr,start,end,approved_symbols,entrez,ensembl,phenotypes)
            #print(new_line)
            fw.write(new_line)
            
            if chr in count_dic:
                count_dic[chr]+=1
            else:
                count_dic[chr]=1

    for key in count_dic.keys():
        new_line="{} : {} 개\n".format(key,count_dic[key])
        #print(new_line)
        fw.write(new_line)
#파일이 이미 정렬되어있기 때문에, 순서대로 읽기만해도 정렬된 순서대로 출력할 수 있다.
#혹은 new_line을 리스트에 저장할 때, append 함수를 이용하면 정렬 순서를 유지할 수 있다.
#만약 파일이 정렬되어있지 않은 경우에서의 코드가 궁금한 사람은 메일 주세요..!