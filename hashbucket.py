class HashBucket:
    def __init__(self, M, B):
        self.M = M              # table size
        self.B = B            # bucket size
        self.T = [None] * M     # table
        self.O = [None] * M     # overflow

    def insert(self, x):
        i = hash(self.B, x)
        j = i*int(self.M/self.B)
        while True:
            if self.T[j] == x:
                return
            elif self.T[j] == None or self.T[j] == "[DEL]":
                self.T[j] = x
                print(j)
                return
            elif j == (i+1)*(self.M/self.B) - 1: # if on the last slot of the bucket
                print(f"bucket full ({j})")
                break
            else:
                j += 1
            
        for k in range(len(self.O)):
            if self.O[k] == x:
                break
            elif self.O[k] == None or self.O[k] == "[DEL]":
                self.O[k] = x
                print(f"overflow {k}")
                break
            else:
                k += 1
    
    def delete(self, x):
        i = hash(self.B, x)
        j = i*int(self.M/self.B)
        while True:
            if self.T[j] == None:
                return
            elif self.T[j] == x:
                self.T[j] = "[DEL]"
                return
            elif j == (i+1)*(self.M/self.B) - 1: # if on the last slot of the bucket
                break
            else:
                j += 1
            
        for k in range(len(self.O)):
            if self.O[k] == x:
                self.T[j] = "[DEL]"
                return
            elif self.O[k] == None:
                break
            else:
                k += 1

    def print(self):
        for x in self.T: # actual table
            if x != None and x != "[DEL]":
                print(f"{x} ", end="")
        for y in self.O: # overflow
            if y != None and y != "[DEL]":
                print(f"{y} ", end="")
        print()

def hash(B, data):
    sum = 0
    for i in range(0,len(data)):
        sum = sum + ord(data[i])
    return sum % B

if __name__ == "__main__":
    table = HashBucket(10, 5)
    table.insert("dog")
    table.insert("cat")
    table.insert("bird")
    table.insert("worm")
    table.insert("fish")
    table.insert("cow")
    table.insert("wolf")
    table.insert("fox")
    table.insert("seal")
    table.insert("fly")

    table.print()