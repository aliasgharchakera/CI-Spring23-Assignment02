import random
from particleEmitter import particleEmitter


class Car(object):
    speed = 0
    def __init__(self,loc):
        self.img = loadImage('images/car.png')
        self.l = loc.get()
        self.velocity = PVector(random.uniform(0,1), random.uniform(-2,2))
        
    def draw(self):
        self.img.resize(200,100)
        self.render()
        # noTint()
        
    def render(self):
        imageMode(CENTER)
        image(self.img,self.l.x,self.l.y)
    
    def update(self):
        self.l.x += self.speed
        if (self.l.x > 1140):
            self.l.x = 0 
        return self.l.x
        # self.ps.update()
        # self.render()
        
    # def addCar(self):
    #     imageMode(CENTER)
    #     image(self.img, 0,650)
    

    
