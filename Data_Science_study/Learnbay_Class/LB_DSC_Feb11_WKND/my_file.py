f = open('my_mod.txt', 'w+')
a = input('Enter a number: ')
f.write('Python class')
print(f.tell())
f.seek(0)
print(f.read())
print(f.tell())
f.close()
print("Hello World")
print("Hello World")
