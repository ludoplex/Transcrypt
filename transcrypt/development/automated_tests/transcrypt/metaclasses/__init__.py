from org.transcrypt.stubs.browser import __pragma__

class UppercaserMeta (type):
    def __new__(cls, name, bases, attribs):
        __pragma__ ('jsiter')       # Translate for ... in directly to JavaScript for ... in ... and translate {} to bare {} rather than to dict {}
        upperAttribs = {
            attribKey
            if attribKey.startswith('__')
            else attribKey.upper(): attribs[attribKey]
            for attribKey in attribs
        }
        __pragma__ ('nojsiter')

        return type.__new__(cls, name, bases, upperAttribs)

class Uppercaser (metaclass = UppercaserMeta):
    pass
    
class Animal (Uppercaser):
    class Thoughts:
        quantity = 7

    # Limitation: no destructuring assignment if metaclass has to alter attributes
    color = 'Brown'
    state = 'Moving'

    def move (self):
        return 'Move'

class Plant (Uppercaser):
    class Thoughts:
        quantity = 6

    color = 'Green'
    state = 'Growing'

    def grow (self):
        return 'Grow'
        
class Stone:
    class Thoughts:
        quantity = 5

    color = 'Gray'
    
    def be (self):
        return ('Being')

def run (autoTester):
    animal = Animal ()
    autoTester.check (animal.THOUGHTS.quantity, Animal.COLOR, animal.COLOR, animal.MOVE ())
    
    plant = Plant ()
    autoTester.check (plant.THOUGHTS.quantity, Plant.COLOR, plant.COLOR, plant.GROW ())
    
    stone = Stone ()
    autoTester.check (stone.Thoughts.quantity, Stone.color, stone.color, stone.be ())
    