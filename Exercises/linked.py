class Node:
    def __init__(self,element,next):
        self.element = element
        self.next = next

    def getElement(self):
        return self.element

    def getNext(self):
        return self.next

    def setElement(self,newElement):
        self.element = newElement

    def setNext(self,newNext):
        self.next = newNext

class LinkedList:

    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.len = 0

    def append(self, element):
        temp = Node(None,None)
        last = self.tail
        last.setNext(temp)
        last.setElement(element)
        self.tail = temp
        self.len += 1

    def print(self):
        current = self.head.getNext()
        string = ""
        while current.getNext() != None:
            string = string + str(current.getElement())
            current = current.getNext()
            if current.getElement() != None:
                string = string + " -> "
        print(string)

    def insert(self,element,index):
        current = self.head.getNext()

        for i in range(index):
            current = current.getNext()

        current.setNext(Node(current.getElement(), current.getNext()))
        current.setElement(element)
    
    def index(self,element):
        current = self.head.getNext()
        index = 0

        while current.getNext() != None:
            if current.getElement() == element:
                return index
            index += 1
            current = current.getNext()
        return -1

    def delete(self,index):

        current = self.head.getNext()

        for i in range(index):
            current = current.getNext()
            if current == self.tail:
                return
        
        current.setElement(current.getNext().getElement())
        if current.getNext() == self.tail:
            self.tail = current
            
        current.setNext(current.getNext().getNext())
        self.len -= 1






if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()           # 1 -> 3
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()           # 15 -> 1 -> 10 -> 3
    print(L.index(1))   # 1
    L.delete(0)
    L.print()           # 1 -> 10 -> 3