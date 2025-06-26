# -*- coding: utf-8 -*-

import math
import networkx as nx

path = 'dolphins.txt'#此处更换数据集
G=nx.Graph()
with  open(path) as file:
    for line in file:
        u, v = [int(x) for x in line.split()]  

        G.add_edge(u,v)
k_shell=nx.core_number(G)
nums = G.number_of_nodes() 
maxD=max(dict(G.degree()).values())
maxKshell=max(k_shell.values())
file.close()

pl={}
for u in G.nodes():      
    allpc = 0              
    degreeU = G.degree(u)               
    neighborsU = G.neighbors(u)      
    neiU_set=set(neighborsU) 
    ks=k_shell[u] 
    allpc=degreeU+ks
    
    
    p=0
    for v in neiU_set: 
        pv=0
        pvself=0
        pvn=0
        ksv=k_shell[v]
        ar=math.log10(G.degree(v)) 
        pvself=math.pow(ksv,ar/maxD)
    
        neighborsV = G.neighbors(v)
        neiV_set=set(neighborsV)
        neiUVJ=neiU_set & neiV_set
        neiUVB=neiU_set | neiV_set
        neiUVC=neiV_set - neiUVJ
        for neiVexc in neiUVC:
            if neiVexc is not u:
                pvn=pvn+math.pow(k_shell[neiVexc],math.log10(G.degree(neiVexc))/maxD)
        pv=pvself+pvn
        sp=(1+len(neiUVJ))/nums
        p=p+pv*sp
    pl[u]=allpc+p
print(pl)
sortNum = sorted(pl.items(), key=lambda x: x[1], reverse=True)
                 
nodelist=[]
for key in sortNum:
    nodelist.append(key.__getitem__(0))
print(nodelist) 

f =open('.\outputdata\MNEN_'+path, "w+")
for key,val in sortNum:
   f.write(str(key)+'\t'+str(val)+"\n")   

f.close()             

nodelist1=[]
sortNum1 = sorted(pl.items(), key=lambda x: x[0], reverse=False)

for key in sortNum1:
    nodelist1.append(key.__getitem__(0))
print(nodelist1)

f =open('.\outputdata\MNEN_1'+path, "w+")
for key,val in sortNum1:
   f.write(str(key)+'\t'+str(val)+"\n")   

f.close()    