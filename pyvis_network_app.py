import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
from pyvis.network import Network

df_characters = pd.read_csv('data/vonnegut_characters_ver2.csv')
st.title('Kurt Vonnegut\'s characters network')

G = nx.from_pandas_adjacency(df_characters.set_index('Персонаж'))

scale = 2.5
d = dict(G.degree)

#Updating dict
d.update((x, scale*y) for x, y in d.items())

#Setting up size attribute
nx.set_node_attributes(G, d, 'size')

net = Network(notebook=True, height='1200px', width='900px')
net.from_nx(G)

# Save and read graph as HTML file (on Streamlit Sharing)
try:
   path = '/tmp'
   net.save_graph(f'{path}/pyvis_graph.html')
   HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')
# Save and read graph as HTML file (locally)
except:
    path = '/html_files'
    net.save_graph(f'{path}/pyvis_graph.html')
    HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

components.html(HtmlFile.read(), height=1600, width=900)