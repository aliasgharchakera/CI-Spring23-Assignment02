
from car import Car

class addCar():
    
    def __init__(self, initial, loc):
        self.cars = []
        for i in range(initial):
            self.cars.append(Car(PVector(100,650)))
        
    def add_car(self):
        if len(self.cars) < 3:
            self.cars.append(Car(PVector(100,650)))
    
    def update(self):
        for i in self.cars:
            i.draw()
            i.update()
    
    def remove_car(self):
        if (len(self.cars) > 0):
            del self.cars[-1]
