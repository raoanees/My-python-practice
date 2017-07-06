class parent:

    def my_method(self):
        print("Parent's my method")

class child(parent):

    def my_method(self):
        print("Child's my method")


childobj = child()
childobj.my_method()