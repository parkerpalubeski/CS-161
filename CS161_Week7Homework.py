#Part 1

#Prompts the user for input
num1 = int(input("Enter the lower number: "))
num2 = int(input("Enter the higher number: "))
n = num1

#Determines if the input is odd, and assigns it to the next number if so
if n % 2 == 1:
    n += 1
print(f"The even numbers between {num1} and {num2} are ")

#Prints n, then assigns the next even number to n
while n <= num2:
    print(f"{n} ")
    n += 2


#Part 2
#Gets User Input
fnum = int(input("Enter a positive Integer: "))

print(f"The factors of {fnum} are: ")
factor = 1

#Cycles through the numbers from 1 to the input, determining if they are a factor of the input
while factor <= fnum:
    if fnum % factor == 0:
        print(f"{factor} ")
    factor += 1


#Part 3:

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
name = input("Enter a name: ")

#a is to count while iterating, total is the sum
a = 0
total = 0

#Iterates through the list, counting the number of instances that letter is present in the name, and adds its number to total
for l in alphabet:
    total += name.count(l) * a
    a += 1

print(f"The sum of the numeric position of the letters of {name} is: {total}")

#Part 4:
#Recursive function
def squares(base_num):
    if base_num >= 1:
        squares(base_num-1)
        print(base_num ** 2)

#Gets input, they calls the function
input_num = int(input("Enter a positive integer: "))
squares(input_num)

#Part 5:
def teepee_sort(num_list):
    #Initialize Empty Lists
    evens = []
    odds = []
    sorted_list = []

    #Split the numbers in the original list into separate lists for even and odd numbers
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            evens.append(num_list[i])
        if num_list[i] % 2 == 1:
            odds.append(num_list[i])

    #Sort the Odds in ascending order
    for i in range(len(odds)):
        for j in range(len(odds)-i-1):
            if odds[j] > odds[j+1]:
                odds[j], odds[j+1] = odds[j+1], odds[j]

    #Sort the evens in descending order
    for i in range(len(evens)):
        for j in range(len(evens)-i-1):
            if evens[j] < evens[j+1]:
                evens[j], evens[j+1] = evens[j+1], evens[j]

    #Add the elements from the odds list, and then the evens list
    sorted_list.extend(odds)
    sorted_list.extend(evens)

    #Print
    print(f"The sorted list is: {sorted_list}")

#Initialize the original list, and then call the sorting function
unsorted_list = (12, 423, 22, 34, 2, 21, 3, 33, 81)
teepee_sort(unsorted_list)

#Part 6
#Unfinished, does not work
#def next_value(numbers_list):
#    position = len(numbers_list) - 1

    #Iterates through the list, starting at the end
#    while position > 0:
#        #Checks if the digit to the left is greater than the one to the right
#        if numbers_list[position-1] > numbers_list[position]:
#            numbers_list[position-1], numbers_list[position] = numbers_list[position], numbers_list[position-1]
#            if position - len(numbers_list) - 1 != 0:
#                for i in range(len(numbers_list)-position):
#                    for j in range(len(numbers_list) - i - 1):
#                        print(j)
#                        if numbers_list[j+position-1] > numbers_list[j + position]:
#                            numbers_list[j+position-1], numbers_list[j + position] = numbers_list[j + position], numbers_list[j + position-1]
#                            print(numbers_list)
#                return 0
#        else:
#            position -= 1

random_list = [9,5,2,1,7,6,0,8,3,4]
#next_value(random_list)