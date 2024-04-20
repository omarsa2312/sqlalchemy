from sqlalchemy.orm import sessionmaker
from models import User, engine


"""
    To do crud operations we need session.
    bind is used to tell session that to whicch db it has to make transactions
"""
Session = sessionmaker(bind=engine)

# actual session object on which we can perform the actions
session = Session()


# CRUD Operations
# --------- Create ----------
"""
# Creating a user object.
user_1 = User(name = 'Om Tiwari', age = 22)
user_2 = User(name = 'Samad Ahmad', age = 23)
user_3 = User(name = 'Satyam Kumar', age = 24)
user_4 = User(name = 'Sanchit Chaudhary', age = 25)

# add method is used to add one object at a time.
session.add(user_2)

# to all mutliple objects we can use add_all and pass a list inside it.
session.add_all([user_3, user_4])

session.commit()
"""

# ---------- Read ----------
'''
# to read the data
all_users = session.query(User).all()

om_user = all_users[0]
print(om_user.name)
print(om_user.id)
print(om_user.age)
'''

'''
om_user = session.query(User).filter_by(name = 'Om Tiwari').all()
print(om_user)
'''

# # It will either return one object or it will return none if there are no objects or more than one objects
# om_user = session.query(User).filter_by(id = 1).one_or_none()
# print(om_user.name)
# print(om_user.age)

# similarly like all, one_or_none, we have first. Gives the first element of the array

# ------Update-----
# to make the change in the database
# suppose I want to change the name of Satyam Kumar to saty kumar
# satyam_user = session.query(User).filter_by(name = 'Satyam Kumar').first()
# satyam_user.name = 'Saty Kumar'
# session.commit()

# ----- Delete-----
# suppose I want to delete the entry with Sanchit Chaudhary
sanchit_user = session.query(User).filter_by(name = 'Sanchit Chaudhary').first()
session.delete(sanchit_user)
session.commit()