#Password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(f"Here is your password: {password_list}") # before
random.shuffle(password_list)
print(f"Here is your password: {password_list}") # after
password = ""
for char in password_list:
    password += char

print(f"Here is your password: {password}")  # after conversion to String

#Fizz buzz app
'''
target = int(input("Enter a number: "))
for number in range(1, target + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
'''

#Adding even numbers, user imput
'''
target = int(input("Enter a number: "))
total = 0
for number in range(2, target + 1, 2):
    total += number
print(total)
'''


#Using For wth range (summ al numbers from 1 to 100)
'''
total = 0
for number in range(1, 101):
    total += number
print(total)
'''


# High score in a list
'''
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
high_score = 0
for score in student_heights:
    if score > high_score:
        high_score = score
print(f"high_score = {high_score}")
'''

# Sum the number in a list using For
'''
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number_of_students = {number_of_students}")
average_height = round(total_height / number_of_students)
print(f"average_height = {average_height}")
'''

'''
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
'''
