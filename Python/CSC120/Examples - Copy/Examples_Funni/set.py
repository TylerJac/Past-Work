set1 = set([1,2,3])
print(set1)
set2 = set([4,6,8])
print(set2)
set1.update(set2)
print(set1)
# set1.discard(2)
# set1.discard(6)
print(set1)
set3 = set1.intersection(set2)
print(set3)

set1 = {item for item in range(1, 6)}
print(set1)
set2 = {item for item in set1}
print(set2)
print(set1.issubset(set2))
print(set1.issuperset(set2))

set1 = set([1, 20, 2, 40, 4, 50])
print(set1)
set2 = {item for item in set1 if item < 10}
print(set2)
