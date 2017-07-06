#Usage of iterators in python

class IterClass:

    def __init__(self,n):
        self.i=0;
        self.n=n;


    def __iter__(self):
        return self;

    def next(self):
        if self.i<self.n:
            self.i+=1;
            return self.i;
        else:
            print("No more items exists in list")



iterobj = IterClass(5);
print(iterobj.next());
print(iterobj.next());
print(iterobj.next());
print(iterobj.next());
print(iterobj.next());
print(iterobj.next());
print(iterobj.next());
