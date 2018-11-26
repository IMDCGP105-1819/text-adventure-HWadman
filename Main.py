from Classes import *
import sys, time

player = Adventurer(0,0,[])
rooms = []

rooms.append(Room(0,0,[],[0,1,0,0]))                                            #Room 0,0 (1)
rooms.append(Room(1,0,[],[1,1,0,1]))                                            #Room 1,0 (2)
rooms.append(Room(2,0,[],[0,1,0,1]))                                            #Room 2,0 (3)
rooms.append(Room(3,0,[],[1,0,0,1]))                                            #Room 3,0 (4)
rooms.append(Room(0,1,[],[1,1,0,0]))                                            #Room 0,1 (5)
rooms.append(Room(1,1,[],[0,1,1,1]))                                            #Room 1,1 (6)
rooms.append(Room(2,1,[],[0,1,0,1]))                                            #Room 2,1 (7)
rooms.append(Room(3,1,[],[0,0,1,1]))                                            #Room 3,1 (8)
rooms.append(Room(0,2,[],[0,1,1,0]))                                            #Room 0,2 (9)
rooms.append(Room(1,2,[],[0,1,0,1]))                                            #Room 1,2 (10)
rooms.append(Room(2,2,[],[0,1,0,1]))                                            #Room 2,2 (11)
rooms.append(Room(3,2,[],[0,0,0,1]))                                            #Room 3,2 (12)

def SlowPrint(words):
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

    if wordList[0] == "look":
        print("look here")

def Move(direction):
    playerRoom = rooms[0]
    for room in rooms:
        if player.xpos == room.xpos and player.ypos == room.ypos:
            playerRoom = room

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

while True:
    Command(input(""))
    print(player)
    sudobreak = input("BREAK?:")
    if sudobreak == "y":
        break

#SlowPrint("My name is jeff and I am a bard traveling the world to share my tales! Who are you? \n")
