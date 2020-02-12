import copy

l = ['a', 'b', 1, 'a', 'a']

one = set(l)
print('one:', one)

l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

l = [

    {'name': 'albert', 'age': 18, 'sex': 'male'},

    {'name': 'james', 'age': 35, 'sex': 'male'},

    {'name': 'taylor', 'age': 25, 'sex': 'female'},

    {'name': 'albert', 'age': 18, 'sex': 'male'},

    {'name': 'albert', 'age': 18, 'sex': 'male'},

]
