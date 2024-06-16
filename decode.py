import MyMath
import MyBase

def getPrivateKey(file):  # file Privatekey
    with open(file, "r", encoding='utf-8') as fi:
        n = int(fi.readline())
        d = int(fi.readline())
    return n, d

def getCiphertext(file):  # file Ciphertext
    with open(file, "r", encoding='utf-8') as fi:
        C = fi.readline()
        C = C.split(" ")
        C = C[:-1]
    return C

def decode(n, d, C, base, fileOut):  # file PlanintextDecode
    with open(fileOut, "w", encoding='utf-8') as fo:
        P = ""
        for i in C:
            m = MyMath.powMod(MyBase.toInt(i, 64), d, n)
            c = str(m)
            while len(c) % base != 0:
                c = '0' + c
            x = 0
            while x != len(c):
                a = c[x:x+base]
                x += base
                P += chr(int(a))
                fo.write(chr(int(a)))
    return P

def main():
    n, d = getPrivateKey("Data/PrivateKey.txt")
    C = getCiphertext("Data/Ciphertext.txt")
    C = decode(n, d, C, 4, "Data/PlaintextDecode.txt")
    #print(C)

main()
