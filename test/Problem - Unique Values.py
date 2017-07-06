#Find unique values from the list

def unique(list):
    uniqs=[];
    for i in list:
        if i not in uniqs:
            uniqs.append(i)
    return uniqs

list = [1,2,2,1,4,5,1,2,6,3]
print(unique(list))

#Find duplicate values

def dups_func(list):
    dups = [];
    i=0;
    while(i<len(list)):
        if list[i] in list[i+1:]:
            dups.append(list[i])
        i+=1
    return unique(dups)

print(dups_func([1, 2, 1, 3, 2, 5]))
