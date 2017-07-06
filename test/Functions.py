#Defining and calling functions
def sum(number_a, number_b):
    return number_a + number_b;


print(sum(1 , 2));
print(sum(2 , 4));


#Pass by value
def changeMe(number_change):
    number_change=123;
    return;

changeMeNum=1;
changeMe(changeMeNum);
print(changeMeNum);


#Pass by reference & Required Arguments
def DareToChangeMe(myList):
    myList.append(1);
    return
myLocalList=[2,34,5];
DareToChangeMe(myLocalList);
print(myLocalList);


#Keyword Arguments
def keywordFunc(arg1,arg2,arg3):
    print(arg1+arg2+arg3);
    return
keywordFunc(arg1="Northbay",arg2=" Solutions",arg3=" University :)");


#Default Arguments
def defaultArgs(name,defaultVal=100):
    print("{} Scored {} Runs".format(name,defaultVal));
    return

defaultArgs("Fakhar Zaman");
defaultArgs("Hafeez",10);


#Variable length arguments
def variableLenParams(arg1,*vargs):
    print("Arg1:",arg1);
    for v in vargs:
        print(v,end=' ');
    return

variableLenParams(1,"sdaf","sdafsda","sdafsdaf",123,12.34)


#Ananymous functions / Lambda Expressions
print();
sum=lambda param1,param2:param1+param2;

print("Sum using Lambda expression:",sum(1,43));


#Documentation strings
def fooDocString():
    """This is test document string for foo function"""

    return

print(fooDocString.__doc__);