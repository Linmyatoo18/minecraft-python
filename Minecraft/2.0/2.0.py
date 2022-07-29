from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina()
stone = load_texture('blocks/mc_stone.png')
grass = load_texture('blocks/mc_grass_block.png')
brick = load_texture('blocks/mc_brick.png')
dirt = load_texture('blocks/mc_dirt.png')
sky = load_texture('blocks/sky.png')
opt = 1

def update():
    global opt
    if held_keys['1']: opt = 1
    if held_keys['2']: opt = 2
    if held_keys['3']: opt = 3
    if held_keys['4']: opt = 4




class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass):
        super().__init__( 
            parent = scene,
            position = position,
            model = 'blocks/block',
            origin_y = 0.5,
            texture = texture, 
            color = color.color(0,0,random.uniform(0.9, 1)),
            scale = 0.5)

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if opt == 1:
                    gss = Voxel(position= self.position + mouse.normal, texture=grass)
                if opt == 2:
                    gss = Voxel(position= self.position + mouse.normal, texture=dirt)
                if opt == 3:
                    gss = Voxel(position= self.position + mouse.normal, texture=stone)
                if opt == 4:
                    gss = Voxel(position= self.position + mouse.normal, texture=brick)
            if key == 'left mouse down':
               destroy(self)
            if key == 'escape':
                exit()

txt = Text(text="Version 2.0", color=color.black, scale=1, x=-0.86, y=0.48, highlight_color = color.white)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = color.rgb(200, 200, 255),
            scale = 150,
            double_sided = True)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))
        voxel = Voxel(position = (x,-1,z), texture = dirt)
        voxel = Voxel(position = (x,-2,z), texture = dirt)
        voxel = Voxel(position = (x,-3,z), texture = stone)

arm = Entity(
    parent = camera.ui,
    model = 'cube',
    color = color.blue,
    rotation = Vec3(35,20,30),
    scale = (0.2,0.2, 0.5),
    position = (0.7,-0.5))
def update():
    if held_keys['left mouse']:
        arm.position = (0.6, -0.6)
    elif held_keys['right mouse']:
        arm.position = (0.6, -0.6)
    else:
        arm.position= (0.7,-0.5)



player = FirstPersonController()
window.color = color.rgb(200, 200, 255)
window.exit_button.visible = False
window.borderless = False

app.run()