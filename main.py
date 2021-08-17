import pygame, sys, random

pygame.init()

SCREEN = pygame.display.set_mode((1280,650))
Clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

# images
WOOD_BG = pygame.image.load('Wood_BG.png')
FLY_SURFACE = pygame.image.load('fly.png')
CROSSHAIR = pygame.image.load('crosshair.png')

# font
GAME_FONT = pygame.font.Font(None,60)
TEXT_SURFACE = GAME_FONT.render('You Won!',True,(255,255,255))
TEXT_RECT = TEXT_SURFACE.get_rect(center = (640,300))


fly_list = []
for fly in range(20):
	fly_position_x = random.randrange(50,1200)
	fly_position_y = random.randrange(120,600)
	fly_rect = FLY_SURFACE.get_rect(center = (fly_position_x, fly_position_y))
	fly_list.append(fly_rect)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEMOTION:
			CROSSHAIR_rect = CROSSHAIR.get_rect(center = event.pos)
		if event.type == pygame.MOUSEBUTTONDOWN:
			for index,fly_rect in enumerate(fly_list):
				if fly_rect.collidepoint(event.pos):
					del fly_list[index]

	SCREEN.blit(WOOD_BG,(0,0))

	for fly_rect in fly_list:
		SCREEN.blit(FLY_SURFACE,fly_rect)

	if len(fly_list) <= 0:
		SCREEN.blit(TEXT_SURFACE,TEXT_RECT)

	SCREEN.blit(CROSSHAIR,CROSSHAIR_rect)
	
	pygame.display.update()
	Clock.tick(120)