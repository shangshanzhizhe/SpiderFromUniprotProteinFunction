#!/usr/bin/python3

import sys,re


def read_file(infile):
    info = {}
    f = open(infile,'r')
    for line in f:
        if line.startswith('Class'): continue
        line = str(line.strip())
        content = line.split('\t')
        gene_text = ''
        if re.search(r'\"(.*)\"', content[10]):
            gene_text = re.search(r'\"(.*)\"', content[10])[1]
        else:
            gene_text = content[10]
        genes = gene_text.split(',')
        for gene in genes:
            if not gene: continue
            if gene in info:
                info[gene].append(content[2])
            else:
                info[gene] = [content[2]]
    return info
    
def read_reffile(reffile):
    reference = {}
    f = open(reffile, 'r')
    for line in f:
        line = line.strip()
        content = line.split('\t')
        go_list = content[1].split(',')
        reference[content[0]] = go_list
    return reference

def check(reffile, infile):
    reference = read_reffile(reffile)
    info = read_file(infile)
    for gene in info:
        for goid in info[gene]:
            if goid not in reference[gene]:
                print(gene + '\t' + goid)

if __name__ == "__main__":
    reffile = sys.argv[1]
    infile = sys.argv[2]
    check(reffile, infile)