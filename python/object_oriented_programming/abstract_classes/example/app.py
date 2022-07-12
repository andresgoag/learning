'''
Example of using abstract classes to define objects that can be save to a database

Database: Is a class that stores the information and with the 
methods insert, remove and find.

Saveable: Is an abstract class that defines that the subclasses of it must have 
a method called to_dict, that is used to save in DB with the function save.

User: Is a subclass of Saveable. so it has to override the to_dict function.

Admin: Is a subclass of User. Has an additional field than user, access. It 
modifies the to_dict function so it includes the access to be saved.

'''

from database import Database
from admin import Admin

a = Admin('rolf', '1234', 3)
a.save()

print(Database.find(lambda x: x['username'] == 'rolf'))