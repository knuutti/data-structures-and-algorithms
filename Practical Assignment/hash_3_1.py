from math import sqrt
import time

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
        for i in range(0, self.M):
            node = self.T[i]
            while True:
                if node:
                    print(node.key, end=" ")
                    if node.next:
                        node = node.next
                    else: 
                        break
                else:
                    break
            print()

    def analyse(self) -> None:
        lengths = []
        empty = 0
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

        mean = sum_of_lengths/nodes
        help_sum = 0
        for length in lengths:
            help_sum += (length-mean)**2
        std = sqrt(help_sum/nodes)

        print(f"\nAnalysis for data distribution ( M = {self.M} ):\n")
        print("Analysing the lengths of the linked lists inside the hash table")
        print(f"Mean: {mean}")
        print(f"Standard deviation: {std}\n")
        print(f"Empty nodes: {empty}\n")
        return


if __name__ == "__main__":

    time_start = time.time()

    nodes = 0
    overflow_keys = 0

    table = HashTable(10000)

    time_table = time.time() - time_start
    print(f"Time spent making the table: {time_table}")

    overflow = 0

    eng_words = open('words_alpha.txt', 'r')
    while True:
        line = eng_words.readline()
        if len(line) < 1:
            break
        else:
            v = table.insert(line.rstrip('\n'))
            if v:
                overflow += 1

    eng_words.close()

    time_insert = time.time() - time_table - time_start
    print(f"Time spent inserting: {time_insert}")

    common = 0

    fin_words = open('kaikkisanat.txt', 'r', encoding="utf-8")
    while True:
        line = fin_words.readline()
        if len(line) < 1:
            break
        else:
            if table.search(line.rstrip('\n')):
                common += 1
    fin_words.close()

    time_search = time.time() - time_insert - time_table - time_start
    print(f"Time spent searching: {time_search}")

    print(f"Common words: {common}")

    table.analyse()
