"""
Title: Máximo Común Divisor (MCD)
Author: Diego Felipe Sánchez Medina
Mail: dsanchezme@unal.edu.co
"""

a=64
b=24

def MCD(a,b):
  if(a%b==0):
    return b
  return MCD(b,a%b)

print(MCD(a,b))
