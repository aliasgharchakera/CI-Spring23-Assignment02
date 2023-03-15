import random
from smokeParticle import smokeParticle

class particleEmitter(object):
    
    def __init__(self,num,img,loc):
        self.loc = loc.get()
        self.particles = []
        self.img = img
        self.it = 1
        for i in range(num):
            self.particles.append(smokeParticle(self.loc, self.img,1))

    def add_particle(self,x,y):
        for i in range((self.it)):
            self.particles.append(smokeParticle(PVector(x,y), self.img,1))
        
    def update(self):
       for i in reversed(range(len(self.particles))):
           p = self.particles[i]
           p.render()
           p.update()
           if p.isDead():
               del self.particles[i] 
    
    # def decreaseGravity(self):
    #     # for i in self.particles:
    #     #     i.gravity = -0.05
    #     for i in reversed(range(len(self.particles))):
    #         p = self.particles[i]
    #         p.decreaseGravity()

    # def increaseGravity(self):
    #     for i in reversed(range(len(self.particles))):
    #         p = self.particles[i]
    #         p.increaseGravity()
            
    def getParticles(self):
        return self.particles
        
        
