import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# Player
bin_player = Actor("bin")
bin_player.center = (WIDTH // 2, HEIGHT - 50)

# Lists
recyclables = []
trash_items = []

score = 0
game_over = False

# Spawn timer
spawn_timer = 0


def draw():
    screen.clear()

    if game_over:
        screen.fill("red")
        screen.draw.text("GAME OVER",center=(WIDTH // 2, HEIGHT // 2 - 30),fontsize=60,color="white")

        screen.draw.text(f"Final Score: {score}",center=(WIDTH // 2, HEIGHT // 2 + 30),fontsize=40,color="yellow")
        return

    screen.fill((100, 200, 255))

    bin_player.draw()

    for item in recyclables:
        item.draw()

    for item in trash_items:
        item.draw()

    screen.draw.text(f"Score: {score}",topleft=(10, 10),fontsize=40,color="black")


def update():
    global spawn_timer
    global score
    global game_over

    if game_over:
        return

    # Bin movement
    if keyboard.left:
        bin_player.x -= 6

    if keyboard.right:
        bin_player.x += 6

    bin_player.x = max(40, min(WIDTH - 40, bin_player.x))

    # Spawn objects
    spawn_timer += 1

    if spawn_timer > 40:
        spawn_timer = 0

        if random.randint(1, 4) == 1:
            item = Actor("trash")
            item.x = random.randint(30, WIDTH - 30)
            item.y = -20
            trash_items.append(item)
        else:
            item = Actor("recycle")
            item.x = random.randint(30, WIDTH - 30)
            item.y = -20
            recyclables.append(item)

    # Move recyclables
    for item in recyclables[:]:
        item.y += 4

        if bin_player.colliderect(item):
            recyclables.remove(item)
            score += 1

        elif item.y > HEIGHT:
            recyclables.remove(item)

    # Move trash
    for item in trash_items[:]:
        item.y += 4

        if bin_player.colliderect(item):
            game_over = True

        elif item.y > HEIGHT:
            trash_items.remove(item)


pgzrun.go()