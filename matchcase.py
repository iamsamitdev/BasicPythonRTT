lang = input("Please input language: ")

match lang:
    case "python":
        print("You choose python")
    case "java":
        print("You choose java")
    case _:
        print("Invalid in your choose")
