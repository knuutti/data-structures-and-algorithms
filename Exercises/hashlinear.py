class HashLinear:
    def __init__(self, M):
        self.M = M             
        self.T = [None] * M    

    def insert(self, x):
        i = hash(self.M, x)
        print(f"{x}, yrittää {i}")
        j = i
        while True:
            if self.T[j] == x:
                break
            elif self.T[j] == None or self.T[j] == "[DEL]":
                self.T[j] = x
                break
            elif j == self.M - 1:
                j = 0
            else:
                j += 1
            
            if j == i:
                break
    
    def delete(self, x):
        i = hash(self.M,x)
        j = i
        while True:
            if self.T[j] == None:
                break
            elif self.T[j] == x:
                self.T[j] = "[DEL]" 
                break
            elif j == self.M - 1:
                j = 0
            else:
                j += 1

            if j == i:
                break   

    def print(self):
        for x in self.T:
            if x != None and x != "[DEL]":
                print(f"{x} ", end="")
        print()


def hash(M, data):
    sum = 0
    for i in range(0,len(data)):
        sum = sum + ord(data[i])
    return sum % M


if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1