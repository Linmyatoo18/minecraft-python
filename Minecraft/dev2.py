from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
stone = load_texture('blocks/mc_stone.png')
grass = load_texture('blocks/mc_grass_block.png')
brick = load_texture('blocks/mc_brick.png')
dirt = load_texture('blocks/mc_dirt.png')
sky = load_texture('blocks/sky.png')

opt = 1

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

class Grass(Button):
    def __init__(self, position=(0,0,0), texture=grass):
        super().__init__(
            parent = scene,
            model = 'blocks/block',
            origin_y = 0.5,
            position = position,
            texture = texture,
            scale = 0.5,
            color = color.white)

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if opt == 1:
                    voxel = Grass(position= self.position + mouse.normal, texture=grass)
                if opt == 2:
                    voxel = Grass(position= self.position + mouse.normal, texture=dirt)
                if opt == 3:
                    voxel = Grass(position= self.position + mouse.normal, texture=stone)
                if opt == 4:
                    voxel = Grass(position= self.position + mouse.normal, texture=brick)
            if key == 'left mouse down':
               destroy(self)
            if key == 'escape':
                exit() 

#I don't need this
class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'blocks/arm',
			texture = 'blocks/hand',
			scale = 0.2,
			rotation = Vec3(150,1,50), ## 1 = UP-DOWN // 2 = lEFT-right // 3 = rotate + = <==
            position = Vec2(0.4,-0.6))

	def act(self):
		self.position = Vec2(0.5,-0.8)

	def pss(self):
		self.position = Vec2(0.4,-0.6)


class hand(Entity):
	def __init__(self):
		super().__init__(
            parent = camera.ui,
            model = 'cube',
            color = color.blue,
            rotation = Vec3(35,20,30),
            scale = (0.2,0.2, 0.5),
            position = (0.7,-0.5))
def update():
    if held_keys['left mouse']:
        hand.position = (0.6, -0.6)
    elif held_keys['right mouse']:
        hand.position = (0.6, -0.6)
    else:
        hand.position= (0.7,-0.5)



for x in range(20):
    for z in range(20):
        voxel = Grass(position=(x,0,z))


ui = Entity(
    model='quad', texture='blocks/border.png', scale=0.15 , parent=camera.ui, position = (0.4,-0.43,0))


player = FirstPersonController()
camera.position = (0,0,0)
hand = hand()
window.color = color.rgb(200, 200, 255)
window.exit_button.visible = False
window.borderless = False
app.run()



































