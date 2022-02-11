from math import *
from functools import *

def makeHammingCodeSEC(inp: str) -> str:
    """
        Returns a Hamming code for an input string
    """
    inp = inp[::-1]
    d = len(inp)
    r = ceil(log2(d))
    while 2**r < d+r+1:
        r += 1
    a = []
    ps = []
    p_ix = []
    for x in range(r):
        ps.append([])
    it = iter(inp)
    d_ix = []
    for i in range(d+r):
        if i == 0 or i-1 == 0:
            a.append([])
            p_ix.append(i)
            continue
        if isPowerOfTwo(i+1):
            a.append([])
            p_ix.append(i)
        else:
            a.append(next(it))
            d_ix.append(i)
    for i in d_ix:
        ix = i+1
        for p in getBinaryPartition(ix):
            ps[p].append(i)
    it = iter(p_ix)
    for i in range(len(p_ix)):
        curr = ps[i]
        my_xor = listXOR([a[j] for j in curr])
        a[p_ix[i]] = my_xor
    ret = ""
    for i in range(len(a)-1, -1, -1):
        ret += str(a[i])
    return ret
    
    
def makeHammingCodeSECDED(inp: str) -> str:
    hamm = makeHammingCodeSEC(inp)
    p0 = listXOR([hamm[i] for i in range(len(hamm))])
    
    return hamm + str(p0)

    
        
def listXOR(li: list) -> int:
    return reduce(lambda x, y: x ^ y, list(map(lambda x: int(x), li)))

    
    
    
def getBinaryPartition(x: int) -> list:
    """
        Returns all indices that are '1' in binary reresentation of x as a list        
    """
    ret = []
    max = floor(log2(x))
    for i in range(max+1):
        # 0010 ~> 0010 >> i ~> 001 % 2 == 0 ? append(i) : pass
        if((x // 2**i) % 2 != 0):
            ret.append(i)
    return ret
    
def isPowerOfTwo(x: int) -> bool:
    """
        Returns whether x is a power of 2
    """
    return x & (x-1) == 0
    


