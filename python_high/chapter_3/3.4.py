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

# print(set(l))
# report error: unhashable type: 'dict'
s = set()
l1 = []
for item in l:
    val = (item['name'], item['age'], item['sex'])
    if val not in s:
        s.add(val)
        l1.append(item)
print(l1)

# define function, not only for hash type but also for not belonging to hash type
def func(items, key=None):
    s = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in s:
            s.add(val)
            yield item

print(list(func(l, key=lambda dic: (dic['name'], dic['age'], dic['sex']))))