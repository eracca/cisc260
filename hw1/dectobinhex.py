import sys

dnum = int(sys.argv[1])
digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
bnum = ""
hnum = ""

#convert to binary
quant = abs(dnum)
while (quant > 0):
    bnum = str(quant % 2) + bnum 
    quant = quant / 2

#pad with zeros
if len(bnum) < 32:
    tmp = (32 - len(bnum))*"0" + bnum
    bnum = tmp

#two's complement
if (dnum < 0):
    #invert
    tmp = ""
    for char in bnum:
        if (char == "0"):
            tmp += "1"
        else:
            tmp += "0"
    bnum = tmp
    #add 1
    tmp = ""
    point = 1
    for char in reversed(bnum):
        if (point == 1) and (char == "1"):
            tmp = "0"+ tmp
        elif (point == 1) and (char == "0"):
            tmp = "1" + tmp
            point = 0
        else:  
            tmp = char + tmp 
    bnum = tmp
print(bnum) 

#convert to hex
for i in range(8):
    num = 0
    tmp = bnum[(28-4*i):(32-4*i)]
    for j in range(4):
        if tmp[j]=="1":
            num += 2**(3-j)
    hnum = digits[num] + hnum
print(hnum)
