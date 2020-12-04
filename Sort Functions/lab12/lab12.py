#Mario Pendleton
#cs303
#lab11

import json
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
    
    def addEdge(self,u,v):
        u.addNeighbor(v)
    
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
a = Node(13)
b = Node(0)
c = Node(4)
d = Node(9)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(11)
k = Node(1)
l = Node(2)
m = Node(3)
n = Node(12)
o = Node(10)
p = Node(8)

b.addNeighbors([e,k,l,f])
c.addNeighbor(m)
d.addNeighbors([n,o,h])
e.addNeighbors([c,m])
f.addNeighbor(c)
g.addNeighbor(p)
h.addNeighbor(n)

a.printNode()
b.printNode()
c.printNode()
d.printNode()
e.printNode()
f.printNode()
g.printNode()
h.printNode()
k.printNode()
l.printNode()
m.printNode()
n.printNode()
o.printNode()
p.printNode()

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
newGraph.addVertices([a,b,c,d,e,f,g,h,k,l,m,n,o,p])
print(newGraph.graph)
print("\na's Neighbors",a.getNeighbors())
newGraph.DFS()
a.printNode()
b.printNode()
c.printNode()
d.printNode()
e.printNode()
f.printNode()
g.printNode()
h.printNode()
k.printNode()
l.printNode()
m.printNode()
n.printNode()
o.printNode()
p.printNode()
print("DFSQ:",newGraph.Q)



print("\n**************** Files to Graph Test **********************")
fileGraph = Graph()
path = "tinyG.txt"
path1 = "tinyDG.txt"
path2 = "mediumG.txt"
fileGraph.loadNodes(path2)
fileGraph.DFS()
print("DFSQ:",fileGraph.Q)


######################## Start Timer ##############################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")






