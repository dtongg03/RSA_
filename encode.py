import MyMath
import MyBase

def getPublicKey(file):
    with open(file, "r", encoding='utf-8') as fi:
        n = int(fi.readline())
        e = int(fi.readline())
    return n, e

def getPlaintext(file):
    with open(file, "r", encoding='utf-8') as fi:
        P = fi.read()
    return P

def convertStringToInt(P, base):
    R = []
    for i in P:
        c = str(ord(i))
        while len(c) < base:
            c = '0' + c  # Đảm bảo mã hóa đúng độ dài
        R.append(c)
    return R

def createBigInt(R, size_n):
    A = []
    x = ""
    for i in R:
        if len(x) + len(i) >= size_n:  # Tối ưu mã hóa nhiều kí tự nhất có thể
            A.append(int(x))
            x = ""
        x += i
    if x:  # Đảm bảo thêm số cuối cùng nếu có
        A.append(int(x))
    return A

def encode(n, e, P, file):
    with open(file, "w", encoding='utf-8') as fo:
        C = ""
        R = convertStringToInt(P, 4)
        A = createBigInt(R, len(str(n)))
        for i in A:
            M = MyMath.powMod(i, e, n)
            M = MyBase.toBase(M, 64)
            C += M + ' '
            fo.write(M + ' ')
    return C

def main():
    n, e = getPublicKey("Data/PublicKey.txt")
    P = getPlaintext("Data/Plaintext.txt")
    C = encode(n, e, P, "Data/Ciphertext.txt")
    #print(C)

main()
