#CS 161 Week 3 Assignment

#1

x = input("What is your name? ")
print ("Hello " + x)

#2

#y = input ("What is your age? ")
#print (y + 5)

#This produces an error because the input command assigns the input to a string by default. When the program runs y + 5, it is attempting to add a integer to a string which it can't do.

y = int(input("What is your age? "))
print(y + 5)

#3
z = int(input("How many years to add? "))
print("In " + str(z) + " years, you will be " + str(y + z))

#4
hours = float(input("Enter the number of hours worked: "))
wage = float(input("Enter your hourly wage, without the $: "))

#5

print("Your gross pay this week is $ " + str(hours * wage))
print("Your estimated annual gross pay will be $ " + str({hours * wage * 50}))