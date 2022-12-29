text = "Hello"
filenames = ['report', 'doc', 'presentation']

for filename in filenames:
    file = open(f"{filename}.txt", "w")
    file.write(text)
    file.close()