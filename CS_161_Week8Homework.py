#Task 1:

def phrase():
    word = str(input("Enter a word: "))
    return word

word1 = phrase()
word2 = phrase()
if word2 == word1.upper():
    print("Stop shouting please!")

#Task 2:
#I had figured that creating a vowels list and simply removing said vowel would be easier and more concise than writing out five if statements for each vowel
def Vowel_Counter(word):
    counter = 0
    vowels_list = ["a", "e", "i", "o", "u"]
    for i in range(len(word)):
        if word[i].lower() in vowels_list:
            vowels_list.remove(word[i])
            counter += 1
    return counter

string = str(input("Enter a string: "))

print(f"There are {Vowel_Counter(string)} unique vowels in the string {string}.")

#Task 3:

input1 = str(input("Enter a string: "))
input2 = str(input("Enter a string: "))
if input1 < input2:
    print(f"{input1} comes before {input2}")
else:
    print(f"{input2} comes before {input1}")

#Task 4:

def checkEmail():
    email1 = str(input("Enter your email address: "))
    email2 = str(input("Enter your email address again: "))
    while email1 != email2:
        print("Your two inputs did not match.")
        email1 = str(input("Enter your email address: "))
        email2 = str(input("Enter your email address again: "))
    print("Thank you!")

checkEmail()

#Task 5:
import time
def factorial_recursive(num):
    if num > 1:
        factorial = num * factorial_recursive(num - 1)
        return factorial
    else:
        return 1
def factorial_iterative(num):
    for i in range(1, num):
        num = num * i
    return num
def factorials(num):
    start = time.perf_counter_ns()
    print(f"The recursive function returns {factorial_recursive(num)}")
    stop = time.perf_counter_ns()
    print("Time elapsed: ", stop - start)
    start = time.perf_counter_ns()
    print(f"The iterative function returns {factorial_iterative(num)}")
    stop = time.perf_counter_ns()
    print("Time elapsed: ", stop - start)

factorials(3)
factorials(10)
factorials(25)