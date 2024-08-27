#qt] Print numbers from 1 to 10 using a for loop
num= range(1,11)
for i in num:
    print(i)
#qt] Calculate the sum of numbers from 1 to 10 using a for loop
sum = 0
for num in range(1, 11):
    sum += num
print(sum)
#qt] Print the elements of a list using a for loop
list = [10, 20, 30, 40, 50]
for i in list:
    print(i)
#qt] Calculate the product of elements in a list using a for loop
li = [1,2,3,4,5]
product = 1
for num in li:
    product *= num
print(product)
#qt] Print even numbers from 1 to 10 using a for loop
a=[]
for i in range(1,10):
    if i%2 == 0:
        a.append(i)
print(a)
#qt] Print numbers in reverse from 10 to 1 using a for loop
for num in range(10, 0, -1):
    print(num)
#qt] Print characters of a string using a for loop
name= 'jasmine'
for i in name:
    print(i)
#qt]Find the largest number in a list using a for loop#
num = [1,4,3,99,7,12]
largest_number= num[0]
for i in num:
    if i > largest_number:
        largest_number = i
print(largest_number)

#qt] Print all uppercase letters in a string using a for loop
a= "Hello World Loop "
for k in a:
    if k.isupper():
        print(k)
#qt] Count the number of vowels in a string using a for loop
vowel = "aeiouAEIOU"
vowel_count = 0
for k in a:
    if k in vowel:
        vowel_count += 1
print(vowel_count)
#qt] Print a pattern of stars using nested for loops
rows= 5
for i in range(rows):
  for j in range(i + 1):
    print("*", end="")
  print()


#qt] Calculate the sum of numbers from 1 to 100 using a while loop
def sum_no(n):
    sum = 0
    num = 1
    while num <= n:
        sum += num
        num += 1
    return sum
result = sum_no(100)
print(result)

#qt] Print numbers divisible by 3 or 5 from 1 to 20 using a for loop
for numbers in range(1, 21):
  if numbers % 3 == 0 or numbers % 5 == 0:
    print(numbers)
#qt] Find the common elements in two lists using a for loop
li1=[10,20,30,40,50]
li2=[90,10,30,70,80]
def common_ele (li1, li2):
    common_elements = []
    for element in li1:
        if element in li2:
            common_elements.append(element)
    return common_elements
common=common_ele (li1, li2)
print(common)
#qt] Print numbers from 1 to 5, except 3 using a for loop and continue statement
for number in range(1, 6):
  if number == 3:
    continue
  print(number)
#qt] Print numbers from 1 to 10. If a number is divisible by 4, stop the loop using a for loop and break statement
for number in range(1, 11):
  print(number)
  if number % 4 == 0:
    break
#qt] Print numbers from 1 to 10. If a number is even, skip it using a for loop and else clause
for number in range(1, 11):
  if number % 2 == 0:
    continue
  else:
    print(number)
#qt] Print numbers from 1 to 10. If a number is even, break the loop using a for loop and else clause
for number in range(1, 11):
  if number % 2 == 0:
    break
    continue
  else:
      print(number)