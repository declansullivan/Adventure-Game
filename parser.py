import main, player, layout

directional_verbs = ['move', 'walk', 'go', 'look']
directions = ['north', 'south', 'east', 'west', 'northwest', 'northeast', 
              'southwest', 'southeast', 'n', 'e', 's', 'w', 'nw', 'ne', 'sw', 
              'se', 'up', 'down', 'u', 'd']

vague_player = ['empty', 'check']
specific_item = ['drop', 'equip', 'take']
inventories = ['hand', 'inventory', 'surroundings', 'ground']

other_verbs = ['attack', 'with']
exit_verbs = ['quit', 'exit']

# Calls main.user's x method, used for checking and other.
vague_verb = lambda x, y: eval("main.user." + x + "_" + y + "()")
# Calls main.user's x method with y parameters, used for equipping and dropping.
speci_verb = lambda x, y: eval("main.user." + x + "(\"" + y + "\")")

default_error = "I don't recognize that.\n"

# Formats directions.
def directional_formatter(direction):
    if len(direction) <= 2:
        return direction
    elif len(direction) < 6:
        return direction[0]
    elif len(direction) > 5:
        return direction[0] + direction[5]
    else:
        return 'INVALID'

# Incorrect sentence structure method.
def retry(error_message):
    print(error_message)
    print("What would you like to do?")
    choice = input().lower().split()
    parse_text(choice)

# Avoids redundant code.
def direction_handler(verb, choice):
    choice = directional_formatter(choice)
    if hasattr(layout.world, choice):
        if verb == 'look':
            layout.look(choice)
        else:    
            layout.world = layout.movement(choice)
    else:
        retry(default_error)

# Incomplete sentence structure method.
def additional_term(verb_type, verb=None):
    choice = input().lower().split()
    if len(choice) != 1:
        retry(default_error)
    else:
        choice = choice[0]
        if verb_type == 'direction':
            if choice in directions:
                direction_handler(verb, choice)
            else:
                retry(default_error)
        elif verb_type == 'player':
            if verb in vague_player:
                if choice in inventories:
                    if choice == 'surroundings':
                        choice = 'ground'
                    vague_verb(verb, choice)
                else:
                    retry(default_error)
            else:
                speci_verb(verb, choice)

# Takes a sentence split into a list.
def parse_text(text):
    if len(text) < 1:
        retry(default_error)
    elif len(text) == 1:
        user_in = text[0]
        if user_in == 'help':
            print("Here are some possible verbs to use.")
            # TODO, VERBS
        elif user_in in exit_verbs:
            print()
            exit()
        elif user_in in directional_verbs:
            print("Where would you like to {}?".format(user_in))
            additional_term('direction', user_in)
        elif user_in in directions:
            direction_handler('walk', user_in)
        elif user_in in vague_player or user_in in specific_item:
            print("What would you like to {}?".format(user_in))
            additional_term('player', user_in)
        else:
            retry(default_error)
    elif len(text) == 2:
        user_verb, user_choice = text[0], text[1]
        if user_verb in directional_verbs and user_choice in directions:
            direction_handler(user_verb, user_choice)
        elif user_verb in vague_player and user_choice in inventories:
            if user_choice == 'surroundings':
                user_choice = 'ground'
            vague_verb(user_verb, user_choice)
        elif user_verb in specific_item:
            speci_verb(user_verb, user_choice)
        else:
            retry(default_error)
    else:
        pass