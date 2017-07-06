#Inheritance concepts

class parent:

    def __init__(self):
        self.name="Parent"

    def parent_method(self):
        print("Parent method called")


class child(parent):
    def __init__(self):
        self.name="Child"

    def child_method(self):
        print("Child method called")


child_obj = child();
parent_obj = parent();

child_obj.parent_method()
child_obj.child_method()

if issubclass(child,parent):
    print ("Child class is inherited from parent")

if isinstance(child_obj,child):
    print("Child obj is instance of child class")
if isinstance(child_obj,parent):
    print("Child obj is instance of parent class")