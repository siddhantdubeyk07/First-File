a=[5,2,3,4]
print(a)
a[0]=1
print(a)
a.append(7) #append adds given value to list.
a.sort() #short arranges the list in ascending order.
print(a)
a.sort(reverse=True) # it will short list in descending order.
print(a)
a.reverse() #reverse the list.
a.insert(2,8) #insert element at index.
print(a)
a.remove(3) #remove first occurance of element.
print(a)
a.pop(4) #removes element at index.
print(a)

#Tuples
b=(1,2,3,4,4,4,4)
print(b)
print(type(b))
print(b.index(2)) #returns index of first ocurrence.
print(b.count(4)) #count total occurences.