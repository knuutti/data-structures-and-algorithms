from math import sqrt
import time

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

            # Other comparisons happen in the loop, if the key is found then the path to the 
            # node (in the previous node) is replaced
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

    # Method for analysing the data distribution in the table
    def analyse(self) -> None:
        lengths = []
        empty = 0

        # Looping through each index value in the table and calculating the amount of nodes
        for node in self.T:
            length = 0
            while True:
                if node:
                    length += 1
                    node = node.next
                else:
                    break
            lengths.append(length)
            if length == 0:
                empty += 1
        
        sum_of_lengths = sum(lengths)
        nodes = len(lengths)

        # Calculating mean of lengths and standard deviation
        mean = sum_of_lengths/nodes
        help_sum = 0
        for length in lengths:
            help_sum += (length-mean)**2
        std = sqrt(help_sum/nodes)

        print("\n","*" *30)
        print(f"Analysis for data distribution ( M = {self.M} ):\n")
        print("Analysing the lengths of the linked lists inside the hash table")
        print(f"\tMean: {mean:.4f}")
        print(f"\tStandard deviation: {std:.4f}")
        print(f"\nEmpty slots in the table: {empty}\n")

        return


if __name__ == "__main__":

    time_start = time.time()

    # Creating the table
    table = HashTable(100000)
    time_table = time.time() - time_start
    print(f"Time spent making the table: {time_table:.4f}s")


    # Storing the English words to the table
    english_words_file = open('words_alpha.txt', 'r')
    english_words = english_words_file.readlines()
    english_words_file.close()

    for word in english_words:
        table.insert(word.rstrip('\n'))

    time_insert = time.time() - time_table - time_start
    print(f"Time spent inserting: {time_insert:.4f}s")


    # Finding the common words from the list of Finnish words
    finnish_words_file = open('kaikkisanat.txt', 'r', encoding="utf-8")
    finnish_words = finnish_words_file.readlines()
    finnish_words_file.close()
    
    common_words = 0
    for word in finnish_words:
        if table.search(word.rstrip('\n')):
                common_words += 1

    time_search = time.time() - time_insert - time_table - time_start
    print(f"Time spent searching: {time_search:.4f}s")


    # Printing the answer (common words)
    print(f"\nCOMMON WORDS: {common_words}")


    # Analysis of the table structure
    table.analyse()
