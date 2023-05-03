import pygame, sys, time, random

speed = 15

#tamaño ventana
frameSizeX = 720
frameSizeY = 480

checkErrors = pygame.init ()

if (checkErrors[1] > 0):
    print ('Error ' + checkErrors[1] )
else:
    print ('Juego iniciado correctamente')


#inicio ventana de juego
pygame.display.set_caption ('Snake Game')
gameWindow = pygame.display.set_mode ((frameSizeX, frameSizeY))


#colores
black = pygame.Color (0,0,0)
white = pygame.Color (255,255,255)
red = pygame.Color (255,0,0)
green = pygame.Color (0,255,0)
blue = pygame.Color (0,0,255)


fpsController = pygame.time.Clock ()


#tamaño de una serpiente
squareSize = 20


def initVars ():
    global headPos, snakeBody, foodPos, foodSpawn, score, direction

    direction = 'RIGHT'
    headPos = [120,60]
    snakeBody = [[120,60]]
    foodPos = [random.randrange (1,(frameSizeX // squareSize)) * squareSize, random.randrange (1,(frameSizeY // squareSize)) * squareSize]
    foodSpawn = True
    score = 0

initVars ()


def showScore (choice, color, font, size):
    scoreFont = pygame.font.SysFont (font, size)
    scoreSurface = scoreFont.render ('Score: ' + str(score), True, color)
    scoreRect = scoreSurface.get_rect ()

    if choice == 1:
        scoreRect.midtop = (frameSizeX / 10, 15)
    else:
        scoreRect.midtop = (frameSizeX / 2, frameSizeY / 1.25)

    gameWindow.blit (scoreSurface, scoreRect)


#loop juego
while True:
    
    for event in pygame.event.get ():
        
        if event.type == pygame.QUIT:
            pygame.quit ()
            sys.exit ()
        elif event.type == pygame.KEYDOWN:
            
            if (event.key == pygame.K_UP or event.key == ord('w') and direction != 'DOWN'):
                direction = 'UP'
            elif (event.key == pygame.K_DOWN or event.key == ord('s') and direction != 'UP'):
                direction = 'DOWN'
            elif (event.key == pygame.K_LEFT or event.key == ord('a') and direction != 'RIGHT'):
                direction = 'LEFT'
            elif (event.key == pygame.K_RIGHT or event.key == ord('d') and direction != 'LEFT'):
                direction = 'RIGHT'


    if direction == "UP":
        headPos [1] -= squareSize
    elif direction =='DOWN':
        headPos [1] += squareSize
    elif direction =='LEFT':
        headPos [0] -= squareSize
    else:
        headPos [0] += squareSize
    

    if headPos [0] < 0:
        headPos [0] = frameSizeX - squareSize
    elif headPos [0] > frameSizeX - squareSize:
        headPos [0] = 0
    elif headPos [1] < 0:
        headPos [1] = frameSizeY - squareSize
    elif headPos [1] > frameSizeY - squareSize:
        headPos [1] = 0
    

    #comer manzana
    snakeBody.insert (0, list(headPos))

    if (headPos [0] == foodPos [0] and headPos [1] == foodPos [1]):
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop ()


    #sapwn comida
    if not foodSpawn:
        foodPos = [random.randrange (1,(frameSizeX // squareSize)) * squareSize, random.randrange (1,(frameSizeY // squareSize)) * squareSize]
        foodSpawn = True

    #gfx
    gameWindow.fill (black)

    for pos in snakeBody:
        pygame.draw.rect (gameWindow, green, pygame.Rect (pos[0] + 2, pos[1] + 2, squareSize - 2, squareSize - 2))

    pygame.draw.rect (gameWindow, red, pygame.Rect (foodPos [0],foodPos [1], squareSize, squareSize))


    #condiciones game over
    for block in snakeBody [1:]:

        if (headPos [0] == block [0] and headPos [1] == block [1]):
            initVars ()

    showScore (1, white, 'consolas', 20)
    pygame.display.update ()
    fpsController.tick (speed)