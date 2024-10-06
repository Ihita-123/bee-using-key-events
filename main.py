import pgzrun
import random 

WIDTH = 600
HEIGHT= 600
msg= "Welcome to this game"
score=0

bee=Actor("bee")
flower=Actor("flower")
bee.x= 200
bee.y=400 
flower.pos=500,300
def draw():
    screen.blit("bg",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(msg,(300,300),color="black")
    screen.draw.text(f"Your final score is: {score}", (400, 200),color="black")

def update():
    global msg,score
    if keyboard.up:
        bee.y-=2
    if keyboard.down:
        bee.y+=2
    if keyboard.left:
        bee.x-=2
    if keyboard.right:
        bee.x+=2
    if bee.colliderect(flower):
        flower.x=random.randint(50,WIDTH-100)
        flower.y=random.randint(50,HEIGHT-100)
        msg= "great job!"
        score+=1
        print(score)
       







pgzrun.go()
