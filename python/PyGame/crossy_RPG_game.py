# Referencias: Zenva - Learn python from making a game

import pygame # Library import


screen_title = "Crossy RPG"
screen_width = 800
screen_height = 800
white_color = (255, 255, 255) # RGB Colors
black_color = (0, 0, 0)


clock = pygame.time.Clock() # Clock used to update game events and frames
pygame.font.init()
font = pygame.font.SysFont("comicsans", 75)

class Game:

    #Typical rate of 60, equivalent to FPS
    tick_rate = 60

    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.heigth = height
        self.game_screen = pygame.display.set_mode((width, height)) # Create the window
        self.game_screen.fill(white_color) # Set the game window color
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image,(width,height))

    def run_game_loop(self, level_speed):
        is_game_over = False
        did_win = False
        direction = 0



        player_character =  PlayerCharacter("files/player.png", 375, 700, 50, 50)

        enemy_0 = NonPlayerCharacter("files/enemy.png", 20, 600, 50, 50)
        enemy_0.speed *= level_speed

        enemy_1 = NonPlayerCharacter("files/enemy.png", self.width-40, 400, 50, 50)
        enemy_1.speed *= level_speed

        enemy_2 = NonPlayerCharacter("files/enemy.png", 20, 200, 50, 50)
        enemy_2.speed *= level_speed

        enemies = [enemy_0, enemy_1, enemy_2]

        treasure = GameObject("files/treasure.png", 375, 50, 50, 50)




        # Main loop, used to update all gameplay such as movement, checks and graphics, Runs until is_game_over = True
        while not is_game_over:

            # A loop to get all of the events occuring at any given time. Events are most often mouse movement, mouse and button clicks, or exit events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    is_game_over = True

                elif event.type == pygame.KEYDOWN: # Detect when key is pressed down
                    if event.key == pygame.K_UP: # Move up if up key pressed
                        direction = 1
                    elif event.key == pygame.K_DOWN: # Move down if down key pressed
                        direction = -1

                elif event.type == pygame.KEYUP: # Detect when the key is released
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN: #Stop movement
                        direction = 0



            self.game_screen.fill(white_color)
            self.game_screen.blit(self.image, (0,0))

            treasure.draw(self.game_screen)

            player_character.move(direction, self.heigth) # Update player position
            player_character.draw(self.game_screen) # Draw the player at new position

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if level_speed > 1:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)

            if level_speed > 2:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)




            if player_character.detecte_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render("WIN", True, black_color)
                self.game_screen.blit(text, (300, 350))
                pygame.display.update()
                clock.tick(1)
                break

            else:
                for enemy in enemies:
                    if player_character.detecte_collision(enemy):
                        is_game_over = True
                        did_win = False
                        text = font.render("WASTED", True, black_color)
                        self.game_screen.blit(text, (300, 350))
                        pygame.display.update()
                        clock.tick(1)
                        break

            #game_screen.blit(player_image, (375, 375)) # Usar imagenes
            pygame.display.update() # Update all game graphics
            clock.tick(self.tick_rate) # Tick the clock to update everything within the game



        if did_win:
            self.run_game_loop(level_speed + 0.2)
        else:
            return




class GameObject:

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(object_image, (width, height))
        self.x_pos = x
        self.y_pos = y
        self.width = width
        self.height = height

    def draw(self, background):
        background.blit(self.image, (self.x_pos, self.y_pos))



class PlayerCharacter(GameObject): # Class to represent the character controlled by player

    #How many tiles the character moves per second
    speed = 10

    def __init__(self, image_path, x, y, width, heigth):
        super().__init__(image_path, x, y, width, heigth)

    def move(self, direction, max_height): #move function
        if direction > 0:
            self.y_pos -= self.speed
        elif direction < 0:
            self.y_pos += self.speed

        if self.y_pos >= max_height - 40: # check if is down the bottom of the window.
            self.y_pos = max_height - 40


    def detecte_collision(self, other_body):
        if self.y_pos > other_body.y_pos + other_body.height:
            return False
        elif self.y_pos + self.height < other_body.y_pos:
            return False

        if self.x_pos > other_body.x_pos + other_body.width:
            return False
        elif self.x_pos + self.width < other_body.x_pos:
            return False

        return True



class NonPlayerCharacter(GameObject): # Class to represent the character controlled by player

    #How many tiles the character moves per second
    speed = 7

    def __init__(self, image_path, x, y, width, heigth):
        super().__init__(image_path, x, y, width, heigth)

    def move(self, max_width): #move function
        if self.x_pos <= 20:
            self.speed = abs(self.speed)
        elif self.x_pos >= max_width - 45:
            self.speed = -abs(self.speed)
        self.x_pos += self.speed







# Pygame initialization
pygame.init()

new_game = Game("files/background.png",screen_title, screen_width, screen_height)
new_game.run_game_loop(1)

# Quit pygame and the program
pygame.quit()
quit()



# Basic shapes
#pygame.draw.rect(game_screen, black_color, [350, 350, 100, 100])
#pygame.draw.circle(game_screen, black_color, (400, 300), 50)
