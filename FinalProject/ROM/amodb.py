data = "v2.0 raw\n"

for i in range(0,256):
    for j in range(0,256):
        if j == 0:
            data += "0\n"
        elif i%j==0:
            data += "1\n"
        else:
            data += "0\n"

with open("amodb.hex",'w') as f:
    f.write(data)