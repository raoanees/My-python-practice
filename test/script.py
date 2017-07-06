#Hello World
print("Hello World");
#numeric Operators
print(6+2);
#adding two variables
var1=12;
var2=10;
print(var1+var2);
#printing simple string
str="NBSU";
print(str);
#tripple quotes literrals
print("""
This stuff 
is printed
using 
tripple quotes
""");
#Concatenated strigs using times
print("om"+3*"nom")
#concatenating two strings
prefix="py";
print(prefix+"thon");
#Strings as arrays
word="Python";
print("Character ar 0:"+word[0])
print("Character ar 1:"+word[1])
print("Character ar 2:"+word[2])
print("Character ar 3:"+word[3])
print("Character ar 4:"+word[4])
print("Character ar 5:"+word[5])
print("Characters at negative indices")
print("Character ar -1:"+word[-1])
print("Character ar -2:"+word[-2])
#Slicing Strings
print("Characters 2 to onwards(2 Included):"+word[2:]);
print("Characters start to 2(2 excluded):"+word[:2]);
print("Characters 0 to 4(0 included, 4 excluded):"+word[0:4]);
#Lists
list=[1,2,3,4,5,6,7,8,9];
print(list)
#Replacing item in list
list[0]=0;
print(list);
#List Built in functions
print(len(list));
#Appending items in list
list.append(10);
print(list)
#Removing item from list
list[0:1]=[];
print(list);
#Truncate list
list[:]=[];
print(list);
#Nested Lists
a=[1,2,3];
b=['a','b','c']
x=[a,b];
print(x);