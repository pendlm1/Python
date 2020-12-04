#Mario Pendleton
#cs303
#lab8

import json
import csv
from time import*

class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.next = None
        
        
    def printNode(self):
        print("Key:", self.key, "Data:", self.data, "Left:", self.left, "Right:", self.right, "Parent:", self.parent,"Next:",next)
        
class Tree:
    root = None

    def __init__ (self):
        self.root = None
        
    def insert(self,node):
        y = None
        x  = self.root
        while x != None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
############################################
    def inOrderTree(self):
        if self.root != None:
            self.inorderTree(self.root)
    
    def inorderTree(self,Node):
        if Node != None:
            self.inorderTree(Node.left)
            print (Node.key)
            self.inorderTree(Node.right)
############################################
    def searchTree(self,node,k):
        try:
            if node == None or k == node.key:
                if node.parent == None and node.left == None and node.right==None:
                    return "Key:",node.key,"Data",node.data,"Left:",node.left,"Right:",node.right,"Parent:",node.parent
          
            elif k < node.key:
                return self.searchTree(node.left,k)
            else:
                return self.searchTree(node.right,k)
        except AttributeError:
            print("Error with node")

############################################
    
    def isEmpty(self):
        if self.root == None:
            return True
        else:
            return False

    def emptyTree(self):
        self.root = None
    
    def load(self,path):
        with open(path,"r") as csv_file:
            file = csv.reader(csv_file)
            for line in file:
                node = Node(int(line[0]),str((line[1]+" "+line[2])))
                self.insert(node)
    
    def createNodes(self,path):
        nodes = []
        with open(path,"r") as csv_file:
            file = csv.reader(csv_file)
            for line in file:
                node = Node(int(line[0]),str((line[1]+" "+line[2])))
                nodes.append(node)
        return nodes
                
########################### Hash Map ##############################
class HashMap:
    def __init__(self):
        self.size = 10000
        self.map = [None] * self.size
                    
    def put(self, key, data):
        node = Node(key, data)
        i = (hash(key)&7)
        n = self.map[i]
        if n is None:
            self.map[i] = node
        else:
            self.map[self.linear_probe(key,data)] = node
    
    def linear_probe(self, key, data):
        i = (hash(key)&7)+1
        while self.map[i] != None and self.map[i] != key:
            i = i+1
        return i
    
    def putq(self, key, data):
        node = Node(key, data)
        i = (hash(key)&7)
    
        n = self.map[i]
        if n is None:
            self.map[i] = node
        else:
            self.map[self.quadratic_probe(key,data)] = node
   
    def quadratic_probe(self, key, data):
        i = (hash(key)&7)+1
        while self.map[i] != None and self.map[i] != key:
            i = i*2
        return i
    
    def get(self, key, data):
        start = process_time()
        i = 0 #hash(key)&0
        while self.map[i] != None:
            if self.map[i].key == key and self.map[i].data == data:
                end = process_time()
                print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")
                return "Your entry",[key,data],"index:",i
                
            else:
                i += 1
    
    def load(self,path):
        count= 0
        try:
            with open(path,"r") as csv_file:
                file = csv.reader(csv_file)
                for line in file:
                    self.put(line[0],str((line[1]+" "+line[2])))
                    count += 1
        except IndexError:
            print(count, "Elements were added to the hashtable")
            
    def loadCompare(self,path):
        try:
            with open(path,"r") as csv_file:
                file = csv.reader(csv_file)
                for line in file:
                    print(self.get(line[0],str((line[1]+" "+line[2]))))
        except IndexError:
            pass
        

######################## Start Timer ##############################

start = process_time()
path = "input.dat.txt"
path1 = "UPC.csv"
path2 = "UPC_unsorted.csv"
########################## Testing ################################
print("\n################ Hash Test ########################")
print("hash test",hash("30")&100) #testing hash
print("hash test",hash("30")&7)

print("\n################## Get/Put Test ######################")
hm = HashMap()
hm.put(1, "beans")
hm.put(2, "greens")
hm.put(3, "tomatoes")
hm.put(4, "potatoes")
hm.put(5, "lambs")
hm.put(6, "rams")
hm.put(7, "hogs")
hm.put(8, "dogs")
hm.put(9, "chicken")
hm.put("10", "chicken")
hm.put(11, "rabbit")
hm.put(12, "bunny")
hm.put(13, "turkey")
hm.put(14, "bacon")
hm.put("15", "ham")
hm.put(16, "bread")
hm.put(17, "cheese")
hm.put(17, "cheeses")
hm.put("American", "cheese")

print(hm.get(1, "beans"))
print(hm.get(2, "greens"))
print(hm.get(3, "tomatoes"))
print(hm.get(4, "potatoes"))
print(hm.get(5, "lambs"))
print(hm.get(6, "rams"))
print(hm.get(7, "hogs"))
print(hm.get(8, "dogs"))
print(hm.get(9, "chicken"))
print(hm.get("10", "chicken"))
print(hm.get(11, "rabbit"))
print(hm.get(12, "bunny"))
print(hm.get(13, "turkey"))
print(hm.get(14, "bacon"))
print(hm.get("15", "ham"))
print(hm.get(16, "bread"))
print(hm.get(17, "cheese"))
print(hm.get(17, "cheeses"))
print(hm.get("American", "cheese"))

print("\n################ Map Test ########################")
print(hm.map[0].key, hm.map[0].data) #test map
print(hm.map[8].key, hm.map[8].data) #test map
print(hm.map[2].key, hm.map[2].data) #test map
print(hm.map[4].key, hm.map[4].data) #test map
print(hm.map[10].key, hm.map[10].data) #test map
print(hm.map[15].key, hm.map[15].data) #test map

print("\n################# Probe Test #######################")
print("Linear:",hm.linear_probe("17","cheeses")) #test linear probe
print("Quad:",hm.quadratic_probe("17","cheeses")) #test quad probe

print("\n############### Load and LoadCompare Test ###################")
hm.load(path1)
hm.loadCompare(path)




    
######################## Start Timer ##############################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")






