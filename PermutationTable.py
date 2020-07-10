"""
Title: Tabla Composición - Permutaciones
Author: Diego Felipe Sánchez Medina
Mail: dsanchezme@unal.edu.co
"""

from tabulate import tabulate
import itertools as it
from google.colab import files

set0 = {1,2,3,4,5}
a = it.permutations(set0, 5)
row = []
col = [row]

matrix = []

for w in a:
    m = []
    row.append(list(w))
    
for i in range(120):
    rows = []
    for j in range(120):
        r = []
        for k in range(5):
            r.append(row[j][row[i][k]-1])
        rows.append(r)
    rows.insert(0,row[i])
    matrix.append(rows)
row.insert(0,"")
    
print(tabulate(matrix, headers=row, tablefmt='fancy_grid'))
