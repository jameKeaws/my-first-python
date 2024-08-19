class Vehicle():
    # By convention, all of the methods in a class, take the reference to the object as the 1st parameter
    # You could call it self, theThing, or whatever
    def __init__(self, body_style):
        print("Call the super().__init__() at Vehicle")
        self.body_style = body_style
        
    def drive(self, speed):
        print("Call the super().drive() at Vehicle")
        self.mode = "driving"
        self.speed = speed
        
        

class Car(Vehicle):
    def __init__(self, engine_type):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine_type = engine_type
        
    def drive(self, speed):
        super().drive(speed)
        print(f'Driving my {self.engine_type} Car at {self.speed}')
        
class Motorcycle(Vehicle):
    def __init__(self, engine_type, has_side_car):
        # Object reference passing is implied, so no need to pass in self
        super().__init__("Motorcycle")
        self.engine_type = engine_type
        self.has_side_car = has_side_car
        if has_side_car == True:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
    
    def drive(self, speed):
        super().drive(speed)
        print(f'Driving my {self.engine_type} Motorcycle at {self.speed}')
        
    
car1 = Car("gas")
car2 = Car("electric")
moto1 = Motorcycle("gas", True)
moto1.drive(20)

print(f'moto1 engine_type : {moto1.engine_type} and moto1 body_style is {moto1.body_style} ')
        
        