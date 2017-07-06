#Write a function group(list, size) that take a list and splits into smaller lists of given size.

def group_and_split(list,size):
    parent=[];
    groups=len(list)/size;
    i=0;
    j=0;
    while(j<groups):
        child=list[i:i+size];
        i+=size;
        parent.append(child);
        j+=1

    return parent;

print(group_and_split([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(group_and_split([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))


list=[1,2,3,4,5,6,7,8,9,10]