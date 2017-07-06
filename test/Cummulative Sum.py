#Function calculates the cummulative sum of list

def cum_sum(list):
    i=1;
    while(i<len(list)):
       list[i]=list[i]+list[i-1]
       i+=1;
    return list;

list=[1,2,3,4,5];
print(cum_sum(list));