#q1)Create an empty dictionary
dict={}
print(dict)
#q2)Create a dictionary with key-value pairs for a person's name and age
person={'name': 'rida', 'ayaz':55, 'age':40}
print(person)
#q3)Access the value associated with the key "age" in the person dictionary
print(person.values())
#q4)Check if a key exists in the person dictionary.
if 'name' in person:
    print('exist')
else:
    print('not exist')
#q5)Add a new key-value pair "city" with the value "New York" to the person dictionary
key='City'
value="New york"
person[key]=value
print(person)
#q6)Remove the key-value pair with the key "age" from the person dictionary
person.pop('ayaz')
print(person)
#q7)Iterate through the keys in the person dictionary.
for key in person:
    print(key)
#q8)Iterate through the values in the person dictionary
val=print(person.values())
print (value)
for i in person.values():
    print(i)
#q9)Iterate through both keys and values in the person dictionary.
both_k_v=person.items()
print(both_k_v)
for key,value in person.items():
    print(key)
    print(value)
#q10)Create a dictionary with default values using the dict.from keys() method
d={}
d['x']=1
d['y']=1
d['z']=1
keys=['x','y','z']
d2='default'
dic= dict.fromkeys(keys,d2)
print(dic)
#q11)Get the value associated with a key using the dict.get() method with a default value.
x=person.get("musa",25)
print(x)
#q12)Count the number of occurrences of each character in a string using a dictionary.
h1="hello"
h2={}
for i in h1:
    if i in h2:
        h2[i]+=1
    else:
        h2[i]=1
print(h2)
#q13)Merge two dictionaries.
dict2={'a':10,'b':20,'c':30}
print((person|dict2))
#q14)Create a dictionary where the values are squares of the keys
sq={x: x**2 for x in range(1,8)}
print(sq)
#q15)Find the key with the maximum value in a dictionary.
#q16)Sort a dictionary by its keys.
sort_person= (sorted (dict.keys()))
print(sort_person)
#q17)Check if two dictionaries are equal.
if person == dict2:
    print ("both are equal")
else:
    print ("both are not equal")
#q18)Remove all elements from a dictionary.
person.clear()
print(person)
#q19)Create a nested dictionary
nesteddict = {1:{'rida': 20 , 'City':'New york', "bilal":40},2:{'a':10,'b':20,'c':30}}
print(nesteddict[1]['rida'])
print(nesteddict[2]['c'])
print(nesteddict[1]['City'])
#q20)Get a list of all keys in a dictionary
lists=(dict2.keys())
print(lists)
#q21)Get a list of all values in a dictionary.
lists1=(dict2.values())
print(lists1)
#q22)Update values in a dictionary using another dictionary
dict.update(dict2)
print(dict)
#q23)Remove a key from a dictionary using the pop() method.
dict.pop("a")
print(dict)
#q24)Get a list of tuples containing key-value pairs from a dictionary.
list=[]
list=(dict.items())
print(list)
#q25)Convert a list of tuples into a dictionary.
li_tup=[('name','rida'),('a',10),('b',20)]
dic={key:value for key,value in li_tup}
print(dic)