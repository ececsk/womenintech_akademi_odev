#Bubble Sort Algorithm
def bubblesort(liste):
    for iteration_num in range(len(liste)-1,0,-1):#we can compare up to the penultimate element, so len(liste)-1 since there is nothing to compare after the last element
        for i in range(iteration_num):
            if liste[i]>liste[i+1]:
                temp = liste[i]
                liste[i] = liste[i+1]
                # print(liste)
                liste[i+1] = temp
    return liste

##2.YOL
#def bubblesort(liste):
#  for i in range(len(liste)):
#    for j in range(len(liste)-1):#we can compare up to the penultimate element, so len(liste)-1 since there is nothing to compare after the last element
#      if liste[j]>liste[j+1]:
#        liste[j+1],liste[j]=liste[j],liste[j+1]


#Selection Sort Algorithm
def selectionsort(liste):
    for i in range(len(liste)):
        min = i
        for j in range(i+1,len(liste)):
            if liste[min]>liste[j]:
                min = j
        liste[i],liste[min] = liste[min],liste[i]
    
    for i in range(len(liste)):
        liste[i] #Sorts elements from smallest to largest
    
    return liste

#Merge Sort Algorithm
#Insertion Sort Algorithm
#Shell Sort Algorithm


my_list =[28, 3, 24, 75, 1, -45]

print("The initial state of the list: ",my_list)

print("Sorting the list with BUBBLE SORT Algorithm: ",bubblesort(my_list))

print("Sorting the list with SELECTION SORT Algorithm: ",selectionsort(my_list))