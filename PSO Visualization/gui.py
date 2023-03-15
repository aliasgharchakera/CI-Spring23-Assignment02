from button import Button
from slider import Slider


class GUI:  # resolution is hard-coded for now, can be generalized by adding association to Map
    def __init__(self):
        self.buttons = []
        self.sliders = []
        self.bg = [1080, 0, 200, 720]  # x,y,w,h
        # Pressable Buttons
        # self.buttons.append(Button('Add Double Slit', self.bg))
        # self.buttons.append(Button('Add Obstacle', self.bg))
        # self.buttons.append(Button('Add Colony', self.bg))
        # self.buttons.append(Button('Add Food', self.bg))
        # self.buttons.append(Button('Add Grass', self.bg))
        # # #Toggle Buttons
        self.buttons.append(Button('Add Car', self.bg))
        self.buttons[0].pressed = True  # press remove by default
        self.buttons.append(Button('Toggle Screen', self.bg))
        self.buttons[0].pressed = True
        # Sliders
        self.sliders.append(Slider('Red Intensity', 0, 255, 0, self.bg))
        self.sliders.append(Slider('Green Intensity', 0, 255, 0, self.bg))
        self.sliders.append(Slider('Blue Intensity', 0, 255, 0, self.bg))
        self.sliders.append(Slider('Lifespan', 0, 1000, 100, self.bg))
        self.tit = '    Particle Simulation\n'
        self.crs = '    Computational Intelligence\n'
        self.auth_1 = '    Muhammad - 06369\n'
        self.auth_2 = '    Ali Asghar Yousuf - ay06993'
        self.crdt = self.crs+self.tit+self.auth_1+self.auth_2

    def draw(self):
        text
        noStroke()
        rectMode(CORNER)
        fill(204, 102, 0)
        rect(*self.bg)
        self.drawElements()
        textSize(11)
        fill(255)
        text(self.crdt, self.bg[0], self.bg[1] +
             (Slider.sliderCount+1)*Button.buttonSpacing, 160, 120)

    def drawElements(self):
        for i in self.buttons:
            i.draw()
        for i in self.sliders:
            i.draw()

    def mouseHover(self):
        for i in self.buttons:
            if (i.mouseHover()):
                return i.id
        return None

    def toggleButton(self, id):
        self.buttons[id].pressed = not self.buttons[id].pressed
