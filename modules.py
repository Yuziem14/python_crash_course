'''
https://github.com/bradtraversy/python_sandbox
'''

# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module | pip3 install camelcase
from camelcase import CamelCase

# Import custom module
import mymodule
from mymodule import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = CamelCase()
# print(c.hump('hello there world'))

email = 'email@email.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')