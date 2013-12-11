from pymongo import MongoClient
from flask import session
c = MongoClient()
db = c.users
default_prefs = {
    "Italian":False,
    "French":False,
    "Chinese":False,
    "Japanese":False,
    "Spanish":False,
    "Fast":False,
    "Dessert":False,
    "Ethiopian":False,
    "Middle-Eastern":False,
    "Polish":False,
    "Thai":False,
    "Caribbean":False}
def authorize(username, password):
    user = db.Collections.find_one({'username':username, 'password':password})
    if user:
        return 0
    else:
        return None
def userExists(username):
    return len(list(db.Collections.find({'username':username}))) == 1
def createUser(username, password):
    if len(username) < 4 or len(password) < 6:
        return 2
    if not userExists(username):
        ui = db.Collections.count()+1
        db.Collections.insert({'id':ui,'username':username, 'password':password, 'preferences': default_prefs})
        return 0
    else:
        return 1
def changePW(username, oldpw, newpw):
    user = db.Collections.find_one({'username':username, 'password':oldpw})
    if user:
        db.Collections.update({'username':username},{'$set':{'password':newpw}})
        return 0
    return 1

def updatePrefs(username, prefs):
    db.Collections.update({'username':username},{'$set':{'preferences':prefs}})

def getPrefs(username):

    return db.Collections.find_one({'username':username})["preferences"]

