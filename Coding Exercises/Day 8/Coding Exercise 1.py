while True:
    entry = input("Enter 'clear' to erase saved data. \nEnter 'exit' to stop the program. \n"
                  "Throw the coin and enter 'head' or 'tail': ")

    if entry == 'exit':
        break

    with open("coinflip_probability.txt", 'r') as file:
        log = file.readlines()

    if entry == 'head' or entry == 'tail':
        log.append(entry + '\n')

    heads_total = log.count("head\n")

    percent = heads_total / len(log) * 100

    with open("coinflip_probability.txt", 'w') as file:
        if entry == "clear":
            log = []
            file.writelines(log)
            percent = 0
        else:
            file.writelines(log)

    print(f"Heads: {percent}%")
