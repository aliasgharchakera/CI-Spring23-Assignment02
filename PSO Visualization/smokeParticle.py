import random

class smokeParticle(object):
    r = 0
    g = 0
    b = 0
    lifespan = 100
    
    def __init__(self, l, img, num):
        self.loc = l.get()
        self.velocity = PVector(random.uniform(0,1), random.uniform(-1,-2))
        self.acceleration = PVector(0,0)
        self.gravity = 0.5
        self.img = img
        self.num = num
        # self.lifespan = 100
        # self.r = 0
        # self.g = 0
        # self.b = 0
        
    def update(self):
        self.velocity.add(self.acceleration)
        self.velocity.y -= self.gravity
        self.loc.x += self.velocity.x
        self.loc.y += self.velocity.y
        noTint()
        
    def render(self):
        imageMode(CENTER)
        tint(self.r,self.g,self.b,self.lifespan)
        image(self.img, self.loc.x, self.loc.y)
    
    def isDead(self):
        return self.lifespan <= 0.0
        
        
