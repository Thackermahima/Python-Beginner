# A List is a collection which is ordered and changeable. Allows duplicate members.

# numbers = [1,2,3,4,5,6] 

# numbers2 = list((1,2,3,4,5,6))

# print(numbers,  numbers2) 

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears'] 
print(fruits[1])
print(len(fruits))

fruits.append('Mangos')
print(fruits)
fruits.remove('Grapes')
print(fruits)

fruits.insert(2, "stawberries")
print(fruits)

fruits.pop(2) 
fruits.reverse
print(fruits, "reverse")

fruits.sort()
print(fruits) 


#Change  value 
fruits[0] = 'Blueberries'
print(fruits) 

