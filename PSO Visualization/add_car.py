
from car import Car

class addCar():
    
    def __init__(self, initial, loc):
        self.cars = []
        for i in range(initial):
            self.cars.append(Car(PVector(100,650)))
        
    def add_car(self):
        self.cars.append(Car(PVector(100,650)))
    
    def update(self):
        for i in self.cars:
            i.draw()
            i.update()
    
    def remove_car(self):
        del self.cars[-1]
