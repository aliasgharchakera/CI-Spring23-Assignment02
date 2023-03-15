# from gui import GUI
from screen import Screen
from cloud import Cloud
from car import Car
from gui import GUI
from particleEmitter import particleEmitter

hud = None
def setup():
    global hud, ps, car
    size(1280,800)
    hud = GUI()
    img = loadImage("images/texture_3.png")
    initial = 10
    car = Car(PVector(100,650))
    ps = particleEmitter(initial, img, PVector(0, 650))
    
def draw():
    screen = Screen()
    screen.draw()
    cloud = Cloud()
    cloud.draw()
    car.draw()
    hud.draw()
    ps.update()
    cx = car.update()
    ps.add_particle(cx-100,680)
    cloud.update(len(ps.particles))
    # if (len(ps.particles) > 50):
    #     cloud.update(k)
    # if (len(ps.particles) > 150):
    #     cloud.update(True)
        
        
    # print(mouseX, mouseY)
    # ps.add_particle(400,680)
        # background(0)
    # image(bg,80,100)
    # screen = Screen()
    # screen.draw()
