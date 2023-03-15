import random
from smokeParticle import smokeParticle

class particleEmitter(object):
    
    def __init__(self,num,img,loc):
        self.loc = loc.get()
        self.particles = []
        self.img = img
        for i in range(num):
            self.particles.append(smokeParticle(self.loc, self.img))

    def add_particle(self,x,y):
        self.particles.append(smokeParticle(PVector(x,y), self.img))
        
    def update(self):
       for i in reversed(range(len(self.particles))):
           p = self.particles[i]
           p.render()
           p.update()
           if p.isDead():
               del self.particles[i] 
    
    def decreaseGravity(self):
        # for i in self.particles:
        #     i.gravity = -0.05
        for i in reversed(range(len(self.particles))):
            p = self.particles[i]
            p.decreaseGravity()

    def increaseGravity(self):
        for i in reversed(range(len(self.particles))):
            p = self.particles[i]
            p.increaseGravity()
            
    def getParticles(self):
        return self.particles
        
        
