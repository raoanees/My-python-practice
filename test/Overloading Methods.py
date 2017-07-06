class vector:

    def __init__(self,a,b):
        vector.a=a;
        vector.b=b;

    def __add__(self, other):
        return vector(self.a+other.a,self.b+other.b)

    def print_vector(self):
        print("Vector {},{}".format(self.a,self.b))

vector_force = vector(1,3)
vector_momentum = vector(2,5)

(vector_force+vector_momentum).print_vector();

