from decimal import HAVE_CONTEXTVAR
from msilib import sequence
import random as rn
from turtle import fd
DNA = ['A','C','G','T']

def Ramdon_Sequence():
    
    DNA_Ramdon_Sequance = [] 
    str_sequence = ""

    for i in range(4):
        for j in range(100):
            DNA_Ramdon_Sequance.append(DNA[rn.randint(0,3)])
        DNA_Ramdon_Sequance.append("\n")
        
    DNA_Ramdon_Sequance.pop(-1)

    for element in DNA_Ramdon_Sequance:
        str_sequence+=element
    

    return str_sequence

print(Ramdon_Sequence())
