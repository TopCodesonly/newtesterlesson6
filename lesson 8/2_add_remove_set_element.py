m={1,2,3}
m.add(4)
print(m)
# updata
m={1,2,3}
m.update([4,5,6])
print(m)# {1,2,3,4,5,6}

# remove

m={1,2,3,4,5,6}
m.remove(4)
print(m)
m.remove(11) #it will rasise an error

# discard

m={1,2,3,4,5,6}
m.discard(4)
print(m)
m.remove(11) # it dose nothing unlike remove


# pop

m={1,2,3,4,5,6}
m.pop()
print(s) # randomly takes and shows and element from the set 

m.clear() #{}