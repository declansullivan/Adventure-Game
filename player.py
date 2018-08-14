import layout

class Player:
    def __init__(self):
        # User Defined
        self.name = None
        self.age = None
        self.place = None

        # Default
        self.inventory = {}
        self.hand = {}
        self.capacity = 10
        self.sub_capacity = 40
        self.health = 100
        self.status = "Healthy"
        self.status_timer = 0

    def assign_values(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def get_hand(self):
        if self.hand:
            return list(self.hand.keys())[0]

    def check_hand(self):
        if self.hand:
            print("You are holding a {}.".format(self.get_hand()))
        else:
            print("Your hands are empty.")

    def check_inventory(self):
        if self.inventory:
            print("Inventory: {}.".format(self.inventory))
        else:
            print("Your inventory is empty.")

    def check_ground(self):
        if layout.world.contents:
            print("Around you is: {}".format(layout.world.contents))
        else:
            print("There is nothing around you.")

    def empty_hand(self):
        if self.hand:
            print("You put away your {}.".format(self.get_hand()))
            self.inventory.update(self.hand)
            self.hand.clear()
        else:
            print("You aren't holding anything.")

    def empty_inventory(self):
        if self.inventory:
            print("You drop everything.")
            print("It's a bold move Cotton, let's see if it pays off.")
            layout.world.contents.update(self.inventory)
            self.inventory.clear()
        else:
            print("You have nothing to drop.")

    def drop(self, item):
        if self.hand and self.hand.get(item):
            print("You drop your {}.".format(item))
            layout.world.contents.update(self.hand)
            self.hand.clear()
        elif self.inventory and self.inventory.get(item):
            print("You drop your {}.".format(item))
            layout.world.contents.update({item: self.inventory.get(item)})
            self.inventory.pop(item)
        else:
            print("You don't have that.")

    def equip(self, item):
        if not self.inventory:
            print("You have nothing to equip.")
        elif not self.inventory.get(item):
            print("You don't have that.")
        elif self.hand.get(item):
            print("You are already holding that.")
        elif self.inventory.get(item):
            if self.hand:
                print("You put away your {}.".format(self.get_hand()))
                self.inventory.update(self.hand)
                self.hand.clear()

            self.hand.update({item: self.inventory.get(item)})
            self.inventory.pop(item)

            print("You take out your {}.".format(item))

    def take(self, item):
        found = False
        if list(layout.world.contents):
            if item == 'all':
                self.inventory.update(layout.world.contents)
                layout.world.contents.clear()
                print("You take everything.")
            else:
                for i in list(layout.world.contents):
                    if item == i:
                        print(i)
                        self.inventory.update({i: layout.world.contents.get(i)})
                        layout.world.contents.pop(i)
                        print("You take the {}.".format(i))
                        found = True
                if not found:
                    print("There is no {} here.".format(item))
        else:
            print("There is nothing to take from here.")

    def effect(self):
        if self.status_timer > 0:
            if self.status == "Poisoned":
                self.health -= 2
                self.status_timer -= 1
            elif self.status == "Blinded":
                self.status_timer -= 1
        else:
            self.status = "Healthy"

    def __repr__(self):
        return "Player Object: " + self.name

    def __str__(self):
        out = "Player: " + self.name + "\n"
        out += "Age: " + str(self.age) + "\n"
        out += "Place: " + self.place
        return out