import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
import random

# fig, ax = plt.subplots(figsize=(5,5))
# def emitoGraph(G, pos):
#  nx.draw_networkx_nodes(G, pos, node_color = "sandybrown", node_size = 1000)
#  nx.draw_networkx_labels(G, pos, font_size = 10, font_family = 'sans-serif')
#  labels = nx.get_edge_attributes(G, 'weight')
#  nx.draw_networkx_edges(G, pos, edge_color='sandybrown', width=2, arrowstyle= '<|-|>', arrowsize = 20,
#  style='dotted', ax=ax)
#  nx.draw_networkx_edge_labels(G, pos, edge_labels = labels)

# def cargoGraph(G):
#  G.add_weighted_edges_from([('a','b', random.random()),('a','f', random.random()),('b','e',1.2),
#  ('c','e', random.random()),('c','d', random.random()),('e','f',1.15),('f','c', random.random())])
 
# G = nx.Graph()
# cargoGraph(G)
# pos = nx.shell_layout(G)
# emitoGraph(G, pos)
# plt.axis('off')
# plt.show()

# print(f"Número de vértices: {G.order()}\nNúmero de vértices: {len(G)}")
# print(f'Revisamos nodos: {G.nodes} \n')
# print(f"Los enlaces son: {G.edges()}\n\nEl número de enlaces es:{G.number_of_edges()}")
# print(f"\nneighbors() permite ver los nodos vecinos, en este caso de e: {list(G.neighbors('e'))}")
# print("\nsize() devuelve el número de aristas", G.size())

aeropuertos = pd.read_csv('archs/aeropuertos.csv', encoding='latin-1')
df_a = pd.DataFrame(aeropuertos)
df_a.head(5)

vuelos = pd.read_csv("archs/combi_precios.csv", encoding='latin-1')
df_b = pd.DataFrame(vuelos)
df_b.head(5)

DG = nx.DiGraph()
for i in range(0, len(df_a)):
 DG.add_node(df_a.iloc[i]['COD'])
 i = i + 1
for i in range(0, len(df_b)):
 DG.add_edge(df_b.iloc[i]['Origen'], df_b.iloc[i]['Destino'])
 i = i + 1

fig, ax = plt.subplots(figsize=(9,7))
DG.nodes(data=True)
nx.draw(DG, node_color="lightblue", edge_color="gray", font_size=8, width=2, with_labels=True,
 node_size=500)
plt.show()

df_b = df_b.loc[:, ['Origen', 'Destino', 'Precio']]
df_b

DG = nx.DiGraph()
DG.add_weighted_edges_from([tuple(x) for x in df_b.values])
# DG.edges()

DG.get_edge_data('AEP','CNQ')