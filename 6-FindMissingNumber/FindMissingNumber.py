import random

my_list = [i for i in range(0, 101)]
random.shuffle(my_list)

#solution_1 to remove 1 random element
remove_list = random.sample(my_list, 1)

#my_list.sort(reverse = False)
#print("Our List: ",my_list)
#print("Number Removed from List: ",remove_list)

for i in remove_list:
    my_list.remove(i)

#solution_1 to delete 1 random element
#my_list.sort(reverse = False)
print("Our List: ",my_list)


#Find the deleted element
#solution_1

#missing_num = []
#for i in range(0, 101):
#    if i not in my_list:
#        missing_num.append(i)

#print(f"One number is missing from our list. Missing number: {missing_num}")
#solution_2

my_set = {i for i in range(0,101)}

difference_set = my_set - set(my_list)
print(f"One number is missing from our list. Missing number: {difference_set}")