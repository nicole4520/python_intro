from sys import exit

def start():
    print "You are in the Sahara dessert"
    print "You see a sandstorm coming and you must find cover."
    print "There is a cave nearby and so you decided to go in for shelter."
    print "there are 2 corridors in the cave. One on your left and the other on your right."
    print "You must chose one to go down."
    choice = raw_input("left / right >>>")

    if choice == "left":
        crown_room()
    elif choice == "right":
        spider_room()
    else:
        dead("You stayed on the outsdide of the cave and the sandstorm killed you. Game over.")

def crown_room():
    print "You have now entered a room with a rock and on top a gold crown."
    print "You could take the crown and sell it when you get out of there."
    print "It must be worth a lot as it is a gold crown."
    print "Or perhaps you just want to focus on getting out of the cave."
    choice = raw_input("take the crown / leave it >>")

    if "take" in choice:
        dead("Taking the crown has caused for an earthquake. You have awaken the gods from above. Game Over.")
    elif "leave" in choice:
        water_room()
    else:
        print "You MUST make a choice"
        crown_room()

def spider_room():
    print "You arrive in a room filled with plenty of spiders crawling up and down the walls."
    print "You want to leave but the door is covered."
    print "You have to take 2 steps to exit"
    spider_gone = False

    while True:
        choice = raw_input("use your shoe to squish the spiders / open the door / blow on the spiders to spread them apart>>")
        if "blow" in choice:
            dead("The spiders crawl all over your body. Game over.")
        elif choice == "use your shoe to squish the spiders" and not spider_gone:
            print "The spiders have been squished. The door is clear."
            spider_gone= True
        elif choice == "use your shoe to squish the spiders" and spider_gone:
            dead("There are no spiders to squish anyone. You waste your time. Game over.")
        elif choice == "open door" and not spider_gone:
            dead("The spiders crawl all over your body. Game over.")
        elif choice == "open door" and spider_gone:
            water_room()
        else:
            print "Please chose one of the following:"

def water_room():
    print "There is a room with a giant water hole inside."
    print "The weather is very warm and taking a swim would be very nice."
    print "However, you do not kow what lies in the water."
    choice = raw_input("swim / walk away >>>")

    if "swim" in choice:
        dead("As you swam, snakes came up and bit you. Game Over.")
    elif "leave" in choice:
        water_room()
    else:
        print "You MUST make a choice"
        crown_room()
