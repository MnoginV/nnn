from pygame import *

wndw = display.set_mode((600,500))
wndw.fill((155, 76,47))
game = True
clock = time.Clock()
finish = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,size):
        super().__init__()
        self.image = transform.scale(image.load(player_image), size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        wndw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    
    def update_l(self):
        keys = key.get_pressed()
        
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        
        if keys[K_s] and self.rect.y<550-80:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        
        if keys[K_DOWN] and self.rect.y<550-80:
            self.rect.y += self.speed
    
ball = GameSprite('mathik.png',200,250,4,(50,50))
player1 = Player('paketka.png',5,100,5,(50,150))
player2 = Player('paketka.png',550,100,5,(50,150))   
font.init()
speed_y = 3
speed_x = 3
font1 = font.Font(None, 35)
lose1 = font1.render('player1 проиграл!', True, (180, 0, 0))
lose2 = font1.render('player2 проиграл!', True, (180, 0, 0))


while game != False:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        wndw.fill((155, 76,47))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
        ball.reset()
    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        wndw.blit(lose1, (200,200))
    if ball.rect.x > 550:
        finish = True
        wndw.blit(lose2, (200,200))
    display.update()
    clock.tick(60)
