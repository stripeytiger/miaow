"""You are a cat. You are hungry. A short adventure game."""

# To-do list:
# Perhaps I need to do ontop rooms as a sub-category of rooms? With inherited characteristics, plus if user tries to go N/S/E/W they say no
# Add a function which adds item to room as well as room to item
# Add a human. The human should move between rooms in the house.
# Add the capability to jump on things.
# Add a mechanism to get food.
# Add a mechanism to get in/out of patio doors.
# Add miaow method

# Cat class with methods for interacting with the game
class Cat(object):
    location = ''

    def move(self, direction):
        new_loc = getattr(self.location, direction)
        if new_loc is not None:
            self.location = new_loc
            print new_loc.description
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

class Room(object):
    name = ''
    cat = ''
    people = ''
    def __init__(self, description, inside):
        self.description = description
        self.inside = inside

class Thing(object):
    def __init__(self, synonyms, description, jump):
        self.synonyms = synonyms
        self.description = description
        self.jump = jump

class OnThing(Room):
    people = None
    
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

living.n = None
living.e = kitchen
living.s = patio
living.w = None

kitchen.n = None
kitchen.e = path
kitchen.s = None
kitchen.w = living

path.n = None
path.e = None
path.s = bank
path.w = kitchen

bank.n = path
bank.e = None
bank.s = None
bank.w = lawn

lawn.n = patio
lawn.e = bank
lawn.s = None
lawn.w = None

patio.n = living
patio.e = None
patio.s = lawn
patio.w = None

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
chair.location = living
table.location = kitchen
dresser.location = kitchen
bowl.location = kitchen
wheelie.location = path
bush.location = bank
flowerpot.location = patio

living.things = [chair]
kitchen.things = [table, dresser, bowl]
path.things = [wheelie]
bank.things = [bush]
lawn.things = None
patio.things = [flowerpot]

# Input handling
def prompt():
    input = raw_input(">")
    input_args = input.split()
    if input_args[0] in ['n', 'e', 's', 'w']:
        kitty.move(input)
    if input_args[0] in ['l', 'look']:
        kitty.look()
    if input_args[0] in ['sleep', 'z', 'zz', 'zzz', 'zzzz']:
        kitty.sleep()
    if input_args[0] in ['x', 'examine']:
        kitty.examine(input_args[1])
    if input_args[0] in ['jump']:
        kitty.jump(input_args[1])

bob = Person()
bob.location = living

kitty = Cat()
kitty.location = living
    
if __name__ == "__main__":
    print kitty.location.description
    while True:
        prompt()

