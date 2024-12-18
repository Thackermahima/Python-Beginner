# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits1 = tuple(('Apples', 'Oranges', 'Grapes'))
fruits2 = ('Apples',) #without , it will return type as a string
print(fruits)
print(fruits2, type(fruits2))

print(fruits[1])
# fruits[0] = 'Peers' 

# Del tuple
print(len(fruits))
# del fruits2
# print(fruits2)
# A Set is a collection which is unordered and unindexed. No duplicate members.

fruits_set = { 'Apples', 'Oranges'}

print('Apples' in fruits_set)

#Add to set 
fruits_set.add('Grape')
print(fruits_set)
