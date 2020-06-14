import pygame
import time
import random

#supposedly initializing pygame 
pygame.init()

#setting colour variables with rgb values
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (50, 153, 213)
green = (0, 255, 0)

#creating dimesions of screen
screen_width = 800
screen_height = 600
 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ryan\'s snake game')

clock = pygame.time.Clock()

#snake variables
snake_block = 10
snake_speed = 30
 
font_style = pygame.font.SysFont(None, 30)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

#function which helps display messages over the screen using blit function 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width/3, screen_height/3])

#gameloop function which actually runs the game
def gameLoop():  
    #initializing game variables
    game_over = False
    game_close = False
 
    x1 = screen_width / 2
    y1 = screen_height / 2
 
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    #using random to determine position of fruit 
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0

    #actual game
    while not game_over:

        #secondary loop which updates end of game screen
        while game_close == True:
            #background colour filling
            screen.fill(white)

            #allows user to retry without having to restart the application
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            
            #another queue which simply checks which keys are pressed (q or c)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        
        #queue which checks for key presses
        for event in pygame.event.get():
            #if the x button is closed on the top of the screen
            if event.type == pygame.QUIT:
                game_over = True

            #detecting any key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #detecs if user has gone out of bounds (collision with a wall technically)
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        #movement of snake by changing its position on the screen
        x1 += x1_change
        y1 += y1_change

        
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
 
        pygame.display.update()

        #if food is eaten summon another food in a random location
        if x1 == foodx and y1 == foody:
            #random coordinates within the screen
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()

#calls game function to run the game.
gameLoop()