import random
from audioop import reverse


collections = ['list', 'tuple', 'dict', 'set']

for collection in collections:
    print('Learning {}'.format(collection))

del collections[2]
    
for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))
    
print(collections.count('tuple'))
    
numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 20))
    
print(numbers)
print(numbers.sort(reverse = False))
print(numbers)

empty_tuple = ()
empty_tuple = tuple ()

one_element_tuple = (1,)
print(type(one_element_tuple))