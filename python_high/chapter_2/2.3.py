data = input("Today's data:")
allday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

# set a value for result
result = 'wrong input'

for day in allday:
    if day == data:
        if data == allday[5]:
            result = 'rest day'
            break
        elif data == allday[6]:
            result = 'rest day'
            break
        else:
            result = 'work day'
            break

print(result)
