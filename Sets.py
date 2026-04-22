s1 = [1,1,2,2,3,3]
st1 = set(s1) 
print(st1)
st2 = {"Hello","World","Hello"}
print(st2)
#print(st2[1]) -> Sets are NOT indexible
#To check if an element exists in a set or not:
if 3 in st1:
    print("Yes")
else:
    print("No")
# Adding elements to sets:
st3 = set([]) #Also {} is valid. But this is confusing because it is similar to dictionary.
st3.add(9)
st3.add(9)
st3.add(6)
st3.add(2)
st3.add(1)
st3.add(10)
print(st3)
#Removing elements from sets:
st3.remove(2)
#st3.remove(5) If we try to remove a number that is not present in the list, with the remove function, it will throw an error.
st3.discard(5) # Unlike the remove function, the discard function doesn't throw an error when we try to discard a number that is not present in the list.
st3.discard(9)# Remove: Present elements. Discard: Present and not present elements.
print(st3)
#Set operations - Union, Intersection, Difference, Symmetric Difference:
a = {1,2,3,4,5}
b = {4,5,6,7,8}
print(a.union(b))# Combines sets together and removes duplicates(because sets only store unique elements.)
print(a.intersection(b))# Prints the overlapping/same elements in the sets.
print(a.difference(b)) # What is there in a but not in be.
print(a.symmetric_difference(b))# First does union. Then subtracts the intersection from the union(difference).