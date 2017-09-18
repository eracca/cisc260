import sys

hnum = sys.argv[1]
digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
num = 0

for i in range(8):
    num += digits.index(hnum[i])*16**(7-i)

print(num)
