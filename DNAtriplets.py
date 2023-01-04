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
        for i in range(0, len(DNAseq)):
            if(DNAseq[i : i+3] == 'ATG'):
                return i+3
                break
    
def add_codons():
    if check_sequence() == True:
        start_codon_ending = find_start_codon() 
        if start_codon_ending is not None:
            for j in range(start_codon_ending, len(DNAseq), 3):
                if len(DNAseq[j:j+3]) % 3 == 0:
                    codon = DNAseq[j:j+3]
                    orf.append(codon)
        else:
            print("There is no ORF")
    return orf
                    
    
def find_finish_codon():
    add_codons()
    for i in range(len(orf)):
        if 'TAA' in orf:
            taa = orf.index('TAA')
            print("The ORf is: {}".format(orf[:taa]))
            break
        elif 'TGA' in orf:
            tga = orf.index('TGA')
            print("The ORf is: {}".format(orf[:tga]))
            break
        elif 'TAG' in orf:
            tag = orf.index('TAG')
            print("The ORf is: {}".format(orf[:tag]))
            break
        else:
            print("We don't have an ORF")
            break
            

find_finish_codon()
        



