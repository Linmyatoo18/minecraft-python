from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina()
stone = load_texture('blocks/mc_stone.png')
grass = load_texture('blocks/mc_grass_block.png')
brick = load_texture('blocks/mc_brick.png')
dirt = load_texture('blocks/mc_dirt.png')
sky = load_texture('blocks/sky.png')
troll = Audio('blocks/XD.mp3', loop = False,autoplay = False)
opt = 1

name = input("\n\n\nEnter your name : ")

def update():
    global opt
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.act()
    else:
        hand.pss()
    if held_keys['1']: opt = 1
    if held_keys['2']: opt = 2
    if held_keys['3']: opt = 3
    if held_keys['4']: opt = 4

## block chose
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
                if opt == 2:
                    voxel = Voxel(position= self.position + mouse.normal, texture=dirt)
                if opt == 3:
                    voxel = Voxel(position= self.position + mouse.normal, texture=stone)
                if opt == 4:
                    voxel = Voxel(position= self.position + mouse.normal, texture=brick)
            if key == 'left mouse down':
               destroy(self)
            if key == 'escape':
                troll.play()

## ground
for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,0,z))
        voxel = Voxel(position = (x,-1,z), texture = dirt)
        voxel = Voxel(position = (x,-2,z), texture = dirt)
        voxel = Voxel(position = (x,-3,z), texture = stone)
player = FirstPersonController()


#Sky
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = sky,
            scale = 150,
            double_sided = True
    )

class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'blocks/arm',
			texture = 'blocks/hand',
			scale = 0.2,
			rotation = Vec3(150,-10,0),
			position = Vec2(0.7,-0.6))

	def act(self):
		self.position = Vec2(0.3,-0.5)

	def pss(self):
		self.position = Vec2(0.7,-0.6)

hand = Hand()

sky = Sky()

ui = Entity(
    parent = camera.ui,model = 'blocks/block', scale = 0.05, texture = grass, position = (-0.255,-0.417))
ui = Entity(
    parent = camera.ui,model = 'blocks/block', scale = 0.05, texture = dirt, position = (-0.086,-0.417))
ui = Entity(
    parent = camera.ui,model = 'blocks/block', scale = 0.05, texture = stone, position = (0.086,-0.417))
ui = Entity(
    parent = camera.ui,model = 'blocks/block', scale = 0.05, texture = brick, position = (0.255,-0.417))
frame = Entity(
    parent = camera.ui, model='cube', texture = 'blocks/frame.png', scale =(0.68,0.17) , position = (0,-0.415))


ui = Entity(parent = camera.ui,model = 'quad', scale = 0.17, texture = 'blocks/border.png', position = (-0.2547, -0.4149))
ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/grass_frame.png')
ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/grass_frame.png')



bk = 1

def input(bk):
    if held_keys['1']: bk = 1
    if held_keys['2']: bk = 2
    if held_keys['3']: bk = 3
    if held_keys['4']: bk = 4

    if bk == 2:
        ui = Entity(parent = camera.ui,model = 'quad', scale = 0.17, texture = 'blocks/border.png', position = (-0.084, -0.4149))
        ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/dirt_frame.png')
        ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/dirt_frame.png')
    if bk == 3:
        ui = Entity(parent = camera.ui,model = 'quad', scale = 0.17, texture = 'blocks/border.png', position = (0.084, -0.4149))
        ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/stone_frame.png')    
        ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/stone_frame.png')   
    if bk == 4:
        ui = Entity(parent = camera.ui,model = 'quad', scale = 0.17, texture = 'blocks/border.png', position = (0.254, -0.4149))
        ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/brick_frame.png')
        ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/brick_frame.png')
    if bk == 1:
        ui = Entity(parent = camera.ui,model = 'quad', scale = 0.17, texture = 'blocks/border.png', position = (-0.2547, -0.4149))
        ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/grass_frame.png')
        ui1 = Entity(parent = camera.ui, model = 'quad', scale =(0.68,0.17) , position = (0,-0.415), texture = 'blocks/grass_frame.png')


txt = Text(text="Last Version", color=color.black, scale=1, x=-0.86, y=0.48, highlight_color = color.white)
window.exit_button.visible = False
window.borderless = False
txt = Text(text="Player - "+ name , color=color.white, scale=1, x=0.5, y=-0.4)
app.run()
