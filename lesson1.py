# Madlibs :
# 1. create a few variables that get certain bits from the user
# 2. print out a string with a short story, using the info gathered
# this will give me a way to get information from a user
name = raw_input("what is your name?")
number = raw_input("What is your favourite number between 1-10?")
animal = raw_input("What are your favourite animals?")
sibling = raw_input("What is your siblings name? or give a random name")
food = raw_input("What is your favourite food?")

story = "Once upon a time there was a princess named %s. She had %s pet %s. She had many servants and treated them all very badly. One day her servant by the name of %s had had enough. She locked princess %s in the cage with all the %s %s and left her there throughout the whole night. Princess %s was ferociously eaten and there was aboslutly nothing left at the end. Her servants then lived hapily ever after.The %s were left with an abundance of food %s and they also lived happy ever after.  " %(name,number,animal,sibling,name,number,animal,name,animal,food)

print story
