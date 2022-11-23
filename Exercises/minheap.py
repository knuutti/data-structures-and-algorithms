class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def parent(self,index):
        return (index-1)//2

    def leftChild(self,index):
        return index*2+1

    def rightChild(self,index):
        return index*2+2

    def hasOneChild(self, index):
        return index*2+2 == self.size

    def isLeaf(self, index):
        return index*2+2 > self.size

    def push(self, key):
        self.heap.append(key)
        self.size += 1
        self.push_help(self.size-1)
        return

    def push_help(self,index):
        if self.heap[index] < self.heap[self.parent(index)] and index > 0:
            self.swap(index, self.parent(index))
            self.push_help(self.parent(index))
        return 

    def print(self):
        for node in self.heap:
            print(node, end = " ")
        print()
        return

    def pop(self):
        temp = self.heap[0] # saves the smallest key
        self.swap(0,self.size-1)
        del self.heap[self.size-1]
        self.size -= 1
        self.pop_help(0)
        return temp

    def pop_help(self,index):

        if self.isLeaf(index):
            return

        if self.hasOneChild(index):
            if self.heap[self.leftChild(index)] < self.heap[index]:
                self.swap(index, self.leftChild(index))
        else:
            if self.heap[self.leftChild(index)] < self.heap[index] and self.heap[self.rightChild(index)] > self.heap[self.leftChild(index)]:
                self.swap(index, self.leftChild(index))
                self.pop_help(self.leftChild(index))
            elif self.heap[self.rightChild(index)] < self.heap[index]:
                self.swap(index, self.rightChild(index))
                self.pop_help(self.rightChild(index))
        return

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]



if __name__ == "__main__":
    items = [4, 8, 6, 5, 1, 2, 3]
    heap = MinHeap()
    [heap.push(key) for key in items]
    heap.print()        # 1 4 2 8 5 6 3 
    print(heap.pop())   # 1
    heap.print()        # 2 4 3 8 5 6 
