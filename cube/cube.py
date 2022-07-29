from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

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
            color = color.rgb(255,255,255),
            scale = 0.5)




cube = Entity(model='sphere', texture='blocks/cobblestone.png', scale=1.5, y=1)
def update():
    cube.x=cube.x+time.dt *2
    cube.rotation_z=cube.rotation_z + time.dt * 120

window.color = color.rgb(190, 190, 255)
grass = Entity(model='blocks/block', texture='blocks/mc_grass_block.png', scale=1,x=1,y=-10)
#def update():

for z in range(1):
    for x in range(100):
        voxel = Voxel(position = (x,0,z))
        voxel = Voxel(position = (x,-1,z), texture='blocks/mc_stone.png')
        voxel = Voxel(position = (x,-2,z), texture='blocks/mc_stone.png')
        voxel = Voxel(position = (x,-3,z), texture='blocks/mc_stone.png')
        voxel = Voxel(position = (x,-4,z), texture='blocks/mc_stone.png')
camera.position=(7,-0.2,-20)

def input(key):
    if key == 'escape':
        exit()


app.run()