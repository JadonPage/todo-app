import glob

myfiles = glob.glob("Day 15/files/*.txt")

for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.read())
