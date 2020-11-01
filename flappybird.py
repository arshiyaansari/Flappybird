import pygame
import gamebox
import random
camera = gamebox.Camera(800, 600)
ground = gamebox.from_color(-100, 600, "black", 1000000000, 100)
sky = gamebox.from_color(-100,0, "white", 1000000000, 100)
bird = gamebox.from_color(50, 200, "red", 15, 40)
bounds_action = "stop"
pillars = []
for x in range(300, 10000, 300):
    pillars.append(gamebox.from_color(x, 0, "green", 50, random.randint(100, 350)))
    pillars.append(gamebox.from_color(x, 500, "green", 50, random.randint(200, 450)))
counter = 0
score = 0
game_over = False
bird.yspeed = 0
def tick(keys):
    global counter
    global game_over
    global score
    if game_over is False:
        if pygame.K_RIGHT in keys:
            bird.x += 20
        if pygame.K_SPACE in keys:
            bird.y -= 20
        bird.y += 5
        bird.x += 3
        camera.clear("cyan")
        camera.draw(bird)
        camera.x = bird.x+150
        counter += 1
        camera.draw(ground)
        for pillar in pillars:
            if bird.touches(pillar):
                game_over = True
            camera.draw(pillar)
            if bird.touches(ground):
                game_over = True
            if bird.touches(sky):
                game_over = True
        score_box = gamebox.from_text(bird.x-170, 30, "Score: " + str(score), "arial", 24, "white", True)
        score += 1
        camera.draw(score_box)
        camera.display()
    else:
        camera.clear("black")
        game_over_text = gamebox.from_text(bird.x+125, 300, "GAME OVER", "arial", 65, "red", True)
        camera.draw(game_over_text)
        final_score = gamebox.from_text(bird.x+125, 500, "SCORE: " + str(score), "arial", 36, "red", True)
        camera.draw(final_score)
        camera.display()
ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)