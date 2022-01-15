# 20CE017 PARTH DARJI

# Write a Python program to sum all the items in a dictionary.

dict = { 'a':10, 'b':20, 'c':30, 'd':40}

list = []

for i in dict:
    list.append(dict[i])

finalSum = sum(list)

print(finalSum)
    