f = open("encyin.txt","r")

firstLine = f.readline().split(" ")
words = int(firstLine[0])
allLines = f.readlines()

wordList = allLines[0:words]
questionList = allLines[words:]

f.close()

f = open("encyout.txt","w")

for page in questionList:
    page = int(page)
    answer = int(wordList[page-1])
    f.write(str(answer) + "\n")

f.close()
