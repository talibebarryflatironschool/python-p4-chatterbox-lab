# #!/usr/bin/env python3

# from random import choice as rc

# from faker import Faker

# from app import app
# from models import db, Message

# fake = Faker()

# usernames = [fake.first_name() for i in range(4)]
# if "Duane" not in usernames:
#     usernames.append("Duane")

# def make_messages():

#     Message.query.delete()
    
#     messages = []

#     for i in range(20):
#         message = Message(
#             body=fake.sentence(),
#             username=rc(usernames),
#         )
#         messages.append(message)

#     db.session.add_all(messages)
#     db.session.commit()        

# if __name__ == '__main__':
#     with app.app_context():
#         make_messages()





#!/usr/bin/env python3
from app import app
from models import db, Message

with app.app_context():
    # Optionally clear existing data
    db.drop_all()
    db.create_all()

    message1 = Message(body="Hello, World!", username="Ian")
    message2 = Message(body="Flask API is cool!", username="Alex")
    message3 = Message(body="Full-stack development FTW!", username="Sam")

    db.session.add_all([message1, message2, message3])
    db.session.commit()
    print("Database seeded!")
