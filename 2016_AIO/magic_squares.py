f = open("magicin.txt", "r")
numbers = list(map(int, f.readline().split(" ")))
f.close()
increase = sorted(numbers)
total = increase[1] + increase[2] + 1
one = total - (numbers[0] + numbers[1])
two = total - (numbers[1] + numbers[2])
three = total - (numbers[0] + numbers[2])
f = open("magicout.txt", "w")
f.write(str(numbers[0]) + " " + str(numbers[1]) + " " + str(one) + " \n")
f.write(str(numbers[2]) + " " + str(two) + " " + str(numbers[1]) + " \n")
f.write(str(three) + " " + str(numbers[2]) + " " + str(numbers[0]) + " \n")
f.close()
