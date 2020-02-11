name = " alberT"

one = name.rsplit()
print("one:", one)

two = name.index('al', 0)
print("two:", two)

three = name.index('T', -1)
print("three:", three)

four = name.replace('l', 'p')
print("four:", four)

five = name.split('l')
print("five:", five)

six = name.upper()
print("six:", six)

seven = name.lower()
print("seven:", seven)

eight = name[1]
print("eight:", eight )

nine = name[:3]
print("nine:", nine)

ten = name[-2:]
print("ten:", ten)

eleven = name.index("e")
print("eleven:", eleven)

twelve = name[:-1]
print("twelve:", twelve)