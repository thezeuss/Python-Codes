def removeElement(element):
    if element in a:
        a.discard(element)
        return a
    else:
        return 'This element does not exist in set'



a = set([1,2,3,4])
print(removeElement(2))