#This script covers basics of object oriented programming

#Creating class
class MyClass:
    "Dummy Class documentation string"
    globalVariable=0;

    def __init__(self,member1,member2):
        self.member1=member1;
        self.member2=member2;
        MyClass.globalVariable+=1;

    def printMetaData(self):
        print
        "MyClass.__doc__:", MyClass.__doc__
        print
        "MyClass.__name__:", MyClass.__name__
        print
        "MyClass.__module__:", MyClass.__module__
        print
        "MyClass.__bases__:", MyClass.__bases__
        print
        "MyClass.__dict__:", MyClass.__dict__


    def displayCount(self):
        print("Total Objects are {}".format(MyClass.globalVariable))

    def displayMember(self):
        print("Member details are {} & {}".format(self.member1,self.member2))

    def __del__(self):
        class_name=self.__class__.__name__
        print ("D-tor called for class {}".format(class_name))

#Creating instance and calling methods
my_class_obj=MyClass("This is"," Python")
my_class_obj.displayCount()
my_class_obj.displayMember()


#creating instance and calling methods
my_class_obj2=MyClass("This is"," PyCharm")
my_class_obj2.displayCount()
my_class_obj2.displayMember()

#Adding new attributes to instances
my_class_obj.newattr=1;
my_class_obj2.newattr=2;
print(my_class_obj.newattr)

#Using getattr,delatte
if hasattr(my_class_obj2,"newattr"):
    print(my_class_obj2.newattr)
    delattr(my_class_obj2,"newattr")
if hasattr(my_class_obj2,"newattr"):
    print(my_class_obj2.newattr)
    delattr(my_class_obj2,"newattr")
else:
    print("Attribute not available")


print("MyClass.__doc__:", MyClass.__doc__)
print("MyClass.__name__:", MyClass.__name__)
print("MyClass.__module__:", MyClass.__module__)
print("MyClass.__bases__:", MyClass.__bases__)
print("MyClass.__dict__:", MyClass.__dict__)

