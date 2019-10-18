# Reading the file
f = open("addin.txt", "r")
numbers = f.readline()
f.close()

# Spliting the two numbers
values = numbers.split(" ")
number_1 = int(values[0])
number_2 = int(values[1])

#Adding the numbers
added = int((number_1) + (number_2))

# Writing to a file
f = open("addout.txt","w")
f.write(str(added) + "\n")
f.close()
