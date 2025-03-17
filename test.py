import pygame
import math
import random


# initialize pygame
pygame.init()

# screen definitions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Measles Herd Immunity Simulation")

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)        # infected
GREEN = (0,255,0)      # immune
BLUE = (0,0,255)       # susceptible
GRAY = (128,128,128)   # deceased

# Measles Herd Immunity Simulation Parameters
POPULATION = 200                 # Total number of people in the simulation

INFECTION_RADIUS = 40            # Distance within which an infected 
                                 # person can spread the infection

INFECTION_PROBABILITY = 0.90     # Represents the chance of spreading
                                 # the infection when an infected person 
                                 # is near a susceptible person

VACCINATED_PERCENT = 0.60        # Proportion of the population that
                                 # starts as immune (vaccinated)

HERD_IMMUNITY_THRESHOLD = 0.70   # The percentage of immune people
                                 # needed to stop uncontrolled spread

DEATH_PROBABILITY = 0.02         # Probability an infected person dies

DAYS_TO_DEATH = 10               # Minimum number of days an infected person must
                                 # be sick before they have a chance to die

print("before class")

# START - INDIVIDUAL PERSON CLASS *************************************************
class Person:
    def __init__(self, x, y, status = "susceptible", age = "adult"):
        self.x = x
        self.y = y
        self.status = status

        self.color = BLUE if self.status == "susceptible" else\
                     GREEN if self.status == "immune" else\
                     RED if self.status == "infected" else\
                     GRAY # therefore == "deceased"
        
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-5, 5)

        self.infection_days = 0

        self.age = age
        
    def move(self):
        if self.status != "deceased":
            self.x += self.speed_x
            self.y += self.speed_y

        if self.x <= 0 or self.x >= WIDTH:
            self.speed_x *= -1
        
        if self.y <=0 or self.y >= HEIGHT:
            self.speed_y *= -1

    def draw(self):        
        pygame.draw.circle(screen,self.color,(int(self.x), int(self.y)), 20)
# END  -  INDIVIDUAL PERSON CLASS *************************************************

# initialize population
people = []
for _ in range(POPULATION):
    x, y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
    people.append(Person(x,y, "susceptible"))


# infect one random person
# random.choice([p for p in people if p.status == "susceptible"]).status = "infected"

def check_infection():
    for person in people:
        if person.status == "infected":
            person.infection_days += 1
            
            # If infected for long enough, introduce a probability of death
            if person.infection_days >= DAYS_TO_DEATH and random.random() < DEATH_PROBABILITY:
                person.status = "deceased"
                continue
            
            for other in people:
                if other.status == "susceptible":
                    dist = math.hypot(person.x - other.x, person.y - other.y)
                    if dist < INFECTION_RADIUS and random.random() < INFECTION_PROBABILITY:
                        other.status = "infected"


# Main loop
running = True
clock = pygame.time.Clock()
print("hello")
# days = 0
# # herd_immunity_achieved = False
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for person in people:
        person.move()
        person.draw()

    check_infection()








    pygame.display.flip()
    clock.tick(30)
    # days += 1

pygame.quit()