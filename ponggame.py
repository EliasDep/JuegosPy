import pygame

pygame.init ()

black = (0, 0, 0)
white = (255, 255, 255)

screenSize = (800, 600)
playerWidth = 15
playerHeight = 90

screen = pygame.display.set_mode (screenSize)
clock = pygame.time.Clock ()

pygame.display.set_caption ('Pong Game')


#jugador A
playerA_coorX = 50
playerA_coorY = 300 - 45
playerA_speedY = 0


#jugador B
playerB_coorX = 750 - playerWidth
playerB_coorY = 300 - 45
playerB_speedY = 0


#pelota
pelotaX = 400
pelotaY = 300
pelota_speedX = 3
pelota_speedY = 3


gameover = False


while not gameover:

    for event in pygame.event.get ():

        if event.type == pygame.QUIT:
            gameover = True
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_w:
                playerA_speedY = -3
            if event.key == pygame.K_s:
                playerA_speedY = 3
            
            if event.key == pygame.K_UP:
                playerB_speedY = -3
            if event.key == pygame.K_DOWN:
                playerB_speedY = 3


        if event.type == pygame.KEYUP:

            if event.key == pygame.K_w:
                playerA_speedY = 0
            if event.key == pygame.K_s:
                playerA_speedY = 0
            
            if event.key == pygame.K_UP:
                playerB_speedY = 0
            if event.key == pygame.K_DOWN:
                playerB_speedY = 0


    if pelotaY > 590 or pelotaY < 10:
        pelota_speedY *= -1


    #revisa si sale de lado derecho
    if pelotaX > 800:
        pelotaX = 400
        pelotaY = 300

        pelota_speedX *= -1 
        pelota_speedY *= -1 


    #revisa si sale de lado izquierdo
    if pelotaX < 0:
        pelotaX = 400
        pelotaY = 300

        pelota_speedX *= -1 
        pelota_speedY *= -1


    #coordenadas para dar movimiento
    playerA_coorY += playerA_speedY
    playerB_coorY += playerB_speedY

    pelotaX += pelota_speedX
    pelotaY += pelota_speedY

    screen.fill (black)


    #dibujo
    playerA = pygame.draw.rect (screen, white, (playerA_coorX, playerA_coorY, playerWidth, playerHeight))
    playerB = pygame.draw.rect (screen, white, (playerB_coorX, playerB_coorY, playerWidth, playerHeight))
    pelota = pygame.draw.circle (screen, white, (pelotaX, pelotaY), 10)


    #colisiones
    if pelota.colliderect (playerA) or pelota.colliderect (playerB):
        pelota_speedX *= -1


    pygame.display.flip ()
    clock.tick (60)

pygame.quit ()