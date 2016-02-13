def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game:
Poork
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
    #print the player's current status
    print("---------------------------")
    print("You are in the " + rooms[currentRoom]["name"])
    #print the current inventory
    print("Inventory : " + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    print("---------------------------")
    
#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other room positions
rooms = {

            1 : {  "name"  : "Hall" ,
                   "south" : 2 ,
                   "east"  : 3 ,
                   "west"  : 7 ,
                   "go-gadget": 4 , 
                } ,        

            2 : {  "name"  : "Kitchen" ,
                   "north" : 1,
                   "item"  : "monster"
                },
            3 : {  "name"  : "Dining room",
                   "west"  : 1,
                   "south" : 4,
                   "east"  : 9
                },
            4 : {  "name"  : "bed room",
                   "west"  : 2,
                   "east"  : 5,
                   "item"  : "key"
                },
            5 : {  "name" : "Cupboard",
                   "east" : 6,
                   "item" : "feather",
                   "west" : 4
                },
            6 : {  "name" : "Narnia",
                   "item" : "sword",
                   "home" : 4
                },
            7 : {  "name" : "Porch",
                   "item" : "Shoehorn",
                   "east" : 1
                },
            8 : {  "name" : "Servants' Quarters",
                   "item" : "Soot",
                   "east" : 2,
                   "north": 7
                },
            9 : {  "name" : "Side Door",
                   "west" : 3,
                   "east" : 10
                },
            10 : { "name" : "Garden",
                   "west" : 9,
                   "south": 11
                },
            11 : { "name" : "Wood",
                   "north": 10,
                   "item" : "twig"
                }
      }
#start the player in room 1
currentRoom = 1


def roomHasMonster():
    return "item" in rooms[currentRoom] and "monster" in rooms[currentRoom]["item"]

def playerHasSword():
    return "sword" in inventory

def playerHasFeather():
    return "feather" in inventory


showInstructions()

#loop infinitely
while True:

    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = raw_input(">").lower().split()

    #if they type 'go' first
    if move[0] == "go":
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
            #there is no door (link) to the new room
        else:
            print("You can't go that way!")

    #if they type 'get' first
    if move[0] == "get" :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + " got!")
            #delete the item from the room
            del rooms[currentRoom]["item"]
            #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print("Can't get " + move[1] + "!")

    if roomHasMonster() and playerHasSword() :
        del rooms[currentRoom]["item"]
        print ("You have killed the monster!")
        print ('''You sense that this monster was not the only one...''')
        
    
    if roomHasMonster()  and not playerHasSword() and not playerHasFeather():
        print("A monster has got you... GAME OVER!")
        print("press any key to quit")
        input()
        break

    if roomHasMonster() and playerHasFeather() :
        del rooms[currentRoom]["item"]
        print("You tickled the monster")
        print("The monster runs away into the darkness...")

    
        


