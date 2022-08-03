#Programmed by Owen Tan
import pygame
from pygame import *
import os
#from PIL import Image
import sys
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
init()
running = True
yesNo = ""
name = ""
done = 0

# Colours
RED = (255, 0, 0)
DARKRED = (180, 0, 0)
DARKERRED = (50, 0, 0)
YELLOW = (255, 255, 0)
DARKYELLOW = (200, 200, 0)
DARKERYELLOW = (175, 175, 0)
ORANGE = (255, 128, 0)
PURPLE = (100, 0, 200)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
DARKBLUE = (0,0,130)
GREEN = (0, 255, 0)
DARKGREEN = (5,40,10)
WHITE = (255, 255, 255)
LIGHTGREY = (227, 227, 227)
LIGHTYGREY = (200, 200, 200)
GREY = (138, 138, 138)
DARKGREY = (70, 70, 70)
LIGHTBROWN = (174, 26, 26)
BROWN = (87, 13, 13)
DARKBROWN = (42, 6, 6)
NIGHT = (14, 0, 50)
NIGHTSHADOW = (7, 3, 25)
# Screen
SIZE = (1000, 700)
screen = pygame.display.set_mode(SIZE)
display.flip()

def textBox(sentence, name1):
    string1 = ''
    string2 = ''
    num = 0
    for i in sentence:
        draw.rect(screen,GREY,(20,500,960,180))
        draw.rect(screen,LIGHTGREY,(30,510,940,160))
        draw.rect(screen,GREY,(40,480,200,50))
        draw.rect(screen,LIGHTGREY,(45,485,190,40))
        text = textFont.render(name1, 1, BLACK)
        screen.blit(text, Rect(55, 490, 0, 0))
        findSpace = sentence[60:].find(" ") 
        if num > 60 and len(string1) == findSpace + 60:
            string2 += i
            text = textFont.render(string1, 1, BLACK)
            screen.blit(text, Rect(80, 550, 0, 0))            
            text = textFont.render(string2, 1, BLACK)
            screen.blit(text, Rect(75, 590, 0, 0))
            time.wait(30)
            display.flip()
        else:
            string1 += i
            text = textFont.render(string1, 1, BLACK)
            screen.blit(text, Rect(80, 550, 0, 0))
            time.wait(30)
            display.flip()
        num += 1

# Title screen text
nightShadowR = 7
nightShadowG = 3
nightShadowB = 25
while nightShadowR != 255:
    titleFont = font.SysFont("Times New Roman",130)
    string = "Getting Colder"    
    text = titleFont.render(string, 1, (nightShadowR, nightShadowG, nightShadowB))
    screen.blit(text, Rect(100, 100, 0, 0))
    display.flip()
    nightShadowR += 1
    nightShadowG -= 0.001
    nightShadowB -= 0.05
    time.wait(10)
nightShadowR = 7
nightShadowG = 3
nightShadowB = 25
while nightShadowB != 227:
    draw.rect(screen, (nightShadowR, nightShadowG, nightShadowB), (200, 350, 600, 250))
    nightShadowR += 1
    nightShadowG += 1
    nightShadowB += 1
    display.flip()
newGameFont = font.SysFont("Times New Roman",90)
string = "New Game"    
text = newGameFont.render(string, 1, BLACK)
screen.blit(text, Rect(290, 420, 0, 0))
display.flip()
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()        
        if event.type == MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            if x > 200 and x < 800 and y > 350 and y < 600:
                draw.rect(screen, BLACK, (0,0,1000,700))
                display.flip()
                nameFont = font.SysFont("Times New Roman",30)
                done += 1
                string = "Enter Your Name: "    
                text = nameFont.render(string, 1, WHITE)
                screen.blit(text, Rect(350, 150, 0, 0)) 
                display.flip()
        if event.type == pygame.KEYDOWN and done != 0 and event.key != 13:
            name += event.unicode
            if event.key == pygame.K_BACKSPACE:
                name = name[:-2]
                draw.rect(screen,NIGHTSHADOW,(580,150,1000,50))
            text = nameFont.render(name, 1, WHITE)
            screen.blit(text, Rect(580, 150, 0, 0)) 
            display.flip()
        if event.type == pygame.KEYDOWN and event.key == 13:
            string = "Are you sure your name is %s?" %name
            text = nameFont.render(string, 1, WHITE)
            screen.blit(text, Rect(280, 200, 0, 0))
            string = "YES     NO"
            text = nameFont.render(string, 1, WHITE)
            screen.blit(text, Rect(410, 250, 0, 0))             
            display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            if x < 470 and x > 410 and y < 280 and y > 250:
                yesNo = "yes"
            elif x < 550 and x > 500 and y < 280 and y > 250:
                yesNo = "no"
        if yesNo == "yes":
            draw.rect(screen,BLACK,(0,0,1000,700))
            display.flip()
            running = False
        elif yesNo == "no":
            name = ""
            draw.rect(screen, NIGHTSHADOW, (0,0,1000,700))
            draw.rect(screen,DARKBROWN,(0,380,1000,320))
            draw.circle(screen,GREEN,(90,540),60)
            draw.circle(screen,GREEN,(150,540),40)
            nuclearWaste(800,400,70,120)
            nuclearWaste(840,420,65,110)
            nuclearWaste(100,410,70,120)
            nameFont = font.SysFont("Times New Roman",30)
            string = "Enter Your Name: "
            text = nameFont.render(string, 1, WHITE)
            screen.blit(text, Rect(350, 150, 0, 0)) 
            display.flip()
            yesNo = ""
time.wait(2000)
white = 255
black = 0
colour = 0

# fade in
while colour != white:
    string = "so.. cold.."
    draw.rect(screen, BLACK, (0,0,1000,700))
    text = nameFont.render(string, 1, (colour, colour, colour))
    screen.blit(text, Rect(350, 150, 0, 0)) 
    display.flip()
    time.wait(7)
    colour += 1
    
# fade out
while colour != black:
    string = "so.. cold.."
    draw.rect(screen, BLACK, (0,0,1000,700))
    text = nameFont.render(string, 1, (colour, colour, colour))
    screen.blit(text, Rect(350, 150, 0, 0)) 
    display.flip()
    time.wait(7)
    colour -= 1

