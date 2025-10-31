data = "v2.0 raw\n"

def lcm(a, b):
    res = a*b
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return res//a

for i in range(0,256):
    for j in range(0,256):
        if i == 0 or j == 0:
            res = 0
        else:
            res = lcm(i,j)
        msg = f"lcm({i},{j}) = {res}"
        print(msg)
        data += str(hex(res))+'\n'

with open("lcm.hex",'w') as f:
    f.write(data)