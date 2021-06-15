# baby_crypto

Hint: 想一想 fn与n的关系？

## wp

e0d0 == k fn +1

```
from gmpy2 import *
k = e0*d0/n
while True:
    fn = (e0*d0 - 1)/k
    if fn*k + 1 == e0 * d0:
        break
    k+=1

d = invert(e,fn)

m = pow(ct,d,n)
print hex(m)[2:].decode('hex')
```

