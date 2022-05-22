#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


G = graphs.RandomGNP(10,.4)
krawedzie = G.edges()

i = 1
for k in krawedzie:
    G.set_edge_label(k[0],k[1],i)
    i+=randint(1,20)




#G = Graph()
#G.add_edges([(2, 3, 4),(0, 1, 10),(0, 2, 6),(0, 3, 5),(1, 3, 15)])
vertices = len(G.vertices())

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])
    
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
    
    
def KruskalMST(vertices, G):
    result = []
    i = 0
    e = 0
    
    G = sorted(G, key=lambda item: item[2])
    parent = []
    rank = []
    
    for node in range(vertices):
        parent.append(node)
        rank.append(0)
        
        
    while e < vertices - 1:
        u, v, w = G[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        print((u,v,w))
        
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
            print("Krawędź została dodana do MST!")
            print(result)
        else:
            print('Krawędź nie została dodana do MST, tworzy cykl!')
    
    minimalny_koszt = 0
    print("Krawędzie w minimalnym drzewie spinającym:")
    for u, v, waga in result:
        minimalny_koszt += waga
        print("%d -- %d == %d" % (u, v, waga))
    print("Waga minimalnego drzewa:", minimalny_koszt)
    

    
    return result   


result = KruskalMST(vertices, G.edges())


plot(G, save_pos = true, edge_labels = True)

listOfLists = result
listOfTuples = []

for list in listOfLists:
    listOfTuples.append(tuple(list))
    






G1 = G.subgraph(edges =listOfTuples)
g1 = plot(G, edge_color = 'red')
g2 = plot(G1,edge_color = 'blue',edge_labels = True,)

show(g1+g2, axes = False)
print('Na niebiesko zostało oznaczone MST')

