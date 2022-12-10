#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:53:49 2022

@author: EvdoksiaKetevan
"""

finish_codons = ['TAA', 'TAG', 'TGA']

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
                print("We have the starting codon ATG starting in {} and ending in {}!".format(i,i+2))
                return i+2
                return True
    return False

def find_finish_codon():
    if check_sequence() == True and find_start_codon() != False:
        start_codon_ending = find_start_codon() + 1 
        for j in range(start_codon_ending, len(DNAseq), 3):
            if len(DNAseq[j:j+3]) % 3 == 0:
                codon = DNAseq[j:j+3]
                if codon not in finish_codons:
                    orf.append(codon)
                else: 
                    break
    print(orf)
                    
    

                    
                
        
find_finish_codon()

        



