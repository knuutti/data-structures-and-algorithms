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
    
    # Creating the table
    table = HashTable(3)

    # Insertion
    insert_keys = [12, 'hashtable', 1234, 4328989, 'BM40A1500', -12456, 'aaaabbbbcccc']
    for key in insert_keys:
        table.insert(key) 
        print(f"\nTable structure after inserting '{key}':")
        table.print()
    
    # Search
    search_keys = [-12456, 'hashtable', 1235]
    for key in search_keys:
        print(f"\nSearching for '{key}':")
        print(table.search(key))

    # Deletion
    delete_keys = ['BM40A1500', 1234, 'aaaabbbbcccc']
    for key in delete_keys:
        table.delete(key)

    # Presenting the table
    print(f"\nTable structure after deletion:")
    table.print()
