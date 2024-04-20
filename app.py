import random
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from models import User, engine

"""
    To do crud operations we need session.
    bind is used to tell session that to which db it has to make transactions
"""
Session = sessionmaker(bind=engine)

# actual session object on which we can perform the actions
session = Session()

# CRUD Operations

# --------- Create ----------
# Creating a user object.
# user_1 = User(name = 'Om Tiwari', age = 22)
# user_2 = User(name = 'Samad Ahmad', age = 23)
# user_3 = User(name = 'Satyam Kumar', age = 24)
# user_4 = User(name = 'Sanchit Chaudhary', age = 25)

# # add method is used to add one object at a time.
# session.add(user_2)
# to add mutliple objects we can use add_all and pass a list inside it.
# session.add_all([user_3, user_4])
# session.commit()

# ---------- Read ----------
# to read the data
# all_users = session.query(User).all()
# om_user = all_users[0]
# print(om_user.name)
# print(om_user.id)
# print(om_user.age)

# Filtering
# om_user = session.query(User).filter_by(name = 'Om Tiwari').all()
# print(om_user)

# It will either return one object or it will return none if there are no objects or more than one objects
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
# sanchit_user = session.query(User).filter_by(name = 'Sanchit Chaudhary').first()
# session.delete(sanchit_user)
# session.commit()

# Populating the data in the table
# user_name_list = ['Rahul', 'Ram', 'Shyam', 'Abhinav', 'Deepak', 'Karan']
# user_age_list = [20, 25, 22, 23, 26, 29, 28, 21, 19, 30]

# for x in range(30):
#     user = User(name = random.choice(user_name_list), age = random.choice(user_age_list))
#     session.add(user)

# session.commit()

# query all users by age (by default it is ascending order)
# users = session.query(User).order_by(User.age.desc(), User.name).all()

# for user in users: 
#     print(f"{user.age} {user.name}")


all_users = session.query(User).all()
print(f"All users {len(all_users)}")

# Filter the users with age less than 25
# filtered_users = session.query(User).filter(User.age < 25, User.name == 'Rahul').all()
# print(f"Filtered users {len(filtered_users)}")

# important to note here is that filter_by is also a method to filter
# but filter_by does not supports conditionals, so we go by filter always
# where method is also there but it is a copy of filter method

# the comma separated conditions that we provide in the filter method
# follow the and condition. If we want or condition to be followed, we can wrap the conditions in or_ method
# filtered_users = session.query(User).filter(or_(User.age < 25, User.name == 'Rahul')).all()
# print(f"Filtered users {len(filtered_users)}")

# If we want or condition then we can also use the '|' operator present in python for the same
# similarly we have and_, and bitwise and not_
