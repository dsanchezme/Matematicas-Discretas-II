# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 18:39:06 2020

@author: Diego Sánchez

Grupo de Automorfismos

"""

import networkx as nx
import matplotlib.pyplot as plt 
import itertools as it

#Recibir grafo y dibujarlo

print("\t\t\tAUTOMORFISMOS DE UN GRAFO\n")

print("\tINSTRUCCIONES\n")
print("\t > Ingresar los vertices separados de espacios")
print("\t > Para ingresar las aristas:")
print("\t     - Separe cada nodo con un espacio")
print("\t     - Presione enter para ingresar otra arista")
print("\t     - Si no desea ingresar más aristas, presione dos enter's")
print("\t > Finalmente, confirme si el grafo dibujado es el deseado")
print("\n----------------------------------------------------------------------------\n")

while True:
    G = nx.Graph()
    G0 = nx.Graph()
    
    nodes = input("\tVertices: ").split()
    
    edges = []
    
    for i in range(len(nodes)):
        G.add_node(nodes[i])
        G0.add_node(nodes[i])
        
    print("\n    Aristas: ")
    
    i=1
    while True:
       e = input("\t     e"+str(i)+": ").split()
       i+=1
       if(len(e)==0):
           break
       edges.append(e)
       
    for i in range(len(edges)):
        G.add_edge(edges[i][0],edges[i][1])
    
    print()        
    print("    Grafo ingresado: ")

    nx.draw(G, with_labels=True,font_color='white',font_size=20, node_size=1000)
    
    plt.show()
     
    while True:
        fin = input("\n\tEl grafo mostrado es el deseado?   Seleccione 1 o 0\n\n\t   1. SI   0. NO\n\n\t   Seleccion: ")
        
        if(fin=='0' or fin=='1'):
            break
        
    if(fin=='0'):
        print("\n----------------------------------------------------------------------------\n")
    elif(fin=='1'):
        break

#########################################  
#Permutaciones de los nodos

set0 = set(nodes)

a = it.permutations(set0, len(nodes))

per = []

for w in a:
    per.append(list(w))

######################################### 

print("\n\tGRUPO DE AUTOMORFISMOS\n")

ans = []

for l in range(len(per)):
    
    #Gtemp = G0
    etemp = []
    
    for i in range(len(edges)):
        etemp.append([])
        for j in range(2):
            etemp[i].append(edges[i][j])
          
    #etemp = [['1', '4'], ['2', '4'], ['3', '4']]
    #etemp = [['1', '2'], ['1', '3'], ['2', '4'],['3', '4'],['3', '5'],['4', '6'],['5', '6']]
    #etemp = [['1', '2'], ['1', '3'], ['3', '4'],['4', '5'],['4', '6'],['5', '6']]
    ntemp = per[l]  
    
    for i in range(len(etemp)):
        for j in range(2):
            etemp[i][j] = ntemp[nodes.index(etemp[i][j])]
            
    
    #for i in range(len(etemp)):
    #    Gtemp.add_edge(etemp[i][0],etemp[i][1])
        
    
    for i in etemp:
        i = i.sort()
        
    for i in edges:
        i = i.sort()
    
    edges.sort()
    etemp.sort()
          
    if(etemp==edges):
        ans.append(per[l])

ans.sort()
               
for i in range(len(ans)):
    for j in range(len(ans[i])):
        ans[i][j]=int(ans[i][j])

print("Respuesta: "+str(ans))
