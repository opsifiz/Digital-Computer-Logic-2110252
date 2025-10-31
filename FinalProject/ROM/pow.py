data = "v2.0 raw\n"

for i in range(0,8):
    for j in range(0,8):
        pow = i**j
        print(pow)
        msg = "a**b = {pow}"
        data += str(hex(pow))+'\n'

with open("pow.hex",'w') as f:
    f.write(data)