# Create a class to hold your contact list
# 1. Define a class called contactList
# 2. Create a class variable list
# 3. Create an instance method called printList()
#  to print class variable list

# 4. Below your class definition, create a
#  new instance of contactList
# 5. Create 2 contacts and add them to list
#  inside your contactList object
# 6. Run your instance method printList()

from Exercise_1 import contact

class contact:

  isBlocked = False

  def__init__(self,first,last,num):
    self.firstName = first
    self.lastName = last
    slef.phone = num

