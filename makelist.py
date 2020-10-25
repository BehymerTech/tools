#! /usr/bin/python3

import requests

import argparse

# Catch user input
parser = argparse.ArgumentParser(description='Add parameter arguments')
parser.add_argument('--userID', help='Submit userID for processing')
args = parser.parse_args()
userID = args.userID


apiURL= 'https://reqres.in/api/'
if userID is not None: 
    params = {"id": userID, "format" : "json"}
else:
    params = {"format" : "json"}

getUsers = requests.get(apiURL + 'users' , params=params)
# print(getUsers.text)
usersJSON = getUsers.json()
user = usersJSON['data']
print(user['last_name'])

# usersJSON = getUsers.json()
# print (usersJSON)
# print(usersJSON.keys())
# vars(response).keys()