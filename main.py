import cv2
import math
#This is a comment
print("Hello Word")
print(math.gcd(3,6))
'''
This is a multi line comment 
'''
print(5+8)
print(cv2.__version__)

''' --Variables-- '''
a = 22
b = "Harry"
c = 22.66
print(a + 5)

# Rules for creating variable
# 1. variable should start with a letter or underscore.
# 2. variable  cannot start with a number
# 3. It can only contain alphanumeric characters
# 4. Variable names are case sensitive

''' Use type() to get type of the variable '''

typeA = type(a)
print(typeA)

#Typecasting

d = "31"
d = int(d)
print(type(d))

#Multiline strings

name = ''' Mahima
   Thacker'''
print(name)
namee = "Mahima"
print(namee[0])
#Slice in Strings
#It will print 2-5 = 3 letters
print(namee[2:5])

name2 = "     Mahima  "
name3 = "hello, hii"
#It won't print spaces in string
print(name2.strip())
print(len(namee))

var = namee.lower()
var = namee.upper()
var = namee.replace("a", "m")
var = name3.replace(",",'')
print(var)

stri = "This is a"
name4 = "Mahima"
name5 = "Anjali"
# temp = "{} and {} both are sisters". format(name4, name5)
temp = f"{name4} and {name5} both are sisters"
print(temp)

''' Operators '''
# 1) + 
# 2) -
# 3) /
# 4) *
# 5) ** Exponentiation Operator
# 6) // floor division Operator
# 7) % Module Operator

''' 

Python Collection :
1) List
2) Tuple
3) Set
4) Dictionary

'''
#1) List
ex = [61, 2, 3, 44, 22]
var = type(ex)
ex[2] = 77
# ex.append(50) #This will add number in the List
ex.insert(2, 70) #[61, 2, 70, 77, 44, 22]
#ex.remove(2)
#ex.pop()  #It will remove element of list from last
# del ex[1]
# ex.clear() #List will be cleared
print(ex)
print(var)

# 2) Tuple
a = ("hello", "hii")
# a = list(a)
print(type(a))


#Tuples values are unchangable, for ex: a[0] = Hey is incorrect

# 3) Sets
# A set in Python is an unordered collection of unique elements. This means that sets cannot contain duplicate elements,
# and the order in which the elements are stored is irrelevant.

s1 = { 5,5, 5, 5, 5, 2, 2, 6, 7,0}
# s1.add(88)
# s1.update([60, 77, 99909, 3232])
# print(len(s1))
# s1.remove(99) This will give an error
# s1.discard(99) It won't give us an error
# we can use .clean .del .pop
print(s1)
'''Intersaction: It will return comman elements of two sets'''

set1 = { 2, 4 , 6, 8}
set2 = { 2, 8, 4, 2}
# intersection = set1.intersection(set2)
# intersection = set1 & set2

# print(intersection)

''' Union '''
union = set1.union(set2)
print(union)

''' Disctionary : It is combination of Key value pairs '''
mahimaDisc = {
   "Name" : "Mahima",
    "Age"  : "18",
    "Gender" : "Female"
}
print(mahimaDisc)
print(mahimaDisc["Name"])

# Input : Type of Input will always be string
# age = input("Enter your Age\n")
# print(age)
# age = int(age)
# if(age>18) : 
#    print("You can drive")
# elif(age == 18) : 
#    print("YOU are an adult")
# else :
#    print("You cannot drive")

''' FOR LOOP '''
# for x in range(0, 100):
#   print(x)

# lst = [1, 4, "Hello"]
# for i in lst:
#    print(i)

''' WHILE LOOP '''

# i = 0 
# while( i < 50):
#    i = i + 1
#    if(i == 30):
#       # break
#       continue
#    print(i+1)

#Functions: 
# def greet():
#    print("Morning")

# greet()

def sum(a,b):
   c = a+b
   return c
d = sum(22, 33)
print(d)

#OOP - Class and constructor
class Employee:
   def __init__(self, gname, gsalary):
      self.name = gname
      self.salary = gsalary

harry = Employee("harry", 33)
print(harry.name)
print(harry.salary)



