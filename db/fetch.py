import csv
from data import connectDB
from schema.message import SpamMessage

if __name__ == "__main__":
    db = connectDB()
    with open('models/data.csv', 'w') as data:
        writer = csv.writer(data)
        writer.writerow(['message', 'label'])
        for messages in SpamMessage.objects():
            writer.writerow([messages.message, messages.label])
    db.drop_database('spamData')
    db.close()