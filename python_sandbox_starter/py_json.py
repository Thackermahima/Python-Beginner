# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json 

#Sample JSON 

userJson  = '{"first_name" : "John", "last_name" : "Doe", "age" : 30}'

#parse to dict 

user = json.loads(userJson)
print(user)
print(user['first_name']) 


car = {"make": 'ford', 'model': 'Mustang'}

carJson = json.dumps(car)
print(carJson)
