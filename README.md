
MyMath - Hàm toán học
  - **powMod(a, b, m)**
    - Ý nghĩa:  Trả về kết quả phép tính `a^b mod m`
    - Kiến thức: **Bình phương liên tiếp**
    - Code:

      ```python
      def powMod(a, b, m):
      	x = []
      	while b != 0:
      		x.append(b & 1)
      		b = b >> 1
      	sz = len(x)
      	po = [a%m]
      	for i in range(1,sz):
      		p = (po[i-1]*po[i-1])%m
      		po.append(p)
      	r = 1
      	for i in range(sz):
      		if(x[i] != 0):
      			r*= po[i]
      			r%= m
      	return r
      ```
  - **GCD(a, b)**
    - Ý nghĩa: Trả về `UCLN(a, b)`
    - Kiến thức: **UCLN(a, b)= UCLN(b, a% b)**, Giải thuật **Euclid**
    - Code:
    ```python
    def GCD(a, b):
    	if b == 0:
    		return a
    	return GCD(b, a%b)
    ```
  - **GCD_extended(a, b)**
    - Ý nghĩa: Trả về 3 số x,y,z thỏa mãn `x*a + y*b = z = UCLN(a, b)`
    - Kiến thức: Giải thuật **Euclid mở rộng**
    - Code:
    ```python
    def GCD_extended(a, b):
    	u1, u2, u3 = 1, 0, a
    	v1, v2, v3 = 0, 1, b
    	while v3 != 0:
    		q = u3//v3
    		t1, t2, t3 = u1 - q*v1, u2 - q*v2, u3 - q*v3
    		u1, u2, u3 = v1, v2, v3
    		v1, v2, v3 = t1, t2, t3
    	return u1, u2, u3
    ```

PrimeTest - Các hàm kiểm tra tính nguyên tố
  - **Fermat(p,x)**:
    - Ý nghĩa: Kiểm tra số p sử dụng định lý Fermat nhỏ với x cơ sở.
    - Kiến thức:
      - Định lý Fermat nhỏ: `a^(p-1) ≡ 1(mod p)` (p: số nguyên tố và a không chia hết cho p)
      - Số giả nguyên tố cơ sở
    - Code:
    ```python
    def Fermat(p,x):
    	for i in range(x):
    		a = sprime[i]
    		if MyMath.powMod(a,p-1,p) != 1:
    			return False
    	return True
    ```
  - **Miller_Rabin(p, x)**:
    - Ý nghĩa: Kiểm tra Miller- Rabin với x cơ sở
    - Kiến thức: n là số nguyên dương lẻ, `n-1 =2^s*m`, n trải qua Miller cơ sở b nếu `b^t ≡ 1 mod n` hoặc `b^((2^j)t) ≡ -1 mod n` với j nào đó 0 ≤ j ≤ s-1
    - Code:

    ```python
    # Q(a,p,m,s) = 1 nếu p trải qua Miller-Rabin cơ sở a
    def Q(a, p, m, s):
    	x = MyMath.powMod(a,m,p)
    	if x == 1:
    		return True
    	for i in range(0,s+1):
    		if x == p - 1:
    			return True
    		x *= x
    		x %= p
    	return False

    def Miller_Rabin(p, x):
    	# x : the number of bases
    	# p - 1 = m*2^s (m is odd)
    	n = p - 1
    	s = 0
    	while n & 1 == 0:
    		n = n >> 1
    		s+= 1
    	m = n
    	for i in range(x):
    		a = sprime[i]
    		if Q(a,p,m,s) == False:
    			return False
    	return True
    ```

Mã hóa RSA
  - **Tạo khóa**
    - Lấy 2 số `p,q`
    - Gắn `n = p*q`, `φ(n) = (p-1)(q-1)`
    - Lấy e sao cho `(e, φ(n)) = 1`
    - Gắn d là nghịch đảo modulo phi của e, xử dụng **GCD_extended**
    ```python
    def getD(e, phi):
    	d = MyMath.GCD_extended(e,phi)[0] #[x,y,z] #d = x
    	if d < 0:
    		d+= phi
    	return d
    ```
    - In kết quả ra file
  - **Mã hóa**
    - Lấy khóa công khai `(n, e)`
    - Lấy bản rõ `P`
    - Chuyển các kí tự trong P về số theo bản mã `UTF-8` tạo thành mảng các số R
    - Ghép các số trong R thành số lớn nhỏ hơn n thành số `Pi` rồi mã hóa nó thành `Ci` với công thức: `Ci ≡ Pi^e mod n`
    ```python
    def encode(n, e, P, file):
    	fo = open(file,"w")
    	C = ""
    	R = convertStringToInt(P, 4)
    	A = createBigInt(R, len(str(n)))
    	for i in A:
    		M = MyMath.powMod(i,e,n)
    		M = MyBase.toBase(M,64)
    		C+= M + ' '
    		fo.write(M+' ')
    	fo.close()
    	return C
    ```
    - In mảng số mới ra file với `cơ số 64`
  - **Giải mã**
    - Lấy khóa bảo mật `(n, d)`
    - Lấy bản mã C trong file chuyển về `cơ số 10`
    - Lấy từ số trong C là `Ci` giải mã được `Pi` với công thức: `Pi ≡ Ci^d mod n`
    - Lấy kết quả tách số rồi chuyển về dạng kí tự
    - In kết quả ra file
    ```python
    def decode(n, d, C, base, fileOut): # file PlanintextDecode
    	fo = open(fileOut,"w")
    	P = ""
    	for i in C:
    		m = MyMath.powMod(MyBase.toInt(i,64),d,n)
    		c = str(m)
    		while len(c) % base != 0:
    			c = '0' + c
    		x = 0
    		while x != len(c):
    			a = c[x:x+base]
    			x+= base
    			P+= chr(int(a))
    			fo.write(chr(int(a)))
    	fo.close()
    	return P