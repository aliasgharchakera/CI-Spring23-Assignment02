import random
from particleEmitter import particleEmitter


class Car(object):

    def __init__(self,loc):
        self.img = loadImage('images/car.png')
        self.l = loc.get()
        # self.cx = l.x
        # self.cy = l.y
        # initial = 1
        # img = loadImage("images/texture_3.png")
        # self.ps = particleEmitter(initial, img, PVector(self.l.x-100, 680))
        self.velocity = PVector(random.uniform(0,1), random.uniform(-2,2))
        
    def draw(self):
        self.img.resize(200,100)
        self.render()
        
    def render(self):
        imageMode(CENTER)
        image(self.img,self.l.x,self.l.y)
    
    def update(self):
        self.l.x += 10
        # self.ps.add_particle(self.l.x-120, 680)
        # self.ps.update()
        if (self.l.x > 1140):
            self.l.x = 0 
        return self.l.x
        # self.ps.update()
        # self.render()

    
