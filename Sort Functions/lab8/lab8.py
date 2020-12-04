#Mario Pendleton
#cs303
#lab8

import json
import csv
from time import*

class Node:

    def __init__(self, key, data):
        self.key = int(key)
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        
        
    def printNode(self):
        print("Key:", self.key, "Data:", self.data, "Left:", self.left, "Right:", self.right, "Parent:", self.parent)
        
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
                
                
######################## Start Timer ##############################

start = process_time()

print("******************* Node Test *************************")

taz = Node(2,"Tazz")
brock = Node(1,"Brock")
dude = Node(3,"Dude")
diamond = Node(4,"Diamond")
#taz.printNode()
#brock.printNode()
#dude.printNode()
#diamond.printNode()
######################## Tree Test ###############################
print("**************** Node in Tree Test ********************")
newTree = Tree()
#newTree.insert(taz)
#newTree.insert(brock)
#newTree.insert(dude)

#taz.printNode()
#brock.printNode()
#dude.printNode()
#diamond.printNode()
#print(newTree.searchTree(brock,1))
#print(newTree.searchTree(taz,2))
#print(newTree.searchTree(dude,3))
#print(newTree.searchTree(diamond,4))
#print(newTree.searchTree(dude,2)) #Exsiting node wrong key
#print(newTree.searchTree(man,34)) #None exsiting node will crash


print("********************************************")
#path = "input.dat.txt"
#path = "UPC.csv"
path = "UPC_unsorted.csv"
print(newTree.load(path))
#print(newTree.isEmpty())
newTree.inOrderTree()
#a=newTree.createNodes(path)
#for i in range(0,len(a)-1):
    #print(newTree.searchTree(a[i],a[i].key))
    
######################## Start Timer ##############################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")






