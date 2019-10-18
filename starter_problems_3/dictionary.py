f = open("dictin.txt","r")
first_line = f.readline().split(" ")
terms = int(first_line[0])
translate = int(first_line[1])
counting = 1
translating = 1
dictionary = {}

while counting <= terms :

    a = f.readline().split(" ")
    dictionary[str(int(a[0]))] = str(int(a[1]))
    counting += 1

g = open("dictout.txt","w")

while translating <= translate :

    b = str(int(f.readline()))
    if b in dictionary.keys():
        
        definition = int(dictionary[b])
        g.write(str(definition) + "\n")
        
    else:

        g.write("C?\n")

    translating += 1

f.close()
g.close()
