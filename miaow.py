"""You are a cat. You are hungry. A short adventure game."""

# To-do list:
# Add a function which adds item to room as well as room to item
# Add a human. The human should move between rooms in the house.
# Add the capability to jump on things.
# Add a mechanism to get food.
# Add a mechanism to get in/out of patio doors.

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
        prompt()

    def look(self):
        print getattr(self.location, 'description')
        prompt()

    def sleep(self):
        if getattr(self.location, 'inside'):
            print "You sprawl languidly and drift into a peaceful doze. After several hours you awake refreshed. You are, however, hungry."
        else:
            print "It would be rather chilly to sleep here. You'd prefer to sleep somewhere you can properly unwind."
        prompt()

    def examine(self, item):
        thing = self.loc_item(item)
        if thing is not None:
            print thing.description
        else:
            print "You can't see any " + item + " here." 
        prompt()        

    # This sub-function checks if the thing being interacted with is in the same
    # room as the kitty. Returns the instance of the thing being interacted with
    # if found, else returns None
    def loc_item(self, item):
        for thing in self.location.things:
            if item in thing.synonyms:
                return thing
        return None
                

class Person(object):
    location = ''

class Room(object):
    name = ''
    exits = ''
    cat = ''
    people = ''
    def __init__(self, description, inside):
        self.description = description
        self.inside = inside

class Thing(object):
    def __init__(self, synonyms, description, jumpable):
        self.synonyms = synonyms
        self.description = description
        self.jumpable = jumpable

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

# Thing definitions
chair = Thing(
    ['chair', 'bed'],
    "It smells warm and comfortable.",
    True)

table = Thing(
    ['table'],
    "You're not supposed to go up there. Apparently.",
    True)

dresser = Thing(
    ['dresser', 'cupboard'],
    "Sometimes your food comes out of there.",
    True)

bowl = Thing(
    ['bowl', 'dish'],
    "It is empty.",
    False)

wheelie = Thing(
    ['bin', 'wheelie'],
    "A useful high vantage point.",
    True)

bush = Thing(
    ['bush', 'shrub'],
    "Smells like teen spirit. Or mouse. One or the other.",
    False)

flowerpot = Thing(
    ['flowerpot', 'pot'],
    "It has some kind of green stuff in it.",
    False)

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

bob = Person()
bob.location = living

kitty = Cat()
kitty.location = living
    
if __name__ == "__main__":
    print kitty.location.description
    prompt()

