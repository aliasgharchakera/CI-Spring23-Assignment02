
class Screen(object):
    
    def __init__(self):
        self.img = loadImage('images/road.png')
        
    def draw(self):
        background(self.img)
        
