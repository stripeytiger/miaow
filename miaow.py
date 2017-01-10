
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
        print "You sprawl languidly and drift into a peaceful doze. After several hours you awake refreshed. You are, however, hungry."
        prompt()

class Person(object):
    location = ''

class Room(object):
    name = ''
    description = ''
    exits = ''
    cat = ''
    objects = ''
    people = ''

living = Room()
living.description = "Living Room\nYou are in a warm room with soft stuff under your paws and comfy places to curl up. You can see a raised cat bed on legs. There are shiny barriers to the south which are sometimes open and a doorway to the east."
living.objects = ['chair']

kitchen = Room()
kitchen.description = "Kitchen\nYou are in the room you associate with food. There is a raised platform where humans put their food when they eat. You are not supposed to jump on it. There is a tall thing in the corner that sometimes has stuff on. Your food bowl is in the corner. There is a doorway to the west and a flappy thing to the east."
kitchen.objects = ['table', 'dresser', 'bowl']

path = Room()
path.description = "Path\nA dark shadowy narrow place. You like it here. South is the bank, and the kitchen is to the west."
path.objects = ['bin']

bank = Room()
bank.description = "Bank\nAn overgrown area where you can creep under the shrubs. You sometimes find tasty mice here. To the west is the lawn, and to the north is the path."
bank.objects = ['bush']

lawn = Room()
lawn.description = "Lawn\nA wide open patch of grass with nowhere to hide. The patio is north and the bank is to the east."
lawn.objects = None

patio = Room()
patio.description = "Patio\nThis is an outside place, but with cold hard stuff under your paws. There's shiny stuff through which you can see the inside to the north, and sometimes get in. The lawn is to the south."
patio.objects = ['flowerpot']

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

def prompt():
    input = raw_input(">")
    if input in ['n', 'e', 's', 'w']:
        kitty.move(input)
    if input in ['l', 'look']:
        kitty.look()
    if input in ['sleep', 'z', 'zz', 'zzz', 'zzzz']:
        kitty.sleep()

bob = Person()
bob.location = living

kitty = Cat()
kitty.location = living
    
if __name__ == "__main__":
    print kitty.location.description
    prompt()

