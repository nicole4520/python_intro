from sys import exit
#declare a function called "start" and print out three lines of story

def start():
    print "You are on a plane."
    print "There are two doors in exit doors in of you."
    print "One is on your left the other on your right. You have to jump out of one."
    choice = raw_input("left / right >>>")
    #write a conditional that calls bear_room() if we turn left, and cthculhu_room() if right

    if choice == "left":
        bear_room()
    elif choice == "right":
        cuthulhu_room()
    else:
        dead("You stayed in the plane as it crashed into the Sahara dessert. All remaining passergers are dead. Game over.")

def bear_room():
    print "There is a bear in the sky."
    print "He is in your way."
    print "How are you going to move him?"
    bear_moved = False
    #Wite a while loop that repeats forever unless we run dead() or gold_room(). There will be three options - take honey / taunt bear / open door. The play must first taunt the bear before openening the door. ALl other options must lead to death.
    while True:
        choice = raw_input("take honey / taunt bear / open door >>")
        if choice == "take honey":
            dead("The bear slaps your face off. Game over.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved. The door is clear."
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear groans very loudly and your ears burst.Game over.")
        elif choice == "open door" and not bear_moved:
            dead("The bear chews off your left toe. Game over.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "Please chose one of the following:"

def cuthulhu_room():
    print "Here you see an evil creature - the Cthulhu."
    print "If he stares at you, you will go insane."
    print "Do you flee for your life or fight the creature?"
    choice = raw_input("flee / fight >>")

    if "flee" in choice:
        start()
    elif "fight" in choice:
        dead("The Cthulu makes your brain melt. Game Over.")
    else:
        print "You feel youself becoming more insane..."
        cuthulhu_room()

def gold_room():
    print "This room is full of gold!"
    print "How much do you take?"
    choice = raw_input("Type a number >>")

    if int(choice) < 100:
        print "Good Job! You are not greedy! you win!"
        exit(0)
    else:
        dead("You are too greedy. You get stuck in the room Game over!")

def dead(msg):
    print msg
    exit(0)

start()
