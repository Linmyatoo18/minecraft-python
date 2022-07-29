from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina()
grass = load_texture('blocks/mc_grass_block.png')
opt = 1
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
                    voxel = Voxel(position= self.position + mouse.normal, texture=grass)
            if key == 'left mouse down':
               destroy(self)
            if key == 'escape':
                exit()
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


txt = Text(text="Version 1.0", color=color.black, scale=1, x=-0.86, y=0.48, highlight_color = color.white)

player = FirstPersonController()
window.color = color.rgb(200, 200, 255)
window.exit_button.visible = False
window.borderless = False

app.run()