class Vehicle:

    #constructor
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print('Moves along')
    
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")

#object
my_car = Vehicle('VW','Golf 7')

my_car.get_make_model()
my_car.moves()

other_car = Vehicle('Skoda','Superb')
other_car.get_make_model()
other_car.moves()

#inheritance
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        #inherit from Vehicle class
        super().__init__(make,model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along')

class Truck(Vehicle):
    def moves(self):
        print('Rumbles along')

#empty class
class GolfCart(Vehicle):
    pass

cessna = Airplane('Cessna','Skyhawk', 'MI-12345')
mack = Truck('Mack','Pinnacle')
golfwagon = GolfCart('Honda','JJ120')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')
#polymorphism

for v in (my_car, other_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()