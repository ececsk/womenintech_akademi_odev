def getIndexesOfNums(liste, target):
  visitedNumbers =  {} 
  for indx in range(len(liste)):
      remain = target - liste[indx] #We subtract the number from target to find the other value.

      if remain in visitedNumbers: 
          return [visitedNumbers[remain], indx]
 
      visitedNumbers[liste[indx]] = indx


my_list = [5,9,7,2,4,1]
print(f"Toplamı 6 olan iki sayının bulunduğu indexler: {getIndexesOfNums(my_list,6)}")


#solution_2
#def getIndexesOfNums(liste, target):
#    for outerIndex in range(len(liste)): #We're going through each element in the list.
#        for innerIndex in range(len(liste)):#For each number in the list, we go through each number in the list one by one.
#            if outerIndex == innerIndex: #Since we cannot use the values in the same index, we skip the same indexes.
#                continue
#            elif liste[outerIndex] + liste[innerIndex] == target:#If the sum of the numbers in the indexes we are on is equal to the target, we return these indexes.
#                return [outerIndex, innerIndex]
