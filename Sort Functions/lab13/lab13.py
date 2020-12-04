#Mario Pendleton
#cs303
#lab11

import json
import math
import csv
from time import*

class Node:

    def __init__(self, key):
        self.key = key
        self.neighbors = []
        self.parent = None
        self.color = "White"
        self.distance = 0
        self.finish = 0
    
    def addNeighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
        return self.neighbors
    
    def addNeighbors(self,vertices):
        vertices
        for i in range(len(vertices)):
            self.neighbors.append(vertices[i])
    
    def getKey(self):
        return self.key
    
    def getDistance(self):
        return self.distance
    
    def getParent(self):
        return self.parent
    
    def getColor(self):
        return self.color
        
    def getNeighbors(self):
        return self.neighbors
    
    def getFinish(self):
        return self.finish
                
    def printNode(self):
        print("Key:", self.key, "Neighbors:", self.neighbors, "Parent:", self.parent, "Color:",self.color,"Distance:",self.distance,"Finish:",self.finish)
        
####################################################################################

class Graph():

    def __init__ (self):
        self.graph = {}
        self.Q = []
        self.edges = {}
    
    def addVertex(self, v):
        if isinstance(v,Node) and v.key not in self.graph:
            self.graph[v.key] = v
    
    def addNodes(self, v):
        for i in range(0,len(v)):
            self.addVertex(v[i])
                
    def addVertices(self, v):
        for i in range(0,len(v)):
            if isinstance(v[i],Node) and v[i].key not in self.graph:
                self.graph[v[i].key] = v[i]
    
    def addEdge(self,u,v,d):
        self.edges[u,v] = d
        self.Q.append([u,v,self.edges[u,v]])
        
    def printGraph(self):
        for i in sorted(list(self.graph.keys())):
            print(i +str(self.graph[i].neighbors))
    
    def getNode(self,key):
        try:
            return self.graph[key]
        except KeyError:
            return False
    
    def BFS(self,s):
        for u in s.neighbors:
            u.color = "White"
            u.distance = 0
            u.parent = None
        s.color = "Gray"
        s.distance = 0
        s.parent = None
        Q = []
        Q.append(s)
        while Q:
            u = Q.pop(0)
            for v in u.neighbors:
                if v.color == "White":
                    v.color = "Gray"
                    v.distance = u.distance+1
                    v.parent = u
                    Q.append(v)
            u.color = "Black"
            
    def DFS(self):
        for u in self.graph:
            self.getNode(u)
            self.getNode(u).color = "White"
            self.getNode(u).parent = None
        time = process_time()
        for u in self.graph:
            if self.getNode(u).color == "White":
                self.DFSV(self.getNode(u))
    
    def DFSV(self, u):
        time = process_time() + 1
        u.distance = time
        u.color = "Gray"
        for v in u.neighbors:
            if v.color == "White":
                v.parent = u
                self.DFSV(v)
        u.color = "Black"
        time = time+1
        u.finish = time
        self.DFSQ(u.key)
    
    def DFSQ(self,u):
        self.Q.append(u)
    
    def printPath(self,s,v):
        if v == s:
            print(s.key)
        elif v.parent == None:
            print("No path from",s.key,"to",v.key,"exists")
        else:
            self.printPath(s,v.parent)
            print(v.key)
     
    def MSTPrim(self,w,r):
        infin  = 99999
        self.insertionSort(self.Q)
        for u in w.neighbors:
            print(u)
            u.distance = infin
            u.parent = None
        r.distance = 0
        while self.Q:
             u = self.Q.pop(0)
             for v in u[0].neighbors:
                if (u[0],v) in self.edges or (u[1],v) in self.edges and self.edges[u[0],v] < v.distance:
                    v.parent = u[0]
                    v.distance = self.edges[u[0],v]
                                 
    def insertionSort(self,list):
        key = 0
        for j in range(1,len(list)):
            key = [list[j][0],list[j][1],list[j][2]]
            i = j-1
            while i>=0 and list[i][2]> key[2]:
                list[i+1] = list[i]
                i = i-1
                #print(list[i+1][2], key)
                list[i+1] = key
    
    def loadNodes(self, path):
        lst = []
        file = open(path,"r")
    
        for line in file:
            n = line.split()
            if len(n) == 1:
                key = int(n[0])
                node = Node(key)
                if self.getNode(key) == False:
                    node = Node(key)
                    self.addVertex(node)
            if len(n) == 2:
                key = int(n[0])
                v = int(n[1])
                if self.getNode(key) == False:
                    node = Node(key)
                    self.addVertex(node)
                    if self.getNode(v) == False:
                        self.addVertex(Node(v))
                    node.addNeighbor(Node(v))
                if len(n) == 3:
                    key = int(n[0])
                    v = int(n[1])
                    dis = float(n[2])
                    self.addEdge(Node(key),Node(v),dis)
                if self.getNode(key) == False:
                    node = Node(key)
                    self.addVertex(node)
                    if self.getNode(v) == False:
                        self.addVertex(Node(v))
                    node.addNeighbor(Node(v))
                    node.distance = dis
                else:
                    if self.getNode(v) == False:
                        self.addVertex(Node(v))
                    self.getNode(key).addNeighbor(Node(v))
                    

######################## Start Timer ##############################

start = process_time()

print("\n******************* Node Test *************************")
a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(4)
f = Node(5)
g = Node(6)
h = Node(7)


a.addNeighbors([h,e,c])
b.addNeighbors([c,d,f,h])
c.addNeighbors([h,e,c])
d.addNeighbors([g])
e.addNeighbors([h,f])
f.addNeighbors([h])
g.addNeighbors([a,c,e])

a.printNode()
b.printNode()
c.printNode()
d.printNode()
e.printNode()
f.printNode()
g.printNode()
h.printNode()


print("a's Key",a.getKey())
print("a's Distance",a.getDistance())
print("a's Color",a.getColor())
print("a's Parent",a.getParent())
print("a's Neighbors",a.getNeighbors())

######################## Graph Test ###############################
print("\n******************** Graph Test *************************")
newGraph = Graph()
print(newGraph)
print(newGraph.graph)
newGraph.addVertices([a,b,c,d,e,f,g,h])
print(newGraph.graph)
print("\na's Neighbors",a.getNeighbors())

print("\n******************** Edges Test *************************")
newGraph.addEdge(e,f,0.35)
newGraph.addEdge(e,h,0.37)
newGraph.addEdge(f,h,0.28)
newGraph.addEdge(a,h,0.16)
newGraph.addEdge(b,f,0.32)
newGraph.addEdge(a,e,0.38)
newGraph.addEdge(c,d,0.17)
newGraph.addEdge(b,h,0.19)
newGraph.addEdge(a,c,0.26)
newGraph.addEdge(b,c,0.36)
newGraph.addEdge(b,d,0.29)
newGraph.addEdge(c,h,0.34)
newGraph.addEdge(g,c,0.40)
newGraph.addEdge(d,g,0.52)
newGraph.addEdge(g,a,0.58)
newGraph.addEdge(g,e,0.93)
#print(sorted(newGraph.edges))
print((e,f) in newGraph.Q)
#print(newGraph.Q)
newGraph.insertionSort(newGraph.Q)
print(newGraph.Q)
for i in newGraph.Q:
    print(i[0].key,i[1].key,i[2])

#print(newGraph.Q[0][2])

newGraph.MSTPrim(a,h)

print(a.parent.key)
#print(b.parent.key)
print(c.parent.key)
print(d.parent.key)
print(e.parent.key)
print(f.parent.key)
print(g.parent.key)
print(h.parent.key)


print("\n**************** Files to Graph Test **********************")
fileGraph = Graph()
path = "tinyG.txt"
path1 = "tinyDG.txt"
path2 = "mediumDG.txt"
fileGraph.loadNodes(path2)
#fileGraph.MSTPrim(fileGraph.getNode(1),fileGraph.getNode(1))
#print("DFSQ:",fileGraph.Q)


######################## Start Timer ##############################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")






