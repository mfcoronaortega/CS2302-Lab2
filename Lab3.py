#Course: CS 2302 Data Structures | Spring 2019
#Author: Maria Fernanda Corona Ortega
#Assignment: Lab 3
#Instructor: Olac Fuentes
#Purpose of Code: The purpose of this code is to explore basic Btrees and 
#operations regarding basic BTree functions
#through plotting and recursion
#Last Modification: 4/3/2019 8:40pm
import matplotlib.pyplot as plt
import timeit
import random

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')

#######################################################################################################################

def PlotTree(T):#FIXME
    fig, ax = plt.subplots()
    ax = fig.add_subplot(111)
    x = 0
    y = 0
    
    if T is not None:
        InOrderD(T.right,space+'   ')
        circle = plt.Circle((x, y), radius=5)
        ax.add_patch(circle)
        items = ax.annotate(T.item, xy=(x, y), fontsize=20, ha="center")
        x = x + 10
        y = y - 10
        InOrderD(T.left,space+'   ')
        
    ax.axis('off')
#    ax.set_aspect('equal')
    ax.set_aspect(1.0)
    
    ax.autoscale_view()
    
    plt.show()

def Search(T,k):#Done Iterative version of the search operation.
    # Returns the address of k in BST, or None if k is not in the tree
    while T is not None:
        if T.item < k:
            T = T.right
        if T.item > k:
            T = T.left
        else:
         return T
            
def Balanced(L): #Done Building a balanced binary search tree
    #height on left and right sides of tree cannot differ by more than 1
    if not L:
        return None
    m = len(L)//2
    T = BST(L[m])
    T.left = Balanced(L[:m])
    T.right = Balanced(L[m+1:])
    
    return T

def IntoList(T,L):#Done Extracting the elements in a binary search tree into a sorted list.
    if T is not None:
        IntoList(T.left, L)
        L.append(T.item)
        IntoList(T.right, L)
    return L

def PrintByDepth(T): #FIXME
    if T  is not None:
        return 
        


###############################################################################
        
T = None
A= []

##############################TESTING SEARCH METHOD############################

#size = 100
#
#for i in range(50):
#    A.append(random.randint(0, size))
#
#for a in A:
#    T = Insert(T,a)
#    
#InOrder(T)
#print()
#
#InOrderD(T,'')
#print()
#
#start = timeit.default_timer()
#
#print(Search(T,A[len(A)//2]))
#
#stop = timeit.default_timer()
#
#print('Time 1: ', stop - start)  

#
#start = timeit.default_timer()
#
#print(Search(T,size+1))
#
#stop = timeit.default_timer()
#
#print('Time 2: ', stop - start)  

############################TESTING BALANCED METHOD############################

#for i in range(50):
#    A.append(i)
#
#start = timeit.default_timer()
#
#T = Balanced(A)
#
#stop = timeit.default_timer()
#
#print('Time: ', stop - start)
#
#InOrder(T)
#print()
#
#InOrderD(T,'')
#print()


############################TESTING INTOLIST METHOD############################

NL=[]
size = 100

for i in range(50):
    A.append(random.randint(0, size))

for a in A:
    T = Insert(T,a)
    
InOrder(T)
print()

InOrderD(T,'')
print()

start = timeit.default_timer()

NL = IntoList(T, NL)

stop = timeit.default_timer()

print('Time: ', stop - start)

print(NL[:])

###############################OTHER METHODS##################################

#PrintByDepth(R)
#PlotTree(T)