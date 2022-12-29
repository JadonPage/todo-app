filenames = ['document', 'report', 'presentation']

for i, name in enumerate(filenames):
    filename = f"{i}-{name.capitalize()}.txt"
    print(filename)