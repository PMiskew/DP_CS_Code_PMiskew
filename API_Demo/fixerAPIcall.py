import requests
import json
from pprint import pprint

#Get Key
#This is a file not in my respository I don't want you to have it
file = open("..//..//API_Keys//fixerkey.txt","r")

#read is an instance method for file object. 
key = file.read()

#Tool to read the contents of a file into a list

#get is a static/class method in the request module. 
resp = requests.get('http://data.fixer.io/api/latest?access_key='+key)

#Converts response to JSON - A DICTIONARY
data = resp.json()

pprint(data)
print(data["base"])
print(data["rates"]["CAD"])

if "CAD" in data["rates"]:
    print("TRUE")
else:
    print("FALSE")

for key in data["rates"]:
    print(key+" :",data["rates"][key])

#print(data)