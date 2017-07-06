def product(list):
    prod=1;
    for num in list:
        prod*=num;

    return prod;

list=[1,2,3]
print(product(list))