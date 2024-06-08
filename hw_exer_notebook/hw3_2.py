#!/usr/bin/env python
import sys

##get input
f_name=sys.argv[1]
input_symbol=sys.argv[2]

##read file and print result
f=open(f_name,"r")
for line in f.read().splitlines():
    # if "#" in line: continue
    if input_symbol in line:
        gene_list = line.split("\t")
        chr = gene_list[0]
        start = gene_list[1]
        end = gene_list[2]
        symbols = gene_list[6]
        approved_symbols = gene_list[8]
        entrez = gene_list[9]
        phenotypes=gene_list[12]

        if input_symbol==approved_symbols or input_symbol in symbols.split(", "):
            print("{} {} {} {} {} {}".format(chr,start,end,symbols,entrez,phenotypes))
f.close()    