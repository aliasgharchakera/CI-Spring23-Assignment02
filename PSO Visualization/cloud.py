

class Cloud(object):
    
    def __init__(self):
        self.r, self.g, self.b = 173,216,230
        self.square = createShape(RECT,0,0,1080,100)
        self.square.setFill(color(self.r, self.g, self.b))
        self.square.setStroke(False)
        
    def draw(self):
        self.render()
        
    def render(self):
        shape(self.square, 0,0)    
        
    def update(self, value):
        self.square = createShape(RECT,0,0,1080,100)
        self.square.setStroke(False)
        if value < 50:
            self.square.setFill(color(173,216,230))
        if value > 50 and value < 150:
            self.square.setFill(color(165,173,167))
        elif value > 150:
            self.square.setFill(color(139,143,140))
        # elif value > 300:
        #     self.square.setFill(color(35, 36, 35))
        # if (extreme == False):
            # square1 = createShape(RECT,0,0,1080,100)
            # square1.setFill(color(165,173,167))
        # shape(self.square,0,0)
        self.render()
        # elif extreme == True:
        #     square2 = createShape(RECT,0,0,1080,100)
        #     square2.setFill(color(139, 143, 140))
        #     square2.setStroke(False)
        #     shape(square2,0,0)
        

        
