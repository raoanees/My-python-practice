from math import pi

#Generating list with range
num_list = list(range(10))
print(num_list)

#Generating list with some expression -
num_list=[(x,x**2) for x in range(10)]
print(num_list)

pi_list=[(round(pi, i)) for i in range(1, 6)]
print(pi_list)


#Sets
Fruits={"Apple","Banana","Banana","Orange","Banana","Mango"}
print(Fruits)
is_member="Orange" in Fruits
print(is_member)
