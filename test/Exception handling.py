import sys
try:
    x=10/0;
except ZeroDivisionError as err:
    print(err)

try:
    f=open("notexistfile",'r')
except IOError as err:
    print(err)
finally:
    print("010010100001010 ! Computer is signing off")


a=True;
b=False;
x=a== (not b);
print(15//-4)
