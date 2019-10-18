friendlist = [0] * 1001

with open("listin.txt", "r") as listin:
    for i, line in enumerate(listin):
        if i > 0:
            a,b = line.split()
            friendlist[int(a)] += 1
            friendlist[int(b)] += 1

max_friends_num = max(friendlist)
listout = open("listout.txt", "w")
for id,val in enumerate(friendlist):
    if val == max_friends_num:
        listout.write(str(id)+'\n')
listout.close()
