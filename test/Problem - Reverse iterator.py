#Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction. ::

class ReverseIter:

    def __init__(self,list_):
        self.list=list_
        self.index=len(self.list)

    def __iter__(self):
        return self;

    def next(self):
        if self.index>0:
            self.index-=1;
            return self.list[self.index]

        else:
            print("nothing to print")



list=[1,2,3,4,5]
rev_iter=ReverseIter(list)
print(rev_iter.next())
print(rev_iter.next())
print(rev_iter.next())
print(rev_iter.next())
print(rev_iter.next())
print(rev_iter.next())
print(rev_iter.next())
