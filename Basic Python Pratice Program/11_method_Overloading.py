class Student:

    def hello(self, name=None):
        if name is not None:
            print('Hey ' + name)
        else:
            print('Hey')

# Creating a class instance
std = Student()

# first overloading for hello
std.hello()

# Call the method for second parameter
std.hello('sagar')
