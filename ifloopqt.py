#Question: Write a program that uses nested if statements to determine if a person can drive based on age and whether they have a license.
def can_drive(age, has_license):
    if age >= 18:
        if has_license:
            return True
        else:
            return False
age = 30
has_license = True
if can_drive(age, has_license):
  print("You can drive")
else:
  print("You can't drive")
#Question: Write a program that uses nested if statements to determine the price of a ticket based on age and membership status.
def ticket_price(age, is_member):
    if age < 15:
        if is_member:
            return 10
        else:
            return 17
    elif age < 70:
        if is_member:
            return 17
        else:
            return 20
age = 25
is_member = True
price = ticket_price(age, is_member)
print("The ticket price is:", price)
#Question: Write a program that uses nested if statements to determine if a person is eligible to apply for a job based on age and work experience.
def is_eligible_for_job(age, work_experience):
  if age >= 18:
    if work_experience >= 2:
      return True
    else:
      return False
  else:
    return False
age = 22
work_experience = 1
if is_eligible_for_job(age, work_experience):
  print("You are eligible.")
else:
  print("You are not eligible.")
#Question: Write a program that uses nested if statements to determine if a year is a leap year.
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
#Question: Write a program that uses nested if statements to classify a student's grade based on their marks
def classify_grade(marks):
  if marks >= 90:
    return "A+"
  elif marks >= 80:
    return "A"
  elif marks >= 70:
    return "B+"
  elif marks >= 60:
    return "B"
  elif marks >= 50:
    return "C+"
  elif marks >= 40:
    return "C"
  else:
    return "F"
marks = 82
marks2 = 91
marks3 = 45
grade = classify_grade(marks)
grade2 = classify_grade(marks2)
grade3 = classify_grade(marks3)
print("The student's grade is:", grade)
print("The student's grade is:", grade2)
print("The student's grade is:", grade3)
#Question: Write a program that uses nested if statements to determine if a person is eligible to vote based on their age and citizenship status.
def is_eligible_to_vote(age, is_citizen):
  if is_citizen:
    if age >= 18:
      return True
    else:
      return False
  else:
    return False
age = 25
is_citizen = True
if is_eligible_to_vote(age, is_citizen):
  print("You are eligible to vote.")
else:
  print("You are not eligible to vote.")
#Write a program that uses nested if statements to check if a number is even or odd, and if it is greater than 10.
def check_number(number):
  if number % 2 == 0:
    if number > 10:
      return "The number is even and greater than 10."
    else:
      return "The number is even but not greater than 10."
number = 12
result = check_number(number)
print(result)
#Question: Write a program that uses nested if statements to determine if a number is positive, negative, or zero.
def check_number(number):
  if number > 0:
    return "The number is positive."
  elif number < 0:
    return "The number is negative."
  else:
    return "The number is zero."
number = -6
result = check_number(number)
print(result)
#Question: Write a while loop to calculate the sum of numbers from 1 to 100.
sum = 0
i = 1
while i <= 100:
  sum += i
  i += 1
print(sum)
#Question: Write a while loop to repeatedly ask the user to enter a positive number.
while True:
  number = int(input("Enter a positive number: "))
  if number > 0:
    print("You enter:", number)
    break
  else:
    print("Please enter a positive number.")
#Question: Write a while loop to print the string "Hello" 5 times
count = 0
while count < 5:
    print("Hello")
    count += 1
#Question: Create a while loop to repeatedly ask for a password until the correct one is entered.
correct_password = "code"
while True:
  password = input("Enter password: ")
  if password == correct_password:
    print("Correct password")
    break
  else:
    print("Incorrect password. Please try again.")
#Question: Write a while loop to print multiples of 3 that are less than 30.
i = 3
while i < 30:
  print(i)
  i += 3
#Question: Write a while loop to continue prompting the user until they enter a number between 1 and 10.
while True:
  number = int(input("Enter a number between 1 and 10: "))
  if 1 <= number <= 10:
    print("You entered:", number)
    break
  else:
    print("Please enter a number between 1 and 10.")
#Question: Write a while loop that prints numbers from 1 to 10, but stops if the number is 6.
i = 1
while i <= 10:
  if i == 6:
    break
  print(i)
  i += 1
#Question: Write a for loop that prints numbers from 1 to 10, but skips printing the number 5.
for i in range(1, 11):
  if i == 5:
    continue
  print(i)

#Question: Write a for loop that iterates over a list of numbers and prints each number, but does nothing if the number is 3
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
  if number == 3:
    continue
  print(number)
#Question: Write a for loop that searches for the first negative number in a list and stops the loop once it finds one.
numbers = [1, 2, -3, 4, 5, 6, 7]
for number in numbers:
  if number < 0:
    print("The first negative number is:", number)
    break
#Question: Write a for loop that prints all even numbers from 1 to 10, using continue to skip odd numbers
for i in range(1, 11):
  if i % 2 != 0:
    continue
  print(i)
#Write a while loop that does nothing until a variable count reach
count = 0
while count < 5:
  # Do nothing
  pass
print("count is:", count)
#Write a for loop that prints numbers from 1 to 15, but skips numbers that are multiple of 3 and 5
for number in range(1, 16):
  if number % 3 == 0 or number % 5 == 0:
    continue
  print(number)