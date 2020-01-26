
"""
Author: Hussein Baba Fuseini
Date: 03/05/2019
"""
import pygame, sys
from pygame.locals import *
from random import randint
from resource import  bite, climb, post

pygame.init()

class ludo:
    """
    This is the game class which contains methods 
    for running the game and loading necessary files
    """
    def __init__(self):
        self.image = self.get_image()
        self.die = self.get_die()
        self.bite = bite
        self.climb = climb
        self.post = post
        self.center = (175,245)
        self.conpost = (245, 245)
        self.dieSize = (100,100)    
        self.diepost = (770,365)
        self.dieS = 5
        self.score = 1
        self.pst = 1
        self.screen = pygame.display.set_mode((900,805))
        self.sound = False
        self.able = True
        pygame.display.set_caption("Ludo: Snake And Ladder")
        pygame.font.init()
        self.fnt = pygame.font.SysFont('Times New Roman', 30)
        self.text = self.fnt.render('Press ''A'' to roll the die  Or Press ''R'' to restart', False, (255, 255,255)) 
        self.restart = self.fnt.render('Press R to replay or ESCAPE to Quit ', False, (255, 255,255))

    def run(self):
        """
        The run method contains the main loop of the game 
        and it is called to enable the user play the game.
        """
        while True:
            """This part of the methods handles the actions like clicking, 
                rolling of the ludo die and restarting the game"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) :
                    sys.exit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_a and self.able:
                    self.soundplay('sound\dice.mp3')
                    pygame.time.delay(700)
                    self.dieS = randint(1,6)
                    self.score = self.pst + self.dieS
                    self.dieS -= 1
                    self.sound = True
                    
                "This fuction will help users restart the game"
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.dieS = 5
                    self.score = 1
                    self.pst = 1
                    self.able = True
            '''
            This Part of the run method checks whether the user has won or  
            otherwise
            '''    
            if self.score == 100:
                self.congr()
              
            elif self.score < 100:
                self.display()
                if self.score in self.climb:
                    self.soundplay('sound\climb.mp3')
                    self.score= self.climb[self.score]
                    self.elevate("ladder")
                    
                elif self.score in self.bite:
                    self.soundplay('sound\sll.mp3')
                    self.elevate("snake")
                    self.score = self.bite[self.score]  
                self.pst = self.score

            else:
                self.above()
            
            
    def scale(self,img, size):
        """
        This method in the class Ludo transforms or scales images to a desired size
        """
        return pygame.transform.scale(img, size)

    def get_die(self):
        """
        get_die() return loaded images of the 6 sides of a Ludo die
        """
        return  [self.scale(pygame.image.load("img\die1.png"),(100,100)),
                self.scale(pygame.image.load("img\die2.png"),(100,100)),
                self.scale(pygame.image.load("img\die3.png"),(100,100)),
                self.scale(pygame.image.load("img\die4.png"),(100,100)),
                self.scale(pygame.image.load("img\die5.png"),(100,100)),
                self.scale(pygame.image.load("img\die6.png"),(100,100))]

    def get_image(self):
        '''
        get_image() uploads necessary images for the game
        '''
        return {"snake":self.scale(pygame.image.load('img\jk.png'),(500,500)),
                    "ladder":self.scale(pygame.image.load("img\lad.png"),(250,500)),
                    "BG":self.scale(pygame.image.load('img\ludo2.jpg'),(700,700)),
                    "local":self.scale(pygame.image.load('img\local.png'),(70,70)),
                    "congrats":self.scale(pygame.image.load('img\congrats.png'),(450,204)),
                    "bg": self.scale(pygame.image.load("img\mm.png"),(900,805))}
    
    def display(self):
        """
        This method is responsible for GUI of the game.
        it displays different images at different scores
        """
        for i in range(self.pst,self.score + 1):
            pygame.time.delay(400)
            if self.sound and i < self.score:
                self.soundplay('sound\move.mp3')
            self.screen.blit(self.image["bg"],(0,0))
            self.screen.blit(self.die[self.dieS],self.diepost)
            self.screen.blit(self.image["BG"],(35,70))
            self.screen.blit(self.image['local'],self.post[i])
            self.screen.blit(self.text,(35,0))
            pygame.display.flip()
        self.sound = False   
        
    def elevate(self,place):
        """
        This method diplays images to inform the user that they
        have been elevated to a higher position or  lower  
        """
        pygame.time.delay(400)
        self.screen.blit(self.image["bg"],(0,0))
        self.screen.blit(self.die[self.dieS],self.diepost)
        self.screen.blit(self.image["BG"],(35,70))
        self.screen.blit(self.image[place], self.center)
        self.screen.blit(self.image['local'],self.post[self.score])
        pygame.display.flip()
        
    def above(self):
        """
        This method informs the user to play a specific number when his/her 
        current position is between 95 and 100
        """
        self.screen.blit(self.image["bg"],(0,0))
        self.screen.blit(self.die[self.dieS],self.diepost)
        self.screen.blit(self.image["BG"],(35,70))
        self.screen.blit(self.image['local'],self.post[self.pst])
        self.screen.blit(self.fnt.render('Play {} to win'.format(100-self.pst), False, (255, 255,255)),(35,0))
        pygame.display.flip()

    def congr(self):
        """
        This method is diplays images to congratulate the user for winning
        """
        if self.able:
            self.screen.blit(self.image["bg"],(0,0))
            self.screen.blit(self.image["congrats"],self.conpost)
            self.screen.blit(self.restart,(35,0))
            self.screen.blit(self.fnt.render("You've Won", False, (255, 255,255)),(35,700))
            self.soundplay('sound\congrats.mp3')
            pygame.display.flip()
            self.able = False

    def soundplay(self, music):
        '''
        soundplay loads and plays a particular sound
        '''
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()

if __name__ == "__main__":
    """
    When this file is executed, an instance of the class Ludo 
    is created and the run function is called to initiate the game
    """
    play = ludo()
    play.run()
'''
Caution: The Snake bite may scare you, make sure you do not throw your laptop away
'''