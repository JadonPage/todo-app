filenames = ['a', 'b', 'c']

for filename in filenames:
    file = open(rf"C:\Users\Adata\Downloads\{filename}.txt", 'r')
    print(file.read())