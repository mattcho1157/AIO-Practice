f = open('bugsin.txt', 'r')
y = int(f.readline())
f.close()

f = open('bugsout.txt', 'w')
f.write(str(y+(7-y%7)))
f.close()
