import os

base_path = os.path.dirname(__file__)
testcases_67 = os.path.join(base_path, 'testcases_2567')
testcases_68_mock = os.path.join(base_path, 'testcases_2568_mock')


transfer = [0]*32

transfer[int("00000",2)] = int("000000",2)
transfer[int("00001",2)] = int("000001",2)
transfer[int("00010",2)] = int("000010",2)
transfer[int("00011",2)] = int("000011",2)
transfer[int("00100",2)] = int("000100",2)
transfer[int("00101",2)] = int("000101",2)
transfer[int("00110",2)] = int("000110",2)
transfer[int("00111",2)] = int("001001",2)
transfer[int("01000",2)] = int("001010",2)
transfer[int("01001",2)] = int("001111",2)
transfer[int("01010",2)] = int("010000",2)
transfer[int("01011",2)] = int("010001",2)
transfer[int("01100",2)] = int("010010",2)
transfer[int("01101",2)] = int("010011",2)
transfer[int("01110",2)] = int("010100",2)
transfer[int("01111",2)] = int("010101",2)
transfer[int("10000",2)] = int("010110",2)
transfer[int("10001",2)] = int("100000",2)
transfer[int("10010",2)] = int("100001",2)
transfer[int("10011",2)] = int("100010",2)
transfer[int("10100",2)] = int("100011",2)
transfer[int("10101",2)] = int("100100",2)
transfer[int("10110",2)] = int("100101",2)
transfer[int("10111",2)] = int("110000",2)
transfer[int("11000",2)] = int("101000",2)
transfer[int("11001",2)] = int("101001",2)
transfer[int("11010",2)] = int("101010",2)
transfer[int("11011",2)] = int("101011",2)
transfer[int("11100",2)] = int("101100",2)
transfer[int("11101",2)] = int("110001",2)
transfer[int("11110",2)] = int("110011",2)
transfer[int("11111",2)] = int("111111",2)

for filename in os.listdir(testcases_67):
    file_path = os.path.join(testcases_67, filename)
    new_path = os.path.join(testcases_68_mock, "mock"+filename)
    # print(file_path)
    with open(file_path, 'r') as f:
        lines = f.readlines()

    data = ""
    n = len(lines)
    lines[0] = lines[0].replace("progIN","progIn")
    # lines[0] = line[0].split()
    for i in range(1,n):
        line = lines[i].split()
        val = int(line[2])
        # print(lines[i])
        # print(line[2], val)
        opcode = val>>8
        oprand = val%256
        opcode = transfer[opcode]
        new_val =(opcode<<8)+oprand
        line[2] = str(new_val)
        lines[i] = " ".join(line) + "\n"

    with open(new_path, 'w') as f:
        f.write("".join(lines))

# print(sum/n)


# for i in range(32):
#     print(f"transfer[int(\"{i:0{5}b}\",2)] = int(\"000000\",2)")