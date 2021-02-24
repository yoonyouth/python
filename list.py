splatoon = ['Yoon','Hong-si','Neseki']

print(splatoon)
print(len(splatoon))
print(splatoon[2])

#add a new item at the end of the list
splatoon.append('Minji')

print(splatoon)
print(len(splatoon))
print(splatoon[2])

#remove the 'Minji' item
#if there are no corresponding item it will return ValueError 
splatoon.remove('Minji')

print(splatoon)
print(len(splatoon))
print(splatoon[2])

#insert the 'Munji' item in index 3
splatoon.insert(3, 'Munji')

print(splatoon)
print(len(splatoon))
print(splatoon[2])

#combine 2 lists in one by + operator
amongUs = ['Lee', 'Dol Dol']

amongYoon = splatoon + amongUs

print(amongYoon)

#add items in amoungUS to splatoon by extend
print(splatoon)

splatoon.extend(amongUs)

print(splatoon)

#delete the item on index 2 from splatoon
del splatoon[2]

print(splatoon)

#if you don't know the index of the item that you would like to delete
del splatoon[splatoon.index('Munji')]

print(splatoon)
