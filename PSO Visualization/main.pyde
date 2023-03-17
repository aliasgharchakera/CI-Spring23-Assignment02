# from gui import GUI
from screen import Screen
from cloud import Cloud
from car import Car
from gui import GUI
from particleEmitter import particleEmitter
from add_car import addCar
# from add_cloud import addCloud
from cloud import Cloud
hud = None

def setup():
    global hud, ps, car, ac
    size(1280,800)
    hud = GUI()
    img = loadImage("images/texture_3.png")
    initial = 0
    car = addCar(1,PVector(100,650))
    ps = particleEmitter(initial, img, PVector(0, 650))
    ac = Cloud()
    # ac = addCloud()
    
def draw():
    screen = Screen()
    screen.draw()
    # cloud = Cloud()
    # cloud.draw()
    hud.draw()
    ac.draw()
    # ac.update_cloud()
    # ac.display_cloud()
    ps.update()
    car.update()
    
    for i in range(len(car.cars)):
        cx = car.cars[i].update()
        ps.add_particle(cx-100,680)
    ac.update(len(ps.particles))
    # if (len(ps.particles) > 200):
    #     Cloud.showTint = True
    #     Cloud.r = 0
    #     Cloud.g = 0
    #     Cloud.b = 0
    # if (len(ps.particles) > 60):
    #     Cloud.showTint = True
    #     Cloud.r = 170
    #     Cloud.g = 160
    #     Cloud.b = 170
    # if (len(ps.particles) < 10):
    #     Cloud.showTint = False
    id = hud.mousepressed()

def mouseClicked():
    button = hud.mouseHover()
    if (button):
        if button == 1:
            car.add_car()
        if button == 2:
            car.remove_car()
            
