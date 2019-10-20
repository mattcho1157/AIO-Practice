f = open("secrtin.txt", "r")
keyL, msg = f.readlines()
f.close()

alp = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
       "J", "K", "L", "M", "N", "O", "P", "Q", "R",
       "S", "T", "U", "V", "W", "X", "Y", "Z"]
keyN = [alp.index(x) + 1 for x in keyL[:-1]]
ans = []

nLength = len(keyN)
index = 0

f = open("secrtout.txt", "w")

for i in msg:
    f.write(alp[(alp.index(i) + keyN[index % nLength]) % 26])
    index += 1

f.close()
