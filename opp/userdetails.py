# creating a class
class User():
    def __init__(self,name,age,location) :
        self.name=name
        self.age=age
        self.location=location
# a function to print location
    def Location(self):
            print(f'He stays at {self.location}')
# creating an object
user1=User("john",20,"kazo") 
# print the user location using the function  
user1.Location()
# printing the user name and age
print(f'name is {user1.name} and age is {user1.age}')     