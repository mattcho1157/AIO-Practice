f = open('cultin.txt', 'r')
n = int(f.readline())
f.close()
answer = 0
while n%2 == 0:
    n /= 2
    answer += 1

f = open('cultout.txt', 'w')
f.write(str(int(n)) + " " + str(answer))
f.close()
