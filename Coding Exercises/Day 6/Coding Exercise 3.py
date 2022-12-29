new_member = input("Add a new member: ")

file = open(r"C:\Users\Adata\Downloads\members.txt", 'r')
members = file.readlines()
file.close()

members.append(f"{new_member}\n")

file = open(r"C:\Users\Adata\Downloads\members.txt", 'w')
file.writelines(members)
file.close()
