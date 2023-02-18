import json
# JSON
# JSON (Javascript object notation), is used a lot to fetch data from online apis. 
# Overall lesson course: Intro, JSON Library, Load Data Into Python, JSON to Python, Printing JSON, Deleting specific JSON data, Formatting JSON data, Indenting 
# Through JSON, Loading JSON, Looping through JSON, Removing Keys from JSON, JSON DUmp, JSON States, Real World Application, Load Response into Python Object, Cleaning up, Reviewing JSON Data, Working With JSON Data, Running the code, Creating Dictionary --> Running Key, Making Conversation.add

# people_string = '''
# {
#   "people": [
#     { 
#       "name": "John Smith",
#       "phone": "615-555-7164",
#       "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
#       "has_license": false
#   },
#     {
#     "name": "Jane Doe",
#     "phone": "615-555-7164",
#     "emails": null,
#     "has_license": true
#     }
#   ]
# }
# '''

# # Here we can see that you can load this string of JSON into the function below
# # this allows the string to be used, and become a python object/dictionary
# data = json.loads(people_string)
# # We then can use this as an object.
# print(data)
# print(type(data))
# # This will convert thins like "object" in JSON to "dict" in python. Same goes for 
# # array --> list
# # string --> str
# # number (int) --> int
# # number (real) --> float
# # true --> True
# # false --> False
# # null --> None

# # So doing this allows us to take JSON and convert it into something python can use
# # We can use this in shelling other code

# # Now we can use this as an actual list.abs

# for people in data['people']:
#   print(people['name'])

# for people in data['people']:
#   print(people)

# # Now let us do the reverse and dump a python string into a JSON one.

# # Let's first delete their phone numbers, an example if we wanted to do something similar.
# for person in data['people']:
#   del person['phone']

# # new_string = json.dumps(data)
# # print(new_string)

# # Let us formatt... indenting is a nice way to increase readability
# # new_string = json.dumps(data, str(indent=2))
# # print(new_string)
# # This will change the keys (classes) into alphetbetical order
# new_string = json.dumps(data,indent=2,sort_keys=True)
# print(new_string)

# Loading JSON files into python objects (working with objects)
from states import *

# Be careful when formatting json files and calling them in. Java is very case sensitive.
with open('states.json') as file:
  data = json.load(file)
  print(data)

# We can print out specific items that we want. 
for state in data['states']:
  print(state)

# We can even call specific 
for state in data['states']:
  print(state['name'],state['abbreviation'])

# Dumping allows you to convert python into json
# Loading allows you to convert json into something that is readible for python.

# This allows us to take in information and store it too another section as a text document.
with open('new_states.json', 'w') as f:
  json.dump(data, f)

# When we run this it will look messy so we can use indent and other methods to keep it clean.
