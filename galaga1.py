import pgzrun

WIDTH=800
HEIGHT=600

TITLE="SHOOTING GAME"

ship=Actor("galaga")
ship.x=400
ship.y=520

bullets=[]
enemies=[]
enemies.append(Actor("bug"))




def update():
    if keyboard.left:
        ship.x-=5
    if ship.left<0:
            ship.left=0
    elif keyboard.right:
        ship.x+=5
    if ship.right>WIDTH:
            ship.right=WIDTH
    for bullet in bullets:
        if bullet.y<=0:
             bullets.remove(bullet)
        bullet.y-=10
    for enemy in enemies:
         enemy.y-=12
         if enemy.y>HEIGHT:
              enemies.remove(enemy)
         for bullet in bullets:
           if enemy.colliderect(bullet):
                score+100
                bullets.remove (bullet)

            




def on_key_down(key):
    if key==keys.SPACE:
          bullets.append(Actor('bullet'))
          bullets[-1].x=ship.x
          bullets[-1].y=ship.y-80







def draw():
    screen.clear()
    screen.fill("blue")
    for bullet in bullets:
         bullet.draw()
    for enemy in enemies:
         enemy.draw()

    ship.draw()


















pgzrun.go()