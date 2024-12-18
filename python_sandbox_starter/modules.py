# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
from datetime import date
from time import time
# import time
# today = datetime.date.today()

import validator 
from validator import validate_email
today = date.today()
timestamp = time()
print(timestamp)
print(today)

email = 'test@gmail'
if validate_email(email):
    print("valid")
else: 
    print('Email is bad')