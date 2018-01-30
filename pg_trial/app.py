from user import User
from database import Database

# print(Database.connection_pool)
Database.initialise(user='postgres',
                    password='postgresql2018',
                    database='learning',
                    host='localhost')
# print(Database.connection_pool)


my_user = User("Joe@baidu.com",
               "Joe",
               "Wang",
               None)

# User.save_to_db(my_user)
my_user.save_to_db()
my_user = User.load_from_db_by_email('Joe@baidu.com')
print(my_user)
#
#
# my_user = User("Sherry@baidu.com",
#                "Sherry",
#                "Hui",
#                None)
#
# my_user.save_to_db()
