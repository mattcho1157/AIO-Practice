f = open("ninjain.txt", "r")
total, escape = list(map(int, f.readline().split(" ")))
f.close()
a = (total%(escape + 1))
if a == 0:
    answer = escape * (total//(escape + 1))
else:
    answer = escape * (total//(escape + 1)) + (total%(escape + 1)) - 1

f = open("ninjaout.txt", "w")
f.write(str(answer))
f.close()
