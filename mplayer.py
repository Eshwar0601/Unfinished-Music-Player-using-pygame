import pygame ,sys , time
from pygame.locals import *
pygame.init()
pygame.mixer.init()

# variables -----------------------------------------------------------------------------

size = width , height = 800,500 
win = pygame.display.set_mode(size)
pygame.display.set_caption('M-PLAYER')
white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
lightred = [210,0,0]
font = pygame.font.SysFont(None,40)
file = 'test.wav'

# sprites -------------------------------------------------------------------------------


playimg = pygame.image.load('Play.png').convert()
playimg = pygame.transform.scale(playimg,[50,50])
frimage = pygame.image.load('fr.png').convert()
frimage = pygame.transform.scale(frimage,[50,50])
ffimage = pygame.image.load('ff.jpg').convert()
ffimage = pygame.transform.scale(ffimage,[50,50])
pauseimage = pygame.image.load('pause.jpeg').convert()
pauseimage = pygame.transform.scale(pauseimage,[50,50])
playimgRect = playimg.get_rect()



# screen message function ---------------------------------------------------------------


def message(msg,mcolor,loc):
    playerMessage = font.render(msg,True,mcolor)
    playerMessageRect = playerMessage.get_rect()
    win.blit(playerMessage,loc)
    pygame.display.update()


# main screen function ------------------------------------------------------------------


def mainScreen():
    colorin = lightred
    win.fill(white)
    message('Welcome to Mplayer',black,[width/3,height/2])
    time.sleep(3)
    win.fill(white)
    pygame.draw.rect(win, black, [15,15,width - 30, height - 30], width=3)
    win.fill(black,rect = [20,40,width/2,height/2])
    win.fill(colorin , rect = [55,350,65,40])
    message('Add',white,[60,360,40,40])
    win.fill(colorin, rect = [255,350,95,40])
    message('delete',white,[260,360,40,40])
    win.blit(playimg,(600,350))
    win.blit(frimage,(500,350))
    win.blit(ffimage,(700,350))
    pygame.display.update()


# play music function -------------------------------------------------------------------


def playMusic(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)


# main function -------------------------------------------------------------------------


def main():
    play = True
    playtime = pygame.mixer.music.get_pos()
    gameOver = False
    mainScreen()
    while not gameOver:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] >= 55 and pos[0] <= 120 and pos[1] > 350 and pos[1] < 390:
                    pass
                elif pos[0] >= 255 and pos[0] <= 350 and pos[1] > 350 and pos[1] < 390:
                    pass
                elif pos[0] >= 500 and pos[0] <= 550 and pos[1] > 350 and pos[1] < 400:
                    pass
                elif pos[0] >= 600 and pos[0] <= 650 and pos[1] > 350 and pos[1] < 400:
                    pass
                elif pos[0] >= 700 and pos[0] <= 750 and pos[1] > 350 and pos[1] < 400:
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:                    
                    if pos[0] >= 55 and pos[0] <= 120 and pos[1] > 350 and pos[1] < 390:
                        print('this is add button')
                    elif pos[0] >= 255 and pos[0] <= 350 and pos[1] > 350 and pos[1] < 390:
                        print('this is delete button')
                    elif pos[0] >= 500 and pos[0] <= 550 and pos[1] > 350 and pos[1] < 400:
                        print('this is rewind  button')
                        pygame.mixer.music.rewind()
                        pygame.display.update()
                    elif pos[0] >= 600 and pos[0] <= 650 and pos[1] > 350 and pos[1] < 400:                        
                        if play :
                            playMusic(file)
                            win.blit(pauseimage,[600,350])                        
                            pygame.display.update()
                            play = False
                        else:
                            win.blit(playimg,[600,350])
                            pygame.mixer.music.unload()
                            pygame.display.update()
                            play = True                                           
                    elif pos[0] >= 700 and pos[0] <= 750 and pos[1] > 350 and pos[1] < 400:
                        print('this is fast forword button')


    
    pygame.display.flip()


main()
sys.exit()