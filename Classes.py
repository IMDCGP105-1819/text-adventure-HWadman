class Adventurer(object):
    def __init__(self, xpos, ypos, things):
        self.xpos = xpos;
        self.ypos = ypos;
        self.things = things;

    def __str__(self):
        list = []
        for thing in self.things:
            list.append(thing.name)
        return(f"You are currently carrying {list}")


class Room(object):
    def __init__(self, xpos, ypos, things, doors, desc):
        self.xpos = xpos;
        self.ypos = ypos;
        self.things = things;
        self.doors = doors;
        self.desc = desc;

    def __str__(self):
        out = ""
        out2 = ""
        out3 = ""
        out += f"You are in a {self.desc}. "
        if self.doors[0] == 1:
            if out2 == "":
                out2 += "There is a door to the north"
            else:
                out2 += ", north"
        if self.doors[1] == 1:
            if out2 == "":
                out2 += "There is a door to the east"
            else:
                out2 += ", east"
        if self.doors[2] == 1:
            if out2 == "":
                out2 += "There is a door to the south"
            else:
                out2 += ", south"
        if self.doors[3] == 1:
            if out2 == "":
                out2 += "There is a door to the west"
            else:
                out2 += ", west"
        if len(self.things) > 0:
            out3 += "There is a "
            for obj in self.things:
                out3 += obj.name
                if len(self.things) != 1:
                    out3 += ", "
                else:
                    out3+= " "
            out3 += "in the room. "
        out += out3
        out += out2
        out += ".\n"
        return(out)

class Thing(object):
    def __init__(self, name, desc):
        self.name = name;
        self.desc = desc;

    def __str__(self):
        return self.desc
