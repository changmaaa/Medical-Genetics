#!/usr/bin/env python

##get input
f_name=input("file name : ")

##Variant initialization
ACGT_dic={"a":0,"c":0,"g":0,"t":0}
total=0


##read file and count bases
f=open(f_name,"r")
for line in f.read().splitlines():
    ACGT_dic['a'] += line.count('a')
    ACGT_dic['c'] += line.count('c')
    ACGT_dic['g'] += line.count('g')
    ACGT_dic['t'] += line.count('t')
total=ACGT_dic['a']+ACGT_dic['c']+ACGT_dic['g']+ACGT_dic['t']
f.close()

##print result
for key in ACGT_dic.keys():
       result=round(ACGT_dic[key]/total,2)
       base=key.upper()
       print("{} : {} percent".format(base,result))