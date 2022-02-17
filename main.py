import random
import timeit
class List_Scanner():
    def __Init__(self):
        self.List = []
    def SCAN(self):
        for i in range(len(self.List)):
            for x in range(i+1, len(self.List)):
                if self.List[i] == self.List[x]:
                    return self.List[i]
    #@profile
    def STOR(self):
        listb = [0]*len(self.List)
        for i in range(len(self.List)):
            if listb[self.List[i]] != 0:
                return self.List[i]
            else:
                listb[self.List[i]] = 1
    def create_rand_List(self):
        self.List = []
        for i in range(1000000):
            pos = random.randint(0, len(self.List))
            self.List.insert(pos, i)
        dupNum = random.randint(0, len(self.List))
        dupPos = random.randint(0, len(self.List))
        self.List.insert(dupPos, dupNum)
        return self.List
hello = List_Scanner()
list = hello.create_rand_List()
print(timeit.timeit(hello.STOR, number=1))
print(timeit.timeit(hello.SCAN, number=1))
