#print Hello World message
print("Hello World")
#program to create int data type
a=23
print(a)
print(type(a))
#program to create float
x=3.8
print(x)
print(type(x))
#program to create string data type
b="human"
print(b)
print(type(b))
#program to create list data type
list=[1,2,3,4,5,6]
print(list)
#program to create tuple data type
tuple=(3,8.9,55,200,"maker",80,3.5)
print(tuple)
#dictionary data type
d={'a':10,'b':20,'c':30}
print(d)
d['d']=40
print(d)
#set data type
s={8,200,7.4,'main',3}
print(s)
s.add(99)
print(s)
s.remove(200)
print(s)
s2={8,100,'main',50,'xyz'}
print(s.intersection(s2))
print(s.union(s2))
print(s2.difference(s))
#convert int to float
x=85
y=float(x)
print(y)
#convert int to boolean
x=27
y=bool(x)
print(y)
#sum of nos
a=45
b=55
c=50
sum=a+b+c
print(sum)
print(sum+a)
print(a+c)
print(b+c)
print(c+a,sum+c)
#dictonary name and students marks
d={'rahil':80,'Noah':60,'akif':89,'Rida':98,'ramish':77}
print(d)
#slicing qt in python
original_list=[10,20,30,40,50,60,70,80]
print(original_list[2:6])
print(original_list[5:8])
print(original_list[::2])
print(original_list[2])
print(original_list[4:1:-1])