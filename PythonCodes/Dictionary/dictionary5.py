# 20CE017 PARTH DARJI


#method 1
dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

d = {}

d.update(dic1)
d.update(dic2)
d.update(dic3)

print(d)

# Method 2

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

d = {}

for i in (dic1, dic2, dic3):
    d.update(i)

print(d)