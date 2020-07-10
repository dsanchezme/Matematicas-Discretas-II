"""
Title: Greater Common Divisor (GCD)
Author: Diego Felipe Sánchez Medina
Mail: dsanchezme@unal.edu.co
"""

a=64
b=24

def GCD(a,b):
  if(a%b==0):
    return b
  return GCD(b,a%b)

print(GCD(a,b))
