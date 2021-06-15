# easy_crypto

hint:https://www.anquanke.com/post/id/211028

## wp

看到题目给了n是2048位的，给了800位的d我们设为d0 所以我们有下面的方程： 

$$ed = k*f(n)+1$$ $$ed0 = k*(p-1)(n/p-1)+1 (mod 2^t)) (t=800)$$ 

解这个关于p的方程，由于我们知道k是小于等于e的，也即是说我们在（1,e+1）的时候循环，即可找到我们想要的前800位p0

我们找到了p0，然后怎么办呢，然后我们要找到p ，由于coppersmith 定理，我们用sage库里的程序

```
f = x*(2**known_bits)+ZZ(p0)
f = f.monic()
roots = f.small_roots(X = 2 ** (NBITS(N) / 2 - known_bits), beta=0.3)
# roots[0]*(2**known_bits)+p0 = k*p
```

完整exp：

```
def NBITS(N):
n1 = hex(N)[:]
return len(n1)*4

def find_pq(d0,e,N):
X = var('X')
PR.<x> = PolynomialRing(Zmod(N))

print '[ ] Thinking...'
for k in xrange(1, e+1):
results = solve_mod([e * d0 * X - k * X * (N - X + 1) + k * N == X], 2 ** known_bits)

for m in results:
f = x * 2 ** known_bits + ZZ(m[0])
f = f.monic()
roots = f.small_roots(X = 2 ** (NBITS(N) / 2 - known_bits), beta=0.3)

if roots:
x0 = roots[0]
p = gcd(2 ** known_bits * x0 + ZZ(m[0]), N)
print '[+] Found factorization!'
return (ZZ(p),N / ZZ(p))
break
if __name__ == "__main__":
known_bits = 800
print NBITS(N)
p,q = find_pq(d0,e,N)
print 'p =', p
print 'q =', q
fn = (p-1)*(q-1)
d = pow(e,-1,fn)
m = pow(ct,d,N)
m = ZZ(m)
print 'm = ' ,m
print hex(m)[2:].decode('hex')
```
