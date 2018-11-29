from Classes import *
import sys, time

player = Adventurer(0,0,[])
rooms = []

rooms.append(Room(0,0,[],[1,1,0,0],"dull concrete room"))                       #Room 0,0 (1)
rooms.append(Room(1,0,[],[1,0,0,1],""))                                         #Room 1,0 (2)
rooms.append(Room(0,1,[],[0,1,1,0],""))                                         #Room 0,1 (3)
rooms.append(Room(1,1,[],[0,0,1,1],""))                                         #Room 1,1 (4)
rooms.append(Room(0,2,[],[0,0,1,0],""))                                         #Room 0,2 (5)
rooms.append(Room(1,2,[],[0,0,0,1],""))                                         #Room 1,2 (6)

rooms[1].things.append(Thing("candle", "A lit candle, it has not melted at all.\n"))
rooms[3].things.append(Thing("brick", "An ordinary brick. It looks like it weighs quite a bit.\n"))

def SlowPrint(words):
    print("\n")
    for letter in words:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.029)

def Command(word):
    wordLC = word.lower()
    wordList = wordLC.split(" ")

    if wordList[0] == "go":
        if wordList[1] == "north" or wordList[1] == "n":
            Move(0)
        if wordList[1] == "east" or wordList[1] == "e":
            Move(1)
        if wordList[1] == "south" or wordList[1] == "s":
            Move(2)
        if wordList[1] == "west" or wordList[1] == "w":
            Move(3)

    if wordList[0] == "look" and len(wordList) <= 1:
        roomToLook = Room(0,0,[],[],"")
        roomToLook = GetRoom(player.xpos, player.ypos)
        SlowPrint(roomToLook.__str__())
    if wordList[0] == "look" and len(wordList) > 1:
        roomTemp1 = GetRoom(player.xpos, player.ypos)
        for obj in roomTemp1.things:
            if obj.name == wordList[1]:
                SlowPrint(obj.desc)
        for obj in player.things:
            if obj.name == wordList[1]:
                SlowPrint(obj.desc)

    if wordList[0] == "take":
        TakeItem(wordList[1])
        SlowPrint(player.__str__())

    if wordList[0] == "drop":
        DropItem(wordList[1])

    if wordList[0] == "use":
        playerRoom = GetRoom(player.xpos, player.ypos)

        if wordList[1] == "candle":
            if playerRoom.xpos == 0 and playerRoom.ypos == 1:
                SlowPrint("You use the candle to burn the rope, a secret door appears to the north.")
                playerRoom.doors[0] = 1
            else:
                SlowPrint("Nothing happens.")
        if wordList[1] == "brick":
            if playerRoom.xpos == 0 and playerRoom.ypos == 2:
                SlowPrint("You put the brick on the scale, a scret door appears to the east.")
                playerRoom.doors[1] = 1
            else:
                SlowPrint("Nothing happens.")

def Move(direction):
    playerRoom = rooms[0]
    playerRoom = GetRoom(player.xpos, player.ypos)
    if playerRoom.doors[direction] == 1:
        if direction == 0:
            player.ypos += 1
        if direction == 1:
            player.xpos += 1
        if direction == 2:
            player.ypos -= 1
        if direction == 3:
            player.xpos -= 1
        SlowPrint("You move into a diffrent room \n")
        return True
    SlowPrint("You cannot move in that direction! \n")
    return False

def GetRoom(roomx, roomy):
    for room in rooms:
        if roomx == room.xpos and roomy == room.ypos:
            return room

def CheckRoom(thingToCheck, room):
    if room.things > 0:
        for obj in room.things:
            if obj == thingToCheck:
                return True
        return False
    else:
        return False

def CheckPlayer(thingToCheck):
    if player.things > 0:
        for obj in player.things:
            if obj == thingToCheck:
                return True
        return False
    else:
        return False

def TakeItem(itemName):
    roomTemp2 = GetRoom(player.xpos, player.ypos)
    for obj in roomTemp2.things:
        if obj.name == itemName:
            player.things.append(obj)
            roomTemp2.things.remove(obj)

def DropItem(itemName):
    roomTemp3 = GetRoom(player.xpos, player.ypos)
    for obj in player.things:
        if obj.name == itemName:
            roomTemp3.things.append(obj)
            player.things.remove(obj)

while True:
    Command(input(""))
    print("\n")
