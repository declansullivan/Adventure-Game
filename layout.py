import parser, usables, player

directional_dict = {"n": "north", "e": "east", "s": "south", "w": "west",
                    'nw': "northwest", "ne": "northeast", "sw": "southwest",
                    "se": "southeast"}

class Map:
    def __init__(self, name, vowel_sound=False):
        self.name = name
        self.vowel = 'n' if vowel_sound else ''

        self.message = ""
        self.description = ""

        self.n = None
        self.e = None
        self.s = None
        self.w = None
        self.nw = None
        self.ne = None
        self.sw = None
        self.se = None

        self.times_encountered = 0
        self.contents = {}

    def __repr__(self):
        links = [i for i in dir(self) if len(i) < 3 \
                    and "__" not in i \
                    and getattr(self, i) != None]
        num_links = len(links)
        plural = "s" if num_links != 1 else ""

        return "Map object {} with {} link{} to other Maps."\
            .format(self.name, num_links, plural)

    def __str__(self):
        return self.name
        

def build_map():
    mountaintop = Map("mountaintop")
    fork = Map("fork")
    bridge = Map("bridge")
    fortress = Map("fortress")
    ledge = Map("ledge")
    cave_entrance = Map("cave entrance")
    cave_exit = Map("cave exit")
    path = Map("winding path")
    plains = Map("plains")
    ruins = Map("ruins")
    beach = Map("beach")
    lighthouse = Map("lighthouse")
    jetty = Map("jetty")
    oil_rig = Map("oil rig", True)
    wasteland = Map("wasteland")
    graveyard = Map("graveyard")
    town = Map("abandoned town", True)
    waterfall = Map("waterfall")
    facility = Map("mining facility")
    quarry = Map("quarry")
    river = Map("river")

    ## ATTRIBUTES ##

    # Mountaintop
    mountaintop.s = fork
    mountaintop.contents.update({"stick": 1})

    # Fork
    fork.n = mountaintop
    fork.e = bridge
    fork.se = ledge
    fork.sw = path
    fork.w = cave_entrance

    # Bridge
    bridge.e = fortress
    bridge.w = fork

    # Fortress
    fortress.w = bridge

    # Ledge
    ledge.nw = fork

    # Cave Entrance
    cave_entrance.n = cave_exit
    cave_entrance.e = fork

    # Cave Exit
    cave_exit.ne = wasteland
    cave_exit.se = facility
    cave_exit.s = cave_entrance

    # Path
    path.ne = fork
    path.se = plains
    path.s = ruins
    path.sw = beach

    # Plains
    plains.nw = path
    plains.sw = ruins

    # Ruins
    ruins.n = path
    ruins.ne = plains
    ruins.nw = beach

    # Beach
    beach.n = lighthouse
    beach.ne = path
    beach.se = ruins

    # Lighthouse
    lighthouse.n = jetty
    lighthouse.s = beach

    # Jetty
    jetty.s = lighthouse

    # Oil Rig

    # Wasteland
    wasteland.e = graveyard
    wasteland.se = quarry
    wasteland.sw = cave_exit

    # Graveyard
    graveyard.s = town
    graveyard.sw = quarry
    graveyard.w = wasteland

    # Town
    town.n = graveyard
    town.sw = waterfall
    town.w = quarry

    # Waterfall
    waterfall.n = river
    waterfall.ne = river
    waterfall.e = river
    waterfall.se = river
    waterfall.s = river
    waterfall.sw = river
    waterfall.w = river
    waterfall.nw = river

    # Facility
    facility.n = quarry
    facility.ne = quarry
    facility.e = quarry
    facility.nw = quarry

    # Quarry
    quarry.ne = graveyard
    quarry.e = town
    quarry.s = facility
    quarry.sw = facility
    quarry.w = facility
    quarry.nw = wasteland

    # River
    river.n = plains
    river.nw = ruins

    return mountaintop


def movement(direction):
    new_loc = eval('world.' + direction)
    if new_loc == None:
        parser.retry("That is not a valid direction to move in.\n")
        return world
    else:
        print("You walk {} and arrive at a{} {}.".format(directional_dict.get(direction), \
                                                    new_loc.vowel, new_loc.name))
        return new_loc

def look(direction):
    loc = eval('world.' + direction)
    if loc == None:
        parser.retry("There is nothing in that direction.\n")
    else:
        print("To the {} you see a{} {}.".format(directional_dict.get(direction), \
                                                loc.vowel, loc.name))

world = build_map()

"""
"You stand at the summit of a mountain, \
the world stretched out beneath you. To the north you see jagged rocks \
jutting into the air. To the east you see an ocean battering the bottom of \
the mountain. Out in the ocean you see a lone rig with a flashing light. \
To the south, a pathway down the mountain marked with footprints that are \
definitely not yours. To the west, a strange looking fortress protected by a \
large wall and gate.", "A mountaintop with a panoramic view of the world."

A mountaintop with a panoramic view of the world.


"""
