temperatures = [10, 12, 14]

string_temp = [str(temp) + '\n' for temp in temperatures]
file = open("file.txt", 'w')

file.writelines(string_temp)