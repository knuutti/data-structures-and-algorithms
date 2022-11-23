class Node:
    def __init__(self, key, next):
        self.key = key
        self.next = next

class HashTable:
    def __init__(self, M):
        self.M = M             
        self.T = [None] * M    

    # Method for inserting a key value to the hash table
    def insert(self, value) -> bool:
        i = self.hash(value)
        new = False

        if self.T[i]:
            node = self.T[i]

            while True:
                if node.key == None:
                    node.key = value
                    break
                elif node.next == None:
                    node.next = Node(value, None)
                    break
                else:
                    node = node.next 
        else:
            self.T[i] = Node(value, None)
            new = True

        return new

    # Method for searching whether the given key value exists in the hash table
    def search(self, value) -> bool:
        i = self.hash(value)

        if self.T[i]:
            node = self.T[i]
            while True:
                if node.key == value:
                    return True
                elif node.key == None:
                    break
                elif node.next == None:
                    break
                else:
                    node = node.next

        return False

    # Method for removing a key value from hash table
    def delete(self, value) -> None:
        i = self.hash(value)
        if self.T[i]:
            node = self.T[i]
            if node.key == value:
                self.T[i] = node.next
                return

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
    def hash(self, data) -> int:
        sum = 0
        data = str(data)
        for i in range(0,len(data)):
            sum = sum + ord(data[i])

        return sum % self.M
        