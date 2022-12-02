class Node:
    def __init__(self, key, next):
        self.key = key          # data value of the key
        self.next = next        # address to the next node

class HashTable:
    def __init__(self, M):
        self.M = M              # size of the table
        self.T = [None] * M     # the table

    # Method for inserting a key value to the hash table
    def insert(self, value) -> None:

        # Getting the index with the hash function
        i = self.hash(value)

        # if there exists a node already in the table, start from the first one
        if self.T[i]: 
            node = self.T[i]
            while True:

                # empty space -> insert key
                if node.key == None: 
                    node.key = value
                    break

                # dublicate is found -> break the loop without inserting the key
                elif node.key == value: 
                    break

                # next node is not defined -> insert a new node with key value
                elif node.next == None: 
                    node.next = Node(value, None)
                    break

                # iterate to the next node in the linked list
                else:
                    node = node.next 
        
        # if there is no node in the hash table at the given index, create one with the key value
        else:
            self.T[i] = Node(value, None) 

        return

    # Method for searching whether the given key value exists in the hash table
    def search(self, value) -> bool:

        # Getting the index with the hash function
        i = self.hash(value)

        # Only proceed if there is a start node at the given index
        if self.T[i]:
            # Start from the first node
            node = self.T[i]
            while True:
                if node.key == value:
                    # in case the key was found, return True
                    return True
                    
                # Break the loop if we reach the end of the linked list
                elif node.key == None or node.next == None:
                    break
                else:
                    node = node.next

        # in case the value was not found, return False
        return False 

    # Method for removing a key value from hash table
    def delete(self, value) -> None:

        # Getting the index with the hash function
        i = self.hash(value)

        # Only start the search if there is a node located at the given index
        if self.T[i]:
            node = self.T[i]

            # The first comparison happens outside the loop
            if node.key == value:
                self.T[i] = node.next
                return

            # Other comparisons happen in the loop, if the key is found then the path to the node (in the previous node) is replaced
            while True: 
                if not node.next:
                    break

                if node.next.key == value:
                    node.next = node.next.next
                    break
                else:
                    node = node.next

        return

    # Hash function
    def hash(self, key) -> int:
        data = str(key) # converting the input data to string

        sum = 0 
        mul = 1
        for i in range (0,len(data)):
            if i % 4 == 0:
                mul = 1
            else:
                mul = mul * 256
            sum += ord(data[i]) * mul
        
        return sum % self.M
        