# 20CE017 PARTH DARJI
# b. 
# Write a Python script to merge two Python dictionaries.

#function to merge two dictionaries
def merge(d1,d2):                       
     return (d1.update(d2))

d1 = {'a':100, 'b':200}
d2 = {'x':300, 'y':600}

merge(d1,d2)
print(d1)

# Method 2

d1 = {'a':100, 'b':200}
d2 = {'x':300, 'y':600}

d=d1.copy()d.update(d2)

print(d)
