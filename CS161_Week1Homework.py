#CS 161 Week 1 Assignment

#Part 1
sibling_type = "Sister" #I do not have any pets, so I am using my sister instead
sibling_name = "Hannah"
print(f"I have a {sibling_type} and her name is {sibling_name}.")

#Part 2
name = input("Enter your first name: ")
age = int(input("Enter your current age: "))
savings = int(input("Enter your yearly savings: "))
print(f"Hello {name}! You are currently {age} years old.")
print(f"In 10 years, you will be {age + 10} years old.")
print(f"If you save {savings} each year, in 5 years you will have saved ${savings * 5}.")
print(f"Your average monthly savings is ${savings // 12:.2f}.") #The sample output had the results include cents.

#Part 3
print(f"The number of seconds in January is {31*24*60*60}")

#Part 4
eggs = int(input("Enter the number of eggs: "))
print(f"This makes {eggs // 12} dozen eggs with {eggs % 12} left over")