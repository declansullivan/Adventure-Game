import parser, player, monsters, layout

user = player.Player()

user.inventory = {"stick": 2, "torches": 4, "sword": 1}

def main():
    print("Welcome to DnZ (Definitely not Zork)!")
    name = input("What is your name?\n")
    age = input("What is your age?\n")
    place = input("Where are you from?\n")

    user.assign_values(name, age, place)

    print()
    print(user)
    print()

    while True:
        print("What would you like to do?")
        choice = input().lower().split()
        parser.parse_text(choice)
        # user.effect()
        print()

if __name__ == "__main__":
    main()