#Task 1
#def average(n1, n2, n3):
#    return (n1 + n2 + n3) / 3

#print(average(7,5,9))
#print(average (6,6,7))



#Task 2:

#print(average(7,5,9))
#print(average (6,6,7))

#def average(n1, n2, n3):
#    return (n1 + n2 + n3) / 3

#The script does not run because when the print command has been called, the average function had not yet been defined in the program



#Task 3:

#def average(n1, n2, n3):
#    return (n1 + n2 + n3) / 3

#print(average(7,5,9))
#print(average (6,6,7))

#print(n1)

#The command print(n1) produces an error because n1 is defined within the scope of the average function, but not the scope of the rest of the program, like where the print command is called



#Task 4:

def convert_human_age(age):
    return 24 + (age - 2)*4

print("6 dog years is equivalent to " + str(convert_human_age(6)))

print("22 dog years is equivalent to " + str(convert_human_age(22)))



#Task 5:

def car_depreciation(age, make, price):
    if make == 'German':
        price = price * .95**age
    elif make == 'Japanese':
        price = price * .93**age
    elif make == 'Italian':
        price = price * .95**age

    print(f"The value of your {make} car will be ${price:.2f} after {age} years.")

car_depreciation(7, 'Italian', 73000)
car_depreciation(22, 'Japanese', 40000)
car_depreciation(1, 'German', 55000)



#Task 6:

#I was unsure if the formula for step 6 was the same as in step 4, so I reused that formula. It seems to provide a different result than the example though.

def dog_years(dog_age):
    return 24 + (dog_age - 2)*4
print("Dog's Age Calculator:")
dog_name = str(input("What is your dog's name? "))
dog_age = int(input(f"How old is {dog_name}? "))
dog_age = dog_years(dog_age)
print(f"Your {dog_name} is {dog_age:.1f} human years old.")

#Task 7

def cone_price(scoop):
    return (scoop * 1.15) + 2.25

print("Ice cream cone price calculator:")
scoops = int(input("How many scoops would you like? "))
print(f"A {scoops}-scoop cone will cost ${cone_price(scoops):.2f}")

