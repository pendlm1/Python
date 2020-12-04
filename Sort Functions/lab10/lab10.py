#Mario Pendleton
#cs303
#lab8

import json
import csv
from time import process_time

class Node:

    def __init__(self, key, data):
        self.key = int(key)
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = None
    
    def getKey(self):
        return self.key
    
    def getData(self):
        return self.data
        
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getParent(self):
        return self.parent
    
    def getColor(self):
        return self.color
        
        
    def printNode(self):
        print("Key:", self.key, "Data:", self.data, "Left:", self.left, "Right:", self.right, "Parent:", self.parent, "Color:",self.color)
        
class Tree():

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
            node.color = "black"
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
        node.left = None
        node.right = None
        node.color = "red"
        self.insertFixUp(node)

    def insertFixUp(self,node):
        try:
            while node.parent.color == "red":
                if node.parent == node.parent.parent.left: #Uncle
                    y = node.parent.getParent().getRight()
                    if y.color == "red":
                        node.getParent().color = "black"
                        y.color = "black"
                        node.parent.getParent().color = "red"
                        node = node.parent.getParent()
                    
                    else:
                        if node == node.parent.right:
                            node = node.parent
                            self.leftRotate(node)
                        node.parent.color = "black"
                        node.parent.parent.color = "red"
                        self.rightRotate(node.parent.parent)
                else:
                    y = node.parent.getParent().getLeft()
                    if y.color == "red":
                        node.parent.color = "black"
                        y.color = "black"
                        node.parent.parent.color = "red"
                        node = node.parent.parent
                    else:
                        if node == node.parent.left:
                            node = node.parent
                            self.rightRotate(node)
                        node.parent.color = "black"
                        node.parent.parent.color = "red"
                        self.leftRotate(node.parent.parent)
            self.root.color = "black"
            
        except AttributeError:
            pass


    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parnet = x
        y.parnet = x.parent
        if x.p == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y


    def rightRotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
        
            
        
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
        return self.root

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

############################################
    def inOrderTree(self):
        if self.root != None:
            self.inorderTree(self.root)

    def inorderTree(self,node):
        if node != None:
            self.inorderTree(node.left)
            node.printNode()
            self.inorderTree(node.right)
                
######################## Start Timer ##############################

start = process_time()

print("******************* Node Test *************************")

taz = Node(2,"Tazz")
brock = Node(1,"Brock")
dude = Node(3,"Dude")
diamond = Node(4,"Diamond")
love = Node(0,"Love")
joe = Node(5,"Joe")
taz.printNode()
brock.printNode()
dude.printNode()
diamond.printNode()

######################## Tree Test ###############################
print("**************** Node in Tree Test ********************")
newTree = Tree()
newTree.insert(taz)
newTree.insert(brock)
newTree.insert(dude)
newTree.insert(diamond)
newTree.insert(love)
newTree.insert(joe)

taz.printNode()
brock.printNode()
dude.printNode()
diamond.printNode()
print(newTree.searchTree(brock,1))
print(newTree.searchTree(taz,2))
print(newTree.searchTree(dude,3))
print(newTree.searchTree(diamond,4))
print(newTree.searchTree(dude,2)) #Exsiting node wrong key
#print(newTree.searchTree(man,34)) #None exsiting node will crash

print(taz.getKey())
print(taz.getData())
print(taz.getLeft())
print(taz.getRight())
#print(taz.getParent().data)
print(taz.getColor())

print(brock.getKey())
print(brock.getData())
print(brock.getLeft())
print(brock.getRight())
print(brock.getParent().data)
print(brock.getColor())

print(dude.getKey())
print(dude.getData())
print(dude.getLeft())
print(dude.getRight())
print(dude.getParent().data)
print(dude.getColor())


print(dude.parent.color == "red")

print("********************************************")
path = "input.dat.txt"
#path = "UPC.csv"
#path = "UPC_unsorted.csv"
print(newTree.load(path))
print(newTree.isEmpty().color)
newTree.inOrderTree()
#a=newTree.createNodes(path)
#for i in range(0,len(a)-1):
    #print(newTree.searchTree(a[i],a[i].key))
    
######################## Start Timer ##############################
end = process_time()
print('\n Process Time | Start:',start, ",", 'End:',end,'| Total processing time:',end-start,"\n")






