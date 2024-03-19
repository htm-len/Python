#Match
name = input("What's your name? ").lower()

match name:
    case "harry" | "hermione" | "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")
