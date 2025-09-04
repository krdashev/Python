import math


def rearrange(bit_string_32):
    """[summary]
    Regroups the given binary string.

    Arguments:
        bitString32 {[string]} -- [32 bit binary]

    Raises:
    ValueError -- [if the given string not are 32 bit binary string]

    Returns:
        [string] -- [32 bit binary string]
    >>> rearrange('1234567890abcdfghijklmnopqrstuvw')
    'pqrstuvwhijklmno90abcdfg12345678'
    """

    if len(bit_string_32) != 32:
        raise ValueError("Need length 32")
    new_string = ""
    for i in [3, 2, 1, 0]:
        new_string += bit_string_32[8 * i : 8 * i + 8]
    return new_string


def reformat_hex(i):
    """[summary]
    Converts the given integer into 8-digit hex number.

    Arguments:
            i {[int]} -- [integer]
    >>> reformat_hex(666)
    '9a020000'
    """

    hexrep = format(i, "08x")
    thing = ""
    for i in [3, 2, 1, 0]:
        thing += hexrep[2 * i : 2 * i + 2]
    return thing


def pad(bit_string):
    """[summary]
    Fills up the binary string to a 512 bit binary string

    Arguments:
            bitString {[string]} -- [binary string]

    Returns:
            [string] -- [binary string]
    """
    start_length = len(bit_string)
    bit_string += "1"
    while len(bit_string) % 512 != 448:
        bit_string += "0"
    last_part = format(start_length, "064b")
    bit_string += rearrange(last_part[32:]) + rearrange(last_part[:32])
    return bit_string


def get_block(bit_string):
    """[summary]
    Iterator:
            Returns by each call a list of length 16 with the 32 bit
            integer blocks.

    Arguments:
            bit_string {[string]} -- [binary string >= 512]
    """

    curr_pos = 0
    while curr_pos < len(bit_string):
        curr_part = bit_string[curr_pos : curr_pos + 512]
        my_splits = []
        for i in range(16):
            my_splits.append(int(rearrange(curr_part[32 * i : 32 * i + 32]), 2))
        yield my_splits
        curr_pos += 512


def not32(i):
    """
    >>> not32(34)
    4294967261
    """
    i_str = format(i, "032b")
    new_str = ""
    for c in i_str:
        new_str += "1" if c == "0" else "0"
    return int(new_str, 2)


def sum32(a, b):
    return (a + b) % 2**32


def leftrot32(i, s):
    return (i << s) ^ (i >> (32 - s))


def md5me(testString):
    bs = ""
    for i in testString:
        bs += format(ord(i), "08b")
    bs = pad(bs)

    tvals = [int(2**32 * abs(math.sin(i + 1))) for i in range(64)]

    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    s = [
        7,
        12,
        17,
        22,
        7,
        12,
        17,
        22,
        7,
        12,
        17,
        22,
        7,
        12,
        17,
        22,
        5,
        9,
        14,
        20,
        5,
        9,
        14,
        20,
        5,
        9,
        14,
        20,
        5,
        9,
        14,
        20,
        4,
        11,
        16,
        23,
        4,
        11,
        16,
        23,
        4,
        11,
        16,
        23,
        4,
        11,
        16,
        23,
        6,
        10,
        15,
        21,
        6,
        10,
        15,
        21,
        6,
        10,
        15,
        21,
        6,
        10,
        15,
        21,
    ]

    for m in getBlock(bs):
        a = a0
        b = b0
        c = c0
        d = d0
        for i in range(64):
            if i <= 15:
                f = (b & c) | (~b & d)
                g = i
            elif i <= 31:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * i) % 16
            dtemp = d
            d = c
            c = b
            b = (b + leftRotate((a + f + tvals[i] + m[g]) % 2**32, s[i])) % 2**32
            a = dtemp
        a0 = (a0 + a) % 2**32
        b0 = (b0 + b) % 2**32
        c0 = (c0 + c) % 2**32
        d0 = (d0 + d) % 2**32

    digest = reformatHex(a0) + reformatHex(b0) + reformatHex(c0) + reformatHex(d0)
    return digest

def getBlock(bitString):
    currPos = 0
    while currPos < len(bitString):
        currPart = bitString[currPos:currPos + 512]
        mySplits = []
        for i in range(16):
            mySplits.append(int(rearrange(currPart[i * 32:i * 32 + 32]), 2))
        yield mySplits
        currPos += 512

def not32(i):
    iStr = format(i, "032b")
    newStr = ""
    for c in iStr:
        newStr += "1" if c == "0" else "0"
    return int(newStr, 2)

def sum32(a, b):
    return (a + b) % 2**32

def leftRotate(i, s):
    return (i << s) ^ (i >> (32 - s))

def reformatHex(i):
    hexRep = format(i, "08x")
    thing = ""
    for i in [3, 2, 1, 0]:
        thing += hexRep[2 * i:2 * i + 2]
    return thing

def rearrange(bitString32):
    if len(bitString32) != 32:
        raise ValueError("Need length 32")
    newString = ""
    for i in [3, 2, 1, 0]:
        newString += bitString32[8 * i:8 * i + 8]
    return newString

def pad(bitString):
    startLength = len(bitString)
    bitString += "1"
    while len(bitString) % 512 != 448:
        bitString += "0"
    lastPart = format(startLength, "064b")
    bitString += rearrange(lastPart[32:]) + rearrange(lastPart[:32])
    return bitString

testString = input("Enter a string: ")
hashValue = md5me(testString)
print("MD5 hash code: " + hashValue)

