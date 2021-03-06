from sys import exit

def gold_room():
    """The gold room environment."""
    print("This room is full of gold. How much do you take?")

    try:
        how_much = int(input("> "))

        if how_much < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        else:
            dead("You greedy bastard!")

    except ValueError:
        dead("Man, learn to type a number.")

def bear_room():
    """The bear room environment."""
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False;

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    """The Cthulu room."""
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    """Takes in a message, prints with "Good job!" and exits."""
    print(why, "Good job!")
    exit(0)

def start():
    """Start the game."""
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
