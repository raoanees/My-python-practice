str="aaabbbaaa";

i=0;
j=len(str)-1;
flag=True;
while(i<j):
    if(str[i]!=str[j]):
        print("Not a Palindrome");
        flag=False;
        break;
    i=i+1;
    j=j-1;

if flag==True:
    print("Palindrome");
