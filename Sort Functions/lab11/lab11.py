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
                
    def printNode(self):
        print("Key:", self.key, "Neighbors:", self.neighbors, "Parent:", self.parent, "Color:",self.color,"Distance:",self.distance)
        
####################################################################################

class Graph():

    def __init__ (self):
        self.graph = {}
    
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
                key = str(n[0])
                node = Node(key)
                if self.getNode(key) == False:
                    node = Node(key)
                    self.addVertex(node)
            if len(n) == 2:
                key = str(n[0])
                v = str(n[1])
                if self.getNode(key) == False:
                    node = Node(key)
                    self.addVertex(node)
                    if self.getNode(v) == False:
                        self.addVertex(Node(v))
                    node.addNeighbor(Node(v))
                else:
                    if self.getNode(v) == False:
                        self.addVertex(Node(v))
                    self.getNode(key).addNeighbor(Node(v))
                    

######################## Start Timer ##############################

start = process_time()

print("\n******************* Node Test *************************")
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")

a.addNeighbors([c,b])
b.addNeighbor(d)
b.addNeighbor(a)
c.addNeighbor(e)
c.addNeighbor(a)
d.addNeighbors([f,b])
e.addNeighbors([c,f])
f.addNeighbor(d)
f.addNeighbor(e)


a.printNode()
b.printNode()
c.printNode()
d.printNode()
e.printNode()
f.printNode()
g.printNode()

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
newGraph.addVertex(a)
newGraph.addVertices([b,c,d,e,f])
newGraph.addVertex(g)
print(newGraph.graph)
newGraph.addEdge(a,g)
newGraph.addEdge(g,a)
print("\na's Neighbors",a.getNeighbors())
newGraph.addEdge(b,a)
newGraph.addEdge(b,d)
newGraph.addEdge(d,b)
newGraph.addEdge(d,f)
newGraph.addEdge(f,d)
newGraph.addEdge(f,e)
newGraph.addEdge(e,f)
newGraph.addEdge(e,c)
newGraph.addEdge(c,e)
newGraph.addEdge(c,a)
newGraph.addEdge(a,c)
newGraph.printGraph()
newGraph.BFS(a)
a.printNode()
b.printNode()
c.printNode()
d.printNode()
e.printNode()
f.printNode()
g.printNode()
newGraph.printPath(g,f)

print("\n**************** Files to Graph Test **********************")
fileGraph = Graph()
path = "largeG.txt"
path2 = "mediumG.txt"
fileGraph.loadNodes(path2)

nodeA = fileGraph.getNode("1")
nodeB = fileGraph.getNode("72")


print(isinstance(nodeA,Node))
print(isinstance(nodeB,Node))

for i in range(len(nodeA.neighbors)):
    lvm = []
    lvm.append (nodeA.neighbors[i].key)
    print(lvm)

#nodeA.printNode()
#nodeB.printNode()
#fileGraph.printGraph()
fileGraph.BFS(nodeA)
print("\nthis is nodeA")
nodeA.printNode()
print("\nthis is nodeB")
nodeB.printNode()
fileGraph.printPath(nodeA,nodeB)


######################## Start Timer ##############################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")






