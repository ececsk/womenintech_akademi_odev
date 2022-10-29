#Preparation of the list
import random

my_list = [i for i in range(0, 21)]
random.shuffle(my_list)

#solution_1 to remove 6 random elements
remove_list = random.sample(my_list, 6)

#print("Our List: ",my_list)
#print("Numbers Removed from the List: ",remove_list) 

for i in remove_list:
    my_list.remove(i)

#solution_2 to del 6 random elements
#del my_list[0:6]

#my_list.sort(reverse = False)
print("Our List: ",my_list)

#Find the deleted elements
#solution_1

missing_list = []
for i in range(0, 6):
    if i not in my_list:
        missing_list.append(i)

print(f"There are {len(missing_list)} missing numbers in our list. Missing numbers: {missing_list}")

#solution_2
#my_set = {i for i in range(0,21)}

#difference_set = my_set - set(my_list)
#print(f"There are {len(difference_set)} missing numbers in our list. Missing numbers: {difference_set}")