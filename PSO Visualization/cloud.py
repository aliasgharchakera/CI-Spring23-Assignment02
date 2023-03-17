

class Cloud(object):

    def __init__(self):
        self.img = loadImage('images/cloud_bg.png')
        self.img.resize(1080,100)
        self.cx = 540
        self.cy = 55

    def draw(self):
        self.render()
        
    def render(self):
        imageMode(CENTER)
        image(self.img, self.cx,self.cy)
        
    def update(self, value):
        if value > 120:
            tint(190,190,190)
        elif value > 80:
            tint(230,230,230)
        elif value < 50:
            tint(255,255,255)
