
# 20CE017 Parth Darji
#  Write a Python program to find the most common elements and their counts from 
# list, tuple, dictionary.

listA = [45, 20, 11, 50, 17, 45, 50,50,50]
print("Given List:\n",listA)
maxRepeated = max(set(listA), key = listA.count)
print("Element with highest frequency:\n",maxRepeated)

