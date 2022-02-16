from math import *
from functools import *
from typing import Any

NO_FLIP  = 0
SEC_FLIP = 1
DED_FLIP = 2

def makeHammingCodeSEC(inp: str) -> str:
    """
        Returns a Hamming code for an input string
    """
    inp = typeMe(inp)
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
    
    
def decodeHammingSEC(inp: str) -> (str, bool):
    """
        Takes a binary input string in Hamming Code, returns a tuple containing the retrieved
        data as binary string and a bool indicating whether a bit flip was detected.
    """
    inp = typeMe(inp)
    l = len(inp)
    num_p = ceil(log2(l))
    # find indices of parity bits (all powers of 2)
    p_ix = [2**i-1 for i in range(num_p)]
    inp = inp[::-1]
    val = inp

    # seperate data bits
    d = "".join([inp[i] for i in range(l-1,0,-1) if i not in p_ix])
    # check whether parity bits match
    enc = makeHammingCodeSEC(d)[::-1]
    if len(enc) != l:
        return None
    # received parity bits
    p1 = [int(inp[i]) for i in p_ix]
    # expected parity bits
    p2 = [int(enc[i]) for i in p_ix]
    # syndrome
    s = [str(p1[i] ^ p2[i]) for i in range(len(p_ix))]
    s = int("".join(s)[::-1], 2)
    # no bit flip
    if s == 0:
        return (d, False)
    # parity flipped
    if s in p_ix:
        return (d, True)
    # data flipped
    s -=1
    inp = val[:s] + flip(val[s]) + val[s+1:]
    d = "".join([inp[i] for i in range(l-1,0,-1) if i not in p_ix])
    return (d, True)
    

def decodeHammingSECDED(inp: str) -> (str, bool, bool):
    """
        Takes a binary input string in Hamming Code SEC/DED, returns a tuple containing the
        retrieved data as binary string and an integer indicating, whether
            0 := no bit flip was detected
            1 := single bit flip was detected and corrected
            2 := double bit flip was detected ( => data string is faulty)
    """
    inp2 = inp[:-1]
    print(inp, inp2)
    dec = decodeHammingSEC(inp2)
    if listXOR(inp):
        return (dec[0], SEC_FLIP)
    if dec[1]:
        return (dec[0], DED_FLIP)
    return (dec[0], NO_FLIP)
  
    
    
def makeBergerCode(inp: str) -> str:
    r = int(ceil(log2(len(inp) +1)))
    num1 = inp.count("1")
    x = num1 ^ (2**r - 1)
    x = format(x, '0'+str(r)+'b')
    return inp + x



def decodeBerger(inp: str) -> (str, bool):
    l = len(inp)
    r = findCheckLength(l)
    en = makeBergerCode(inp[:-r])
    return (inp[:-r], en == inp)
    

#-------------------------------------------------------------------------------


def flip(a: str):
    if a == "1":
        return "0"
    return "1"


def typeMe(inp: Any) -> str:
    if type(inp) == str:
        return inp
    if type(inp) == int:
        return str(inp)
    raise TypeError("Expected int but found {}".format(type(inp).__name__))
    
    
def findCheckLength(x: int) -> int:
    d = ceil(x/2)
    inter = d
    berger = d + ceil(log2(d+1))
    while berger != x:
        if berger < x:
            d += inter
        if berger > x:
            d-= inter
        berger = d + ceil(log2(d+1))
        inter = ceil(inter/2)
    return x-d

 
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
    
