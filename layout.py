import parser, usables, player

class Map:
    def __init__(self, name):
        self.name = name
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
    mountaintop = Map("Mountaintop")
    fork = Map("Fork")
    bridge = Map("Bridge")
    fortress = Map("Fortress")
    ledge = Map("Ledge")
    cave_entrance = Map("Cave Entrance")
    cave_exit = Map("Cave Exit")
    path = Map("Winding Path")
    plains = Map("Plains")
    ruins = Map("Ruins")
    beach = Map("Beach")
    lighthouse = Map("Lighthouse")
    jetty = Map("Jetty")
    oil_rig = Map("Oil Rig")
    wasteland = Map("Wasteland")
    graveyard = Map("Graveyard")
    town = Map("Abandoned Town")
    waterfall = Map("Waterfall")
    facility = Map("Mining Facility")
    quarry = Map("Quarry")
    river = Map("River")

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
    print('world.' + direction)
    new_loc = eval('world.' + direction)
    if new_loc == None:
        parser.retry("That is not a valid direction to move in.\n")
        return world
    else:
        print(new_loc)
        print(repr(new_loc))
        return new_loc


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
