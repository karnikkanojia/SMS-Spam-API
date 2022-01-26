from mongoengine import connect
from pprint import pprint

def connectDB():
    return connect('spamData', host='mongodb://localhost:27017/', username='root', password='1406')
