from mongoengine import connect
from db.schema.message import SpamMessage
from dotenv import load_dotenv
import os


load_dotenv('.env')
def connectDB():
    return connect('spamData', host=os.environ.get('MONGO_URI'))

def createDoc(message=None, label=None):
    message = SpamMessage(message=message, label=label)
    return message.save(validate=True)
    