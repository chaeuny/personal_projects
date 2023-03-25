# create a list of integers 
# and take all of the numbers in the list that are even and create a new list with only the even numbers 

import random 

list_of_integers = []
for i in range(0, 6):
    n = random.randint(1,20)
    list_of_integers.append(n)

print(list_of_integers)

new_list = []

for num in list_of_integers:
    if num % 2 == 0:
        new_list.append(num)

print(new_list)


