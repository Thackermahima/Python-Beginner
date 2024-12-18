# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

person = {
    'first_name' : 'John',
    'last_name' : 'Doe'
}

print(person['first_name'])
print(person.get('last_name'))

person['phone'] = '5555555555555'

person2 = person.copy()
person2['city'] = 'Boston'
print(person2) 

del(person['first_name'])

#List on dic 

person3 = [
    {"name" : "etc", 'age' : 30},
     {"name" : "Kevib", 'age' : 30},
    
]
print(person3[1]['name'])
print(person, type(person))
