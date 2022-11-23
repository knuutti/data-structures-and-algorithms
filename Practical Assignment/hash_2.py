class Node:
    def __init__(self, key, next):
        self.key = key
        self.next = next

class HashTable:
    def __init__(self, M):
        self.M = M             
        self.T = [None] * M    

    # Method for inserting a key value to the hash table
    def insert(self, value) -> None:
        i = self.hash(value)

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

        return 

    # Method for searching whether the given key value exists in the hash table
    def search(self, value) -> bool:
        i = self.hash(value)
        inTable = False

        if self.T[i]:
            node = self.T[i]
            while True:
                if node.key == value:
                    inTable = True
                    break
                elif node.key == None:
                    break
                elif node.next == None:
                    break
                else:
                    node = node.next

        return inTable

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
        data = str(data)

        sum = 0 
        mul = 1
        for i in range (0,len(data)):
            if i % 4 == 0:
                mul = 1
            else:
                mul = mul * 256
            sum += ord(data[i]) * mul
        
        return sum % self.M

    # Method for presenting the hash table
    def print(self) -> None:
        print("Index\tNodes")
        for i in range(0, self.M):
            node = self.T[i]
            print(f"{i}\t", end="")
            while True:
                if node:
                    print(node.key, end=" ")
                    if node.next:
                        node = node.next
                        continue
                break
            print()
        return


if __name__ == "__main__":
    table = HashTable(3)

    insert_keys = [12, 'hashtable', 1234, 4328989, 'BM40A1500', -12456, 'aaaabbbbcccc']
    for key in insert_keys:
        table.insert(key) 
    
    search_keys = [-12456, 'hashtable', 1235]
    for key in search_keys:
        print(table.search(key))

    delete_keys = ['BM40A1500', 1234, 'aaaabbbbcccc']
    for key in delete_keys:
        table.delete(key)
    table.print()
