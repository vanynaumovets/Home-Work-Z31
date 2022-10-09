class Auto:
    brand = None
    age = None
    color = None
    mark = None
    weight = None
    move = "attention"


    def __init__(self, brand, age,  color, mark, weight, move):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight
        self.move = move

    def get_data(self):
     print ("brand:", self.brand, ". age:", self.age, ". color:", self.color, ". mark:", self.mark,
            ". weight:", self.weight, self.move)

Auto1 = Auto("WAG", "13", "black", "audi", "2450", move= "attention" )
Auto1.get_data()

class car(Auto):
    max_speed = None

    def __init__(self, max_speed):
        # super(car, self).__init__(move)
        self.max_speed = max_speed



    def get_data(self):
         print("max speed:", self.max_speed)
    pass
class truck(Auto):
    max_load = None
    def __init__(self, max_load):
        # //super(truck, self).__init__(move)
        self.max_load = max_load




    def get_data(self):
        print("max Load:", self.max_load)
    pass
Car = car(231)
Car.max_speed()






