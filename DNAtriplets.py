#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:53:49 2022

@author: EvdoksiaKetevan
"""

DNAseq = input("Give me your DNA sequence:\n").upper()

orf = []

def check_sequence():
    for char in DNAseq:
        if char not in 'ATGC':
           print("That is not a DNA sequence!")
           break
        else:
           return True 

def find_start_codon():
    if check_sequence() == True:
        for i in range(len(DNAseq)):
            if DNAseq[i] == 'A' and DNAseq[i+1] == 'T' and DNAseq[i+2] == 'G':
                return i+2
                return True
                print("There is a start codon")
    return False
    
def add_codons():
    if check_sequence() == True and find_start_codon() != False:
        start_codon_ending = find_start_codon() + 1 
        for j in range(start_codon_ending, len(DNAseq), 3):
            if len(DNAseq[j:j+3]) % 3 == 0:
                codon = DNAseq[j:j+3]
                orf.append(codon)
    print(orf)
                    
    

def find_finish_codon():
    for i in range(len(orf)):
        if 'TAA' in orf:
            taa = orf.index('TAA')
            print(orf[:taa])
            break
        elif 'TGA' in orf:
            tga = orf.index('TGA')
            print(orf[:tga])
            break
        elif 'TAG' in orf:
            tag = orf.index('TAG')
            print(orf[:tag])
            break
        else:
            print("We have no ORF!")
            break
            
    
    
    

add_codons()
find_finish_codon()
        



