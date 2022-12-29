country = input("What country are you from? ")
country = country.strip()
country = country.lower()

while True:
    match country:
        case "usa":
            print("Hello")
            break
        case "india":
            print("Namaste")
            break
        case "germany":
            print("Hallo")
            break
