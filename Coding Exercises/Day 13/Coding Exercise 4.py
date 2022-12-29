def get_num_names(names_arg):
    """My solution"""
    start = 0
    names_list = []
    index = 0
    for i in names_arg:
        if i == ",":
            name = names_arg[start:index]
            names_list.append(name)
            start = index + 1
        elif index == len(names_arg) - 1:
            name = names_arg[start:index]
            names_list.append(name)
        index += 1
    number = len(names_list)
    return number


def get_nr_items(user_input):
    """Better Solution (Given)"""
    items = user_input.split(',')
    return len(items)


names = input("Enter names separated by commas (no spaces): ")
nr_items = get_nr_items(names)
print(nr_items)
