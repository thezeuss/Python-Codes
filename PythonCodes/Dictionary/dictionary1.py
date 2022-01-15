# 20CE017 PARTH DARJI
# DICTIONARY

# a .
# Write a Python script to check whether a given key already exists in a dictionary.

x = {1:50, 2:100, 3:200, 4:500, 5:69, "hello":68}

def isPresent(y):
    if y in x:
        print('Key is present in the dictioanry')
    else:
        print('Key is not present in the dictionary')
    
      
isPresent(68)   #Checks only Key not values.
isPresent(500)
isPresent(2)
isPresent(4)
        
        

