data = "v2.0 raw\n"

def isprime(n):
    if n < 2: return False
    if n < 4: return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

for i in range(0,256):
    if isprime(i):
        # print(1)
        data += "1\n"
    else:
        # print(0)
        data += "0\n"

with open("prime.hex",'w') as f:
    f.write(data)