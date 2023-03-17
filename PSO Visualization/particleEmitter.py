import random
from smokeParticle import smokeParticle

class particleEmitter(object):
    it = 0
    lifespan = 100
    def __init__(self,num,img,loc):
        self.loc = loc.get()
        self.particles = []
        self.img = img
        # self.iter = 1
        for i in range(num):
            self.particles.append(smokeParticle(self.loc, self.img,1))

    def add_particle(self,x,y):
        # print(self.it)
        randomNum = random.randint(1,20)
        if randomNum < self.it:
            for i in range(randomNum):
                self.particles.append(smokeParticle(PVector(x,y), self.img,1))
        else:
            for i in range(int(self.it)):
                self.particles.append(smokeParticle(PVector(x,y), self.img,1))
    def update(self):
       for i in reversed(range(len(self.particles))):
           p = self.particles[i]
           if (p.loc.y < self.lifespan):
               del self.particles[i]
           p.render()
           p.update()
           if p.isDead():
               del self.particles[i] 
    
            
    def getParticles(self):
        return self.particles
        
        
