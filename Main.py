from Classes import *
import sys, time

player = Adventurer(0,0,[])
rooms = []
gameOver = False

rooms.append(Room(0,0,[],[1,1,0,0],"dull concrete room"))                                                                                       #create room 0,0 (1)
rooms.append(Room(1,0,[],[1,0,0,1],"dull concrete room"))                                                                                       #create room 1,0 (2)
rooms.append(Room(0,1,[],[0,1,1,0],"flooded room, the water has a red tint to it. There is also a rope holding a door closed to the north"))    #create room 0,1 (3)
rooms.append(Room(1,1,[],[0,0,1,1],"worn down brick room"))                                                                                     #create room 1,1 (4)
rooms.append(Room(0,2,[],[0,0,1,0],"room made out of padded fabric. There is a scale on the north side of the room"))                           #create room 0,2 (5)
rooms.append(Room(1,2,[],[0,0,0,1],"room made out of padded fabric. The walls are dyed red with blood"))                                        #create room 1,2 (6)

#Add the items to the rooms
rooms[1].things.append(Thing("candle", "A lit candle, it has not melted at all.\n"))                #add the candle to room (2)
rooms[3].things.append(Thing("brick", "An ordinary brick. It looks like it weighs quite a lot.\n")) #add the brick to room (4)
rooms[4].things.append(Thing("dagger", "A bloodied dagger. The blood is still wet.\n"))             #add the dagger to room (5)
rooms[5].things.append(Thing("mask", "A blank white face mask.\n"))                                 #add the mask to room (6)

#funcion to print 1 letter at a time
def SlowPrint(words):
    print("\n")
    for letter in words:            #for each letter in the string
        sys.stdout.write(letter)    #store letter in buffer
        sys.stdout.flush()          #write everything in buffer
        time.sleep(0.029)           #wait for 0.29 seconds

#player input funcion
def Command(word):
    wordLC = word.lower()
    wordList = wordLC.split(" ")

    #go command
    if wordList[0] == "go" and len(wordList) == 2:
        if wordList[1] == "north" or wordList[1] == "n":    #if the player types go (n/north)
            Move(0)                                         #call the move function
            return                                          #exit function
        if wordList[1] == "east" or wordList[1] == "e":
            Move(1)
            return
        if wordList[1] == "south" or wordList[1] == "s":
            Move(2)
            return
        if wordList[1] == "west" or wordList[1] == "w":
            Move(3)
            return

    #look command
    if wordList[0] == "look" and len(wordList) == 1:                    #if the player only types look
        roomToLook = GetRoom(player.xpos, player.ypos)                  #get the current room the player is in
        SlowPrint(roomToLook.__str__())                                 #slow print the description of the current room
        return

    if wordList[0] == "look" and len(wordList) == 2:                    #if the player types look then another word
        roomTemp1 = GetRoom(player.xpos, player.ypos)                   #get the current room the player is in

        if CheckRoom(wordList[1],roomTemp1):                            #check the room for an object with the same name as the players input, if there is an object
            for obj in roomTemp1.things:                                #loop through the rooms objects
                if obj.name == wordList[1]:                             #find the object with the same name as the player input
                    SlowPrint(obj.desc)                                 #slow print the description of that object
            return

        if CheckPlayer(wordList[1]):                                    #same as above but loops through players inventory instead of the room
            for obj in player.things:
                if obj.name == wordList[1]:
                    SlowPrint(obj.desc)
            return
        SlowPrint("That item does not exist!")                          #if there is no item with that name in the room or player slow print this
        return

    #take command
    if wordList[0] == "take" and len(wordList) > 1:                     #if the player types take
        if CheckRoom(wordList[1],GetRoom(player.xpos,player.ypos)):     #check the current room for the item the player input, if there is an object
            TakeItem(wordList[1])                                       #take the item
            SlowPrint(f"You picked up the {wordList[1]}")               #slow print that they picked it up
            SlowPrint(player.__str__())                                 #slow print the players inventory
            return
        else:                                                           #else slow print item doesnt exist
            SlowPrint("That item does not exist!")
            return

    #drop command
    if wordList[0] == "drop" and len(wordList) > 1:                     #if the player types drop
        if CheckPlayer(wordList[1]):                                    #check if the player has the item
            DropItem(wordList[1])                                       #drop the item
            SlowPrint(f"You dropped the {wordList[1]}")                 #slow print that they dropped the item
            return
        else:                                                           #else slow print item doesnt exist
            SlowPrint("That item does not exist!")
            return
    #use command
    if wordList[0] == "use":                                            #if the player types use
        playerRoom = GetRoom(player.xpos, player.ypos)                  #get the current room

        if wordList[1] == "candle":                                     #if they type use candle
            if CheckPlayer("candle"):                                   #check if the player has a candle
                if playerRoom.xpos == 0 and playerRoom.ypos == 1:       #check if they are in the room which they can use the candle in
                    SlowPrint("You use the candle to burn the rope, a secret door appears to the north.")   #slow print that they have used the candle
                    rooms[2].desc = "flooded room, the water has a red tint to it. There is also a snapped rope that held the door to the north closed" #change the description of the room
                    playerRoom.doors[0] = 1                             #open a door to the north
                else:
                    SlowPrint("Nothing happens.")                       #else they are not in the right room
                return
            else:
                SlowPrint("You are not carrying that item.")            #else they are not carrying the candle
                return
        if wordList[1] == "brick":                                      #if they type use brick
            if CheckPlayer("brick"):                                    #repeat above
                if playerRoom.xpos == 0 and playerRoom.ypos == 2:
                    for obj in player.things:
                        if obj.name == "brick":
                            player.things.remove(obj)
                    SlowPrint("You put the brick on the scale, a secret door appears to the east.")
                    rooms[4].desc = "room made out of padded fabric. There is a scale balanced using a brick on the north side of the room"
                    playerRoom.doors[1] = 1
                else:
                    SlowPrint("Nothing happens.")
                return
            else:
                SlowPrint("You are not carrying that item.")
                return
        if wordList[1] == "dagger":                                     #if they type use dagger
            if CheckPlayer("dagger"):                                   #repeat above
                SlowPrint("Nothing happens.")
                return
            else:
                SlowPrint("You are not carrying that item.")
                return
        if wordList[1] == "mask":                                       #if they type use mask
            if CheckPlayer("mask"):                                     #repeat above
                if playerRoom.xpos == 1 and playerRoom.ypos == 2:
                    EndGame()
                    SlowPrint("You put the mask on. As you do the room turns pitch black and you hear the doors lock behind you. A voice whispers,\n ~no escape~.")
                else:
                    SlowPrint("Nothing happens.")
                return
            else:
                SlowPrint("You are not carrying that item.")
                return
        SlowPrint("You are not carrying that item.")
        return
    print("Invalid command")

#---FUNCTIONS---
#move function
def Move(direction):
    playerRoom = GetRoom(player.xpos, player.ypos)                      #get the current room
    if playerRoom.doors[direction] == 1:                                #if there is a door in the direction input
        if direction == 0:                                              #if the player wants to move north
            player.ypos += 1                                            #increase the players y value by 1
        if direction == 1:                                              #east
            player.xpos += 1
        if direction == 2:                                              #south
            player.ypos -= 1
        if direction == 3:                                              #west
            player.xpos -= 1
        SlowPrint("You move into a diffrent room \n")
        return True
    SlowPrint("You cannot move in that direction! \n")
    return False

#return room function
def GetRoom(roomx, roomy):
    for room in rooms:                                                  #loops through all the rooms
        if roomx == room.xpos and roomy == room.ypos:                   #return the room with the same x,y value as the input
            return room

#check room for specific object function
def CheckRoom(thingToCheck, room):
    if len(room.things) > 0:                                            #if the room contains 1 or more objects
        for obj in room.things:                                         #loop through objects in the room
            if obj.name == thingToCheck:                                #return true if there is an object with the same name as the input
                return True
        return False                                                    #return false as there is no object with the same name
    else:
        return False                                                    #return false as there is no objects in the room

#check the player for specific object function
def CheckPlayer(thingToCheck):
    if len(player.things) > 0:                                          #if the players inventory is not empty
        for obj in player.things:                                       #loop through the player
            if obj.name == thingToCheck:                                #return true if there is an object with the same name as the input
                return True
        return False                                                    #return false as there is no object with the same name
    else:
        return False                                                    #return false as there is no objects in the players inventory

#take item function
def TakeItem(itemName):
    roomTemp2 = GetRoom(player.xpos, player.ypos)                       #get current room
    for obj in roomTemp2.things:                                        #loop through the rooms items
        if obj.name == itemName:                                        #if an item name matches the input
            player.things.append(obj)                                   #add it to the players inventory
            roomTemp2.things.remove(obj)                                #remove it from the room

#drop item function
def DropItem(itemName):
    roomTemp3 = GetRoom(player.xpos, player.ypos)                       #get current room
    for obj in player.things:                                           #loop through the items in the players inventory
        if obj.name == itemName:                                        #if an item name matches the input
            roomTemp3.things.append(obj)                                #add it to the room
            player.things.remove(obj)                                   #remove it from the players inventory

#end game function
def EndGame():
    global gameOver
    gameOver = True

#input loop
while True:
    Command(input(""))
    print("\n")
    if gameOver == True:
        break
