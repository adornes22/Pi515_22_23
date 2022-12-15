# Create a class for contact information
# Use the included Template.py as reference

# 1. Define a class called contact
# 2. Write the constructor
# 3. Create instance variables for the following:
#   - First name (argument 1)
#   - Last name (argument 2)
#   - Phone number (argument 3)
#   - Blocked status  (default false)
# 4. Create an instance method which changes
# the blocked status from false to true

class contact:

 blocked = False
  
 def __init__(self,first,last,phone):
    self.firstname = first
    self.lastname = last
    self.phone = phone

 def toggleblocked(self):
    if self.blocked:
      self.blocked = False
    else:
      self.blocked = True

x=contact('Ana','Dornes','911')
print(x.firstname)
print(x.lastname)
print(x.phone)
print(x.blocked)
x.toggleblocked()
print(x.blocked)

print('\n')
y=contact('My','Mother','119')
print(y.firstname)
print(y.lastname)
print(y.phone)
print(y.blocked)