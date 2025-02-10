#Task 1
def check_factor(n):
    if n % 5 == 0:
        print("That is divisible by 5")
    else:
        print("That is not divisible by 5")

num = int(input("Enter a number: "))
check_factor(num)

#Task 2
def name_capital_elif(st):
    if st == "Oregon":
        print("Salem")
    elif st == "California":
        print("Sacramento")
    elif st == "Washington":
        print("Olympia")
    elif st == "Texas":
        print("Austin")
    elif st == "Montana":
        print("Helena")
    elif st == "Nevada":
        print("Carson City")

state_dict = {
    "Oregon":"Salem",
    "California":"Sacramento",
    "Washington":"Olympia",
    "Texas":"Austin",
    "Montana":"Helena",
    "Nevada":"Carson City"
}

def name_capital_mc(st):
    match st:
        case "Oregon":
            capital = state_dict.get("Oregon")
            print(capital)
        case "California":
            capital = state_dict.get("California")
            print(capital)
        case "Washington":
            capital = state_dict.get("Washington")
            print(capital)
        case "Texas":
            capital = state_dict.get("Texas")
            print(capital)
        case "Montana":
            capital = state_dict.get("Montana")
            print(capital)
        case "Nevada":
            capital = state_dict.get("Nevada")
            print(capital)
        case _:
            print("Unknown")


state = str(input("Name any state (Use proper capitalization): "))
name_capital_elif(state)
state2 = str(input("Name any state (Match-case/dictionary version): "))
name_capital_mc(state2)

#Task 3
def check_price(age):
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 60:
        return 6
    else:
        return 4

swimmer_age = int(input("Enter age: "))
print(f"For a {swimmer_age} year old, your price is ${check_price(swimmer_age)}")

#Task 4

import requests
import psutil

request = requests.get("http://coccbobcat.com")
html = request.text
ct = html.count("160")
print(f"The string '160' appears {ct} times on the page")
pids = psutil.pids()
print(f"There are {len(pids)} running processes right now.")