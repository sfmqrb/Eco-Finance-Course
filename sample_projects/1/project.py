#_____import_______
import sys
import pytse_client as tse
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

#_____func________
class Loader():
    an=[]
    i=0
    num=0
    def __init__(self, num):
        for i in range(1, num+1):
            space = num - i
            bar=(i*'█')+(space*' ')
            self.an.append(bar)
        self.num = num
    def fill(self):
        s = self.an[self.i]
        sys.stdout.write("\r| " + s + " | loading...")
        sys.stdout.flush()
        self.i += 1
    def finish(self):
        sys.stdout.write("\r| "+self.num*'█'+" | loading... done!")
        sys.stdout.flush()
        print('\n')
def cut(string,char):
    listX=[]
    fromIndex=0
    string=string+char
    for toIndex in range(len(string)):
        i=string[toIndex]
        if i==char:
            listX.append(string[fromIndex:toIndex])
            fromIndex=toIndex+1
    return listX
def public_stock(inc): return True if "عام" in inc else False
def shareholders(name):
    ticker=tse.Ticker(name)
    data_frame=ticker.shareholders
    inc=list(filter(public_stock, data_frame.shareholder))
    targets=[]
    for target in inc:
        cats=cut(target,'-')[0]
        targets.append(cats[5:])
    return targets
def cut2(a):
    a=cut(a,"\u200c")
    b=""
    for i in range(len(a)):
        b=b+" "+a[i]
    return b[1:]
def find(stock,logo,a):
    ind=stock.index(a)
    return logo[ind]
def read_exel(name):
    df = pd.read_excel(name)
    stock=[]
    logo=[]
    for i , row in df.iterrows():
        a=list((row))
        a[1]=cut2(a[1])
        stock.append(a[1])
        logo.append(a[0])
    return stock,logo
def arabic(text):
    text=text.split()
    if len(text)>1:
        text.reverse()
    b=""
    for i in text:
        a=get_display(arabic_reshaper.reshape(i))
        b=b+" "+a
    return b

#______main______
l=Loader(23)
stock , logo=read_exel("stock.xlsx")
l.fill()
shareholder=[]
names_of_stock=[]
for i in range(len(logo)):
    try:
        shareholder.append(shareholders(logo[i]))
        names_of_stock.append(stock[i])
    except:
        pass
    if i%6==0:
        l.fill()
l.finish()
del l

G = nx.petersen_graph()
G = nx.Graph()
for i in range (len(names_of_stock)) :
    name=find(stock,logo,names_of_stock[i])
    G.add_node(arabic(name))
    for j in shareholder[i] :
        name_st=find(stock,logo,names_of_stock[i])
        G.add_edge(arabic(name_st),arabic(j))
plt.figure(figsize=(100,100))
#nx.draw(G, with_labels=True,font_family="Tahoma", font_weight='bold')
pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_color="#ffffff")
nx.draw_networkx_edges(G,pos,edgelist=G.edges(data=True),width=2)
nx.draw_networkx(G,pos,arrows=True,font_size=24,font_family='Tahoma')
plt.axis('off')
plt.show()
#nx.draw(G, with_labels=True, font_weight='bold')
input()
