import pgzrun

WIDTH=800
HEIGHT=600

TITLE="SHOOTING GAME"

ship=Actor("galaga")
ship.x=400
ship.y=520


def update():
    if keyboard.left:
        ship.x-=5
        if ship.left<0:
            ship.left=0
    elif keyboard.right:
        ship.x+=5
        if ship.right>WIDTH:
            ship.right=WIDTH
            







def draw():
    screen.clear()
    screen.fill("blue")
    ship.draw()


















pgzrun.go()