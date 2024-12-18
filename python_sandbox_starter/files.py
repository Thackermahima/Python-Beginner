# Python has functions for creating, reading, updating, and deleting files.

myFile = open('myfile.txt', 'w')


#Get Info over file 

print('Name ', myFile.name)
print('is Closed ', myFile.closed)
print('Opening Mode ', myFile.mode)


#write to the File 

myFile.write('I love python')
myFile.write(' and Javascript')
myFile.close() 

#Append to file  
myFile = open('myfile.txt', 'a')
myFile.write(' and also solidity')
myFile.close() 
 
 #Read from file 
 
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)


