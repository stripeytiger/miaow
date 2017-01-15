"""You are a cat. You are hungry. A short adventure game."""

# To-do list:
# Add a mechanism to get food.
# Add a mechanism to get in/out of patio doors.
# Add miaow method

import random

# Cat class with methods for interacting with the game
class Cat(object):
    location = ''

    def move(self, direction):
        new_loc = getattr(self.location, direction)
        if isinstance(new_loc, Room):
            self.location = new_loc
            print new_loc.description
            if new_loc == bob.location:
                print "There's a human here."
        elif isinstance(new_loc, str):
            print new_loc
        else:
            print "You cannot go " + direction + " from here."

    def look(self):
        print getattr(self.location, 'description')

    def sleep(self):
        if getattr(self.location, 'inside'):
            print "You sprawl languidly and drift into a peaceful doze. After several hours you awake refreshed. You are, however, hungry."
        else:
            print "It would be rather chilly to sleep here. You'd prefer to sleep somewhere you can properly unwind."

    # This sub-function checks if the thing being interacted with is in the same
    # room as the kitty. Returns the instance of the thing being interacted with
    # if found, else returns None
    def loc_item(self, item):
        for thing in self.location.things:
            if item in thing.synonyms:
                return thing
        return None

    def examine(self, item):
        thing = self.loc_item(item)
        if thing is not None:
            print thing.description
        else:
            print "You can't see any " + item + " here." 

    def jump(self, item):
        thing = self.loc_item(item)
        if thing is not None:
            if thing.jump is not None:
                self.location = thing.jump
                print thing.jump.description
            else:
                print "You can't jump on the " + item
        else:
            print "You can't see any " + item + " here." 

class Person(object):
    location = ''

    def set_loc(self, new_loc):
        old_loc = self.location
        if old_loc:
            old_loc.people.remove(self)
        new_loc.people.append(self)
        self.location = new_loc
        
    def move(self):
        if random.random() < 0.25:
            direction = random.choice(['n', 'e', 's', 'w'])
            new_loc = getattr(self.location, direction)
            if isinstance(new_loc, Room):
                if new_loc.inside:
                    self.set_loc(new_loc)
                    if kitty.location == new_loc:
                        print "A human wanders in."
                    
class Room(object):
    def __init__(self, description, inside):
        self.description = description
        self.inside = inside
        self.n = None
        self.e = None
        self.s = None
        self.w = None
        self.d = None
        self.u = None
        self.things = []
        self.people = []

    def addthing(self, item):
        item.location = self
        self.things.append(item)

class Thing(object):
    def __init__(self, synonyms, description, jump):
        self.synonyms = synonyms
        self.description = description
        self.jump = jump

class OnThing(Room):
    def __init__(self, description, inside):
        super(OnThing, self).__init__(description, inside)
        self.n = "You have to get down first."
        self.e = "You have to get down first."
        self.s = "You have to get down first."
        self.w = "You have to get down first."
    
# Room definitions
living = Room(
    "Living Room\nYou are in a warm room with soft stuff under your paws and comfy places to curl up. You can see a raised bed on legs. There are shiny barriers to the south which are sometimes open and a doorway to the east.",
    True)

kitchen = Room(
    "Kitchen\nYou are in the room you associate with food. There is a raised platform where humans put their food when they eat. You are not supposed to jump on it. There is a tall thing in the corner that sometimes has stuff on. Your food bowl is in the corner. There is a doorway to the west and a flappy thing to the east.",
    True)

path = Room(
    "Path\nA dark shadowy narrow place. You like it here. South is the bank, and the kitchen is to the west.",
    False)

bank = Room(
    "Bank\nAn overgrown area where you can creep under the shrubs. You sometimes find tasty mice here. To the west is the lawn, and to the north is the path.",
    False)

lawn = Room(
    "Lawn\nA wide open patch of grass with nowhere to hide. The patio is north and the bank is to the east.",
    False)

patio = Room(
    "Patio\nThis is an outside place, but with cold hard stuff under your paws. There's shiny stuff through which you can see the inside to the north, and sometimes get in. The lawn is to the south.",
    False)

onchair = OnThing(
    "On the chair\nIt's very cosy here. You start to purr.",
    True)

ontable = OnThing(
    "On the table\nAh, the forbidden zone! Just let them try to take this away from you.",
    True)

ondresser = OnThing(
    "On the dresser\nThere are tinfoil packets of food here. You cannot get into them, despite attempting to chew through.",
    True)

onwheelie = OnThing(
    "On the wheelie bin\nYou hunker down in the meatloaf position, and half-close your eyes, watching carefully in case the world should try something.",
    False)

living.e = kitchen
living.s = patio

kitchen.e = path
kitchen.w = living

path.s = bank
path.w = kitchen

bank.n = path
bank.w = lawn

lawn.n = patio
lawn.e = bank

patio.n = living
patio.s = lawn

onchair.d = living

ontable.d = kitchen

ondresser.d = kitchen

onwheelie.d = path


# Thing definitions
chair = Thing(
    ['chair', 'bed'],
    "It smells warm and comfortable.",
    jump = onchair)

table = Thing(
    ['table'],
    "You're not supposed to go up there. Apparently.",
    jump = ontable)

dresser = Thing(
    ['dresser', 'cupboard'],
    "Sometimes your food comes out of there.",
    jump = ondresser)

bowl = Thing(
    ['bowl', 'dish'],
    "It is empty.",
    jump = None)

wheelie = Thing(
    ['bin', 'wheelie'],
    "A useful high vantage point.",
    jump = onwheelie)

bush = Thing(
    ['bush', 'shrub'],
    "Smells like teen spirit. Or mouse. One or the other.",
    jump = None)

flowerpot = Thing(
    ['flowerpot', 'pot'],
    "It has some kind of green stuff in it.",
    jump = None)

# Location information of things
living.addthing(chair)
kitchen.addthing(table)
kitchen.addthing(dresser)
kitchen.addthing(bowl)
path.addthing(wheelie)
bank.addthing(bush)
patio.addthing(flowerpot)

# Input handling
def gamestep():
    input = raw_input(">")
    input_args = input.split()
    if input_args[0] in ['n', 'e', 's', 'w', 'd', 'u']:
        kitty.move(input)
    elif input_args[0] in ['l', 'look']:
        kitty.look()
    elif input_args[0] in ['sleep', 'z', 'zz', 'zzz', 'zzzz']:
        kitty.sleep()
    elif input_args[0] in ['x', 'examine']:
        kitty.examine(input_args[1])
    elif input_args[0] in ['jump']:
        kitty.jump(input_args[1])
    else:
        print "Sorry, I don't understand."
    bob.move()

bob = Person()
bob.set_loc(living)

kitty = Cat()
kitty.location = living
    
if __name__ == "__main__":
    print kitty.location.description
    while True:
        gamestep()

