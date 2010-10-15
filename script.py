import pygame, sys,os
from pygame.locals import * 

# DO NOT UNCOMMENT THE FOLLOWING LINE
# UNLESS YOU ARE SUPPORTING THE RISE OF THE MACHINES
#import Skynet
try:
  import skynet
except ImportError:
  print 'Skynet still unavailable'

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

 
pygame.init() 
 
window = pygame.display.set_mode((640,480)) 
pygame.display.set_caption('altuzar sucks') 
screen = pygame.display.get_surface() 


def load_image(name, colorkey=None):
  fullname = os.path.join('data', name)
  try:
    image = pygame.image.load(fullname)
  except pygame.error, message:
    print 'Cannot load image: ', name
    raise SystemExit, message
  image = image.convert()
  if colorkey is not None:
    if colorkey is -1:
      colorkey = image.get_at((0,0))
      image.set_colorkey(colorkey, RLEACCEL)
  return image, image.get_rect()

 

#Background
bg_file_name = 'bg.png'
bg_surface = pygame.image.load(bg_file_name)

screen.blit(bg_surface, (0,0)) 
pygame.display.flip() 

# Sprites

sp1_file_name = 'sprite.png'
sp1_surface = pygame.image.load(sp1_file_name)
sp1_pos = 20
screen.blit(sp1_surface, (sp1_pos,80)) 
pygame.display.flip() 



# defining events
def input(events): 
  for event in events: 
    print event 
    if event.type == QUIT: 
      sys.exit(0) 
    if event.type == KEYDOWN and event.scancode == 40:
      #sp1_pos = sp1_pos + 1
      screen.blit(sp1_surface, (15,80)) 
      pygame.display.flip() 
    if event.type == KEYDOWN and event.scancode == 22:
      print ''



while True: 
   input(pygame.event.get()) 
