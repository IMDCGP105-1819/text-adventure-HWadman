class Adventurer(object):
    def __init__(self, xpos, ypos, things):
        self.xpos = xpos;
        self.ypos = ypos;
        self.things = things;

    def __str__(self):
        list = " ".join(self.things)
        return(f"You are currently in position {self.xpos},{self.ypos} and are carrying {list}")


class Room(object):
    def __init__(self, xpos, ypos, things, doors):
        self.xpos = xpos;
        self.ypos = ypos;
        self.things = things;
        self.doors = doors;

class Thing(object):
    def __init__(self, name, desc, onUse):
        self.name = name;
        self.desc = desc;
        self.onUse = onUse;
