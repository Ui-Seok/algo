from csv import reader
from gc import isenabled


a = eval("6528-*2/+") # 후위표기법
print(a)
print(6+5*(2-8)/2)

'''연결 Queue
class Node:
    def __init__(self, item, n = None):
        self.item = item
        self.next = n

def enQueue(item):
    global front, rear
    newNode = Node(item)
    if front == None:
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def isEmpty():
    return front == None

def deQueue():
    global front, rear
    if isEmpty():
        print("Queue_Empty")
        return None
    
    item = front.item
    front = front.next
    if front == None:
        rear = None
    return item

def Qpeek():
    return front.item

def printQ():
    f = front
    s = ""
    while f:
        s += f.item + ""
        f = f.next
    return s

front, rear = None, None

enQueue('A')
enQueue('B')
enQueue('C')
printQ()
print(deQueue)
print(deQueue)
print(deQueue)
'''