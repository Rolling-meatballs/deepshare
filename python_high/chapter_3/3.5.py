s = 'hello albert albert say hello world world'

words = s.split()
pure = []
for word in words:
    if word not in pure:
        pure.append(word)
result = dict()

for i in range(len(pure)):
    count = words.count(pure[i])
    result[pure[i]] = i

print(result)

#method 1
list1 = s.split()
dict1 = {}
for item in list1:
    if item in dict1:
        dict1[item] += 1
    else:
        dict1[item] = 1
print('dict1:', dict1)

#method 2
dict2 = {}
list2 = s.split()
for word in list2:
    dict2[word]= s.count(word)
print('dict2:', dict2)

#method 3
dict3 = {}
list3 = s.split()
for word in list3:
    dict3.setdefault(word, s.count(word))
print('dict3:', dict3)
