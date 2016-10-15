#This is the main game engine



# prints current room (example : print_room(rooms["Room1"])
def print_room(room):
    print()
    print(room["name"].upper())
    print()
    print(room["description"])
    print()


# takes a dictionary of exits and a direction returns the name of the exit it leads to
# example ( exit_leads_to(rooms["Room1"]["exits"], "south"))
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


# prints a line of a menu of exits. arguments are the name of the exit and the
# name of the room it leads to. example ("east","Room2")
def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


# prints actions available to the player (add actions)
def print_menu(exits):
    print("You can:")
    for direction in exits:
        print_exit(direction, exit_leads_to(exits, direction))

    print("What do you want to do?")


# checks if the exit is valid returns True if valid else False
# example: is_valid_exit(rooms["room1"]["exits"], "north") == True
def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


# updates the current room based on the direction (example execut_go("east"))
def execute_go(direction):
    global current_room
    if direction in current_room["exits"].keys():
        new_position = current_room["exits"][direction]
        current_room = rooms[new_position]
        print(rooms[new_position]["name"])
    else:
        print("You cannot go there.")


#  prints the menu of actions using print_menu() function.
#It then prompts the player to type an action. (add actions)
def menu(exits):
    print_menu(exits)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)
    return normalised_user_input


# returns the room the player will move in.
#example (move(rooms["Room1"]["exits"], "north")---> rooms["Room4"])
def move(exits, direction):
    return rooms[exits[direction]]
