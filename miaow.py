
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

class Room(object):
    name = ''
    description = ''
    exits = ''
    cat = ''

living = Room()
living.description = "This is the living room."

kitchen = Room()
kitchen.description = "This is the kitchen."

living.n = None
living.e = kitchen
living.s = None
living.w = None

kitchen.n = None
kitchen.e = None
kitchen.s = None
kitchen.w = living

def prompt():
    input = raw_input("Do something:")
    if input in ['n', 'e', 's', 'w']:
        kitty.move(input)

kitty = Cat()
kitty.location = living
    
if __name__ == "__main__":
    prompt()

