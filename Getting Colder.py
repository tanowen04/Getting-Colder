#Programmed by Owen Tan
import pygame
from pygame import *
import os
#from PIL import Image
import sys
import random
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(20, 20)
init()
mixer.init()
running = True
s = 'sound'
yesNo = ""
name = ""
done = 0
textFont = font.SysFont("Times New Roman",30)
black = 0
#Music and sound effects
typing = mixer.Sound('Typing.mp3')
footsteps = mixer.Sound('Footsteps.ogg')
heartbeat = mixer.Sound('Heartbeat.ogg')
music = mixer.music.load('Background music.mp3')
death = mixer.Sound('Death.mp3')
gunshot = mixer.Sound('Gunshot.wav')
mixer.music.play(-1)
heartRate = 55

# Colours
BLACK = (black,black,black)
WHITE = (255, 255, 255)

# Screen
SIZE = (1000, 700)
screen = pygame.display.set_mode(SIZE)
display.flip()

def decision(deci1, deci2, quick):
    counter = 10
    heartCount = 0
    countCounter = 0
    decision = ''
    randx = 0
    randy = 0
    nameFont = font.SysFont("Times New Roman",30)
    running = True
    # If it is not a quick-time event
    if quick == False:
        heartRate = 95
        while running:
            draw.rect(screen,(black,black,black),(0,650,274,50))
            # Makes the text vibrate
            randy = random.randrange(659,662)
            randx = random.randrange(9,12)
            string = "Make Your Decision: "    
            text = nameFont.render(string, 1, WHITE)
            screen.blit(text, Rect(randx, randy, 0, 0))
            display.flip()
            time.wait(20)
            heartCount += 1
            # Plays a heartbeat sound
            if heartCount == heartRate:
                mixer.Sound.play(heartbeat)
                heartCount = 0            
            for event in pygame.event.get():
                
                # Will exit out of the game if you click the X on the top right
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit() 
                
                # Detects if you press a key
                if event.type == pygame.KEYDOWN and event.key != 13:
                    decision += event.unicode
                    # Allows you to backspace
                    if event.key == pygame.K_BACKSPACE:
                        decision = decision[:-2]
                        draw.rect(screen,(black,black,black),(275,660,1000,50))
                    # Prints the text on the screen
                    text = nameFont.render(decision, 1, WHITE)
                    screen.blit(text, Rect(275, 660, 0, 0)) 
                    display.flip()
                if event.type == pygame.KEYDOWN and event.key == 13:
                    # Returns whether the player picked the first or second option
                    # Makes it so it's not case sensitive
                    if decision.lower() == deci1.lower():
                        return 1
                    elif decision.lower() == deci2.lower():
                        return 2
                    else:
                        # Will show an error message if the player did not type a valid input
                        decision = ''
                        draw.rect(screen,(black,black,black),(275,660,1000,50))
                        string = "Invalid Input"
                        text = nameFont.render(string, 1, WHITE)
                        screen.blit(text, Rect(275, 660, 0, 0))
                        display.flip()
                        time.wait(100)
                        draw.rect(screen,(black,black,black),(275,660,1000,50))
                        display.flip()
    # If it is a quick-time event
    else:
        heartRate = 85
        while running:
            if counter == 0:
                dead()
            draw.rect(screen,(black,black,black),(0,650,325,50))
            randy = random.randrange(659,662)
            randx = random.randrange(9,12)
            string = ("Make Your Decision (" + str(counter) + "): ")    
            text = nameFont.render(string, 1, WHITE)
            screen.blit(text, Rect(randx, randy, 0, 0))
            display.flip()
            time.wait(20)
            # Makes it count down from 10
            countCounter += 1
            if countCounter == 50:
                countCounter = 0
                counter -= 1
            heartCount += 1
            # Plays heartbeat faster than usual
            if heartCount == heartRate:
                mixer.Sound.play(heartbeat)
                heartCount = 0  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()        
                if event.type == pygame.KEYDOWN and event.key != 13:
                    decision += event.unicode
                    if event.key == pygame.K_BACKSPACE:
                        decision = decision[:-2]
                        draw.rect(screen,(black,black,black),(325,660,1000,50))
                    text = nameFont.render(decision, 1, WHITE)
                    screen.blit(text, Rect(325, 660, 0, 0)) 
                    display.flip()
                if event.type == pygame.KEYDOWN and event.key == 13:
                    if decision.lower() == deci1.lower():
                        return 1
                    elif decision.lower() == deci2.lower():
                        return 2
                    else:
                        decision = ''
                        draw.rect(screen,(black,black,black),(325,660,1000,50))
                        string = "Invalid Input"
                        text = nameFont.render(string, 1, WHITE)
                        screen.blit(text, Rect(325, 660, 0, 0))
                        display.flip()
                        time.wait(100)
                        draw.rect(screen,(black,black,black),(325,660,1000,50))
                        display.flip()            

def textBox(xyz):
    draw.rect(screen,(black,black,black),(0,0,1000,700))
    string1 = ''
    yString = 20
    running = True
    num = 0
    mixer.Sound.play(typing)
    for i in xyz:
        draw.rect(screen,(black,black,black),(10,yString,990,40))
        string1 += i
        text = textFont.render(string1, 1, WHITE)
        screen.blit(text, Rect(10,yString,0,0))
        time.wait(30)
        display.flip()
        if len(string1) >= 70 and i == " ":
            yString += 40
            string1 = ''
    mixer.Sound.stop(typing)
    
            
def dead():
    mixer.Sound.stop(footsteps)
    mixer.music.stop()
    time.wait(300)
    mixer.Sound.play(death)
    draw.rect(screen,BLACK,(0,0,1000,700))
    display.flip()
    time.wait(3000)
    nightShadowR = 7
    nightShadowG = 3
    nightShadowB = 25
    while nightShadowR != 255:
        titleFont = font.SysFont("Times New Roman",130)
        string = "You Died"    
        text = titleFont.render(string, 1, (nightShadowR, nightShadowG, nightShadowB))
        screen.blit(text, Rect(200, 100, 0, 0))
        display.flip()
        nightShadowR += 1
        nightShadowG -= 0.001
        nightShadowB -= 0.05
        time.wait(10)
    time.wait(1000)
    quit()

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
                draw.rect(screen,BLACK,(580,150,1000,50))
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
            draw.rect(screen, BLACK, (0,0,1000,700))
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
    string = "Wear Headphones for the Best Experience"
    draw.rect(screen, BLACK, (0,0,1000,700))
    text = nameFont.render(string, 1, (colour, colour, colour))
    screen.blit(text, Rect(250, 200, 0, 0)) 
    display.flip()
    time.wait(7)
    colour += 1
    
# fade out
while colour != black:
    string = "Wear Headphones for the Best Experience"
    draw.rect(screen, BLACK, (0,0,1000,700))
    text = nameFont.render(string, 1, (colour, colour, colour))
    screen.blit(text, Rect(250, 200, 0, 0)) 
    display.flip()
    time.wait(7)
    colour -= 1
    

# Game begins
running = True
while running:
    textBox("You feel cold all over. Waking up, you realize that you are in a dark forest. The fog is heavy, but you can barely make out a small river in the distance. Will you [Run to the river] or [Stay in place] for now?")
    if decision("Run to the river", "Stay in place", False) == 1:
        black += 4
        textBox("You run to the river. As you reach the bank, you realize that you aren't the only person here. Someone has left their bag here unattended. What will you do? [Search through] their bag, or [Leave it alone] and try to call for help?")
        if decision("Search through", "Leave it alone", False) == 1:
            black += 8
            mixer.Sound.play(footsteps)
            textBox("You ruffle through their belongings, trying to find something, anything that will help you survive. Inside the bag is some string, along with a lighter. Perfect! A heat source to start fires with. You suddenly hear the ruffling of trees, and stop. There's someone there. Will you [Call for help], or [Run away]?")
            if decision("Call for help", "Run away", True) == 1:
                mixer.Sound.play(gunshot)
                dead()
            else:
                mixer.Sound.stop(footsteps)
                textBox("You run away, the footsteps following after you. Terrified, you run faster until you can no longer hear them. You sigh in relief as you take the lighter and rope from your pockets. You look up and notice rain clouds gathering in the distance. You need to find a place to build a shelter now. Will you build a shelter on [High ground] or [Low ground]?")
                if decision("High ground", "Low ground", False) == 1:
                    black += 20
                    textBox("You use the rope and pieces of wood to create a shelter on high ground that will keep you safe from the rain. The rain pours down, soaking everything except for you. The next morning, you wake up, cold but dry. What will you do first? [Build a fire]? or [Find water]?")
                    if decision("Build a fire", "Find water", False) == 1:
                        black += 10
                        textBox("It's much too wet at the moment to build a fire. You try and fail to light a fire that will warm you up. Not only that, but it seems like the lighter has run out of fuel. You go back to the river, hoping to find the bag you had searched through yesterday. But unfortunately, it was gone. You now had no way of building a fire.")
                        time.wait(5000)
                        dead()
                    else:
                        black -= 10
                        textBox("You head to the river, where you know fresh water is waiting. By a stroke of luck, the bag you had searched through yesterday was still there. You search through again, and find a flint and steel that you had missed yesterday. Eager to leave before the person came back, you head back to your shelter, where you can safely live for a long time.")
                        time.wait(5000)
                        quit()
                else:
                    black += 40
                    textBox("The shelter you built on low ground quickly flooded with the intense rain. Freezing, there was nothing else for you to do.")
                    time.wait(5000)
                    dead()
                        
        else:
            black += 8
            mixer.Sound.play(footsteps)
            textBox("You leave the bag alone, and continue to walk alongside the river. Suddenly, you hear footsteps approaching and you freeze. Someone is walking towards the bag that you had just abandoned. Will you [Run away] or [Ask for help]?")
            if decision("Run away", "Ask for help", True) == 1:
                black += 4
                mixer.Sound.stop(footsteps)
                textBox("You run away, the footsteps following you. Terrified, you begin running faster until you don't hear their footsteps anymore. However, you now have no way of surviving on your own.")
                time.wait(5000)
                dead()
            else:
                mixer.Sound.play(gunshot)
                dead()
    else:
        black += 12
        mixer.Sound.play(footsteps)
        textBox("You stay where you are, not wanting to put yourself in any danger. Suddenly, you hear footsteps on your right. You stay still, listening closely to the footsteps that seemed to be walking towards the river. It could be someone dangerous, or it could be someone who could save you. What will you do? Will you [Ask for help] or [Escape quietly]?")
        if decision("Ask for help", "Escape quietly", False) == 1:
            mixer.Sound.play(gunshot)
            dead()
        else:
            black += 8
            mixer.Sound.stop(footsteps)
            textBox("You leave, making sure to keep your footsteps as quiet as possible. The person's footsteps stopped when they reached the river, and you were safe for the time being. If there are people in the forest, a city or town must be nearby. What do you think? Will you [Retrace their footsteps] or go in a [Different direction]?")
            if decision("Retrace their footsteps", "Different direction", False) == 1:
                black += 4
                textBox("You start walking towards where you had heard the footsteps coming from. After a while, you finally spot something; a small wooden house. Cautiously, you approach the house and scan the outside. Luckily, the windows showed that the lights were not on, meaning nobody was inside the house at the moment. Will you [Enter] the house? or [Wait outside] for someone to arrive?")
                if decision("Enter", "Wait outside", False) == 1:
                    black -= 20
                    textBox("You enter the house, immediately feeling warmer. A warm rug was spread across the floor, and there were long shotguns laid across the wall. You stare at the guns, thinking about taking one for yourself. Will you take it? [Yes] or [No]?")
                    if decision("Yes", "No", False) == 1:
                        mixer.Sound.play(footsteps)
                        textBox("You take a gun with you, loading it with bullets. Suddenly. footsteps start approaching the house and you freeze. The man from earlier was back, and this time with a giant animal hung around his shoulder. Quickly moving away from the window, you think about what to do. Will you get ready to [Shoot] him, or try to [Talk] with him?")
                        if decision("Shoot", "Talk", True) == 1:
                            mixer.Sound.stop(footsteps)
                            mixer.Sound.play(gunshot)
                            textBox("Congratulations " + name + ", the house belongs to you now!")
                            time.wait(5000)
                            quit()
                        else:
                            mixer.Sound.stop(footsteps)
                            mixer.Sound.play(gunshot)
                            dead()
                    else:
                        textBox("Suddenly. footsteps start approaching the house and you freeze. The man from earlier was back, and this time with a giant animal hung around his shoulder. Quickly moving away from the window, you think about what to do. Will you get ready to [Shoot] him, or try to [Talk] with him?")
                        if decision("Shoot", "Talk", True) == 1:
                            mixer.Sound.stop(footsteps)
                            textBox("You are unable to load the gun quickly enough before the man opens the door and shoots you to death.")
                            mixer.Sound.play(gunshot)
                            dead()
                else:
                    black += 30
                    textBox("You wait outside in the freezing cold. The man you had heard earlier walking towards the river came back, carrying a giant animal on their shoulder. Will you [Knock on the door] or [Leave quietly]?")
                    if decision("Knock on the door", "leave quietly", False) == 1:
                        textBox("You knock on the door, and it opens. A large man is pointing a shotgun straight at your face. Do something, quick! Will you [Talk to him] or [Punch him]?")
                        if decision("Talk to him", "Punch him", True) == 1:
                            mixer.Sound.play(gunshot)
                            dead()
                        else:
                            mixer.Sound.play(gunshot)
                            dead()
                    else:
                        black += 40
                        textBox("You are unable to walk any more due to the freezing cold.")
                        time.wait(5000)
                        dead()
            else:
                black += 4
                textBox("You run off in a different direction. However, you quickly fall and scrape your knee. Not having any first aid, the wound becomes infected.")
                time.wait(5000)
                dead()
                
                    
            