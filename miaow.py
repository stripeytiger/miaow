
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
kitchen.description = "This is the kitchen."
kitchen.objects = ['table', 'dresser']

path = Room()
path.description = "This is the path."
path.objects = ['bin']

bank = Room()
bank.description = "This is the bank."
bank.objects = ['bush']

lawn = Room()
lawn.description = "This is the lawn."
lawn.objects = None

patio = Room()
patio.description = "This is the patio."
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
    input = raw_input("Do something:")
    if input in ['n', 'e', 's', 'w']:
        kitty.move(input)

bob = Person()
bob.location = living

kitty = Cat()
kitty.location = living
    
if __name__ == "__main__":
    prompt()

