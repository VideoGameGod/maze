from pygame import *
window = display.set_mode((700, 500))
display.set_caption("aMAZEing game")
background = transform.scale(image.load("background.jpg"), (700, 500))
mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
kick = mixer.Sound("kick.ogg")
money = mixer.Sound("money.ogg")
font.init()
font = font.Font(None, 70)
win = font.render("You win!", True, (0, 255, 0))
lose = font.render("You lose!", True, (255, 0, 0))
game = 1
finish = 0
clock = time.Clock()
fps = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
class Enemy(GameSprite):
    def update(self):
        if self.speed > 0 and self.rect.x > 640:
            self.speed = -1 * self.speed
        if self.speed < 0 and self.rect.x < 500:
            self.speed = -1 * self.speed
        self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, colour_1, colour_2, colour_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.colour_1 = colour_1
        self.colour_2 = colour_2
        self.colour_3 = colour_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((colour_1, colour_2, colour_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
hero = Player("hero.png", 0, 400, 5)
cyborg = Enemy("cyborg.png", 500, 300, 2)
treasure = GameSprite("treasure.png", 600, 400, 0)
w1 = Wall(150, 80, 30, 100, 100, 10, 400)
w2 = Wall(150, 80, 30, 200, 0, 10, 400)
w3 = Wall(150, 80, 30, 300, 100, 10, 400)
w4 = Wall(150, 80, 30, 400, 0, 10, 400)
w5 = Wall(150, 80, 30, 500, 100, 10, 400)
def main():
    pass
while game:
    for events in event.get():
        if events.type == QUIT:
            game = 0
    if not finish:
        window.blit(background, (0, 0))
        keys_pressed = key.get_pressed()
        hero.reset()
        cyborg.reset()
        treasure.reset()
        hero.update()
        cyborg.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        if sprite.collide_rect(hero, treasure):
            finish = 1
            money.play()
            window.blit(win, (250, 250))
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5):
            finish = 1
            kick.play()
            window.blit(lose, (250, 250))
        display.update()
        clock.tick(fps)