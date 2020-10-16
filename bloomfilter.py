
# simple hash function
class Hash:
    def __init__(self, cap, seed):
        self.cap = cap
        self.seed = seed
    
    def hash(self, value):
        ret = 0
        for i in range(len(value)):
            ret += self.seed * ret + ord(value[i])
        return ret % self.cap


class BloomFilter:
    def __init__(self, size):
        self.size = size
        # k = ln(2)* m/n, k is number of hash functionm, n is the number of data, m is the size of bitarray
        self.seeds = [5, 7, 11, 13, 31, 37, 61]
        self.bitarray = [0] * self.size
        self.hashFunc = []

        # init hash functions
        for seed in self.seeds:
            self.hashFunc.append(Hash(self.size, seed))
    
    def insert(self, value):
        for fn in self.hashFunc:
            loc = fn.hash(value)
            self.bitarray[loc] = 1
    
    def is_contained(self, value):
        if value == None:
            return False
        
        for fn in self.hashFunc:
            loc = fn.hash(value)
            if self.bitarray[loc] == 0:
                return False
        
        # may contains the target
        return True
