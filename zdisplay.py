

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RPG")
pygame.draw.rect(screen, RED, [55, 50, 20, 25], width=0)

class Button():
	def __init__(self, surface, x, y, image, size_x, size_y):
		self.image = pygame.transform.scale(image, (50, 100))
		self.rect = self.image.get_rect()
		self.rect.topleft = (300, 300)
		self.clicked = False
		self.surface = surface

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		self.surface.blit(self.image, (self.rect.x, self.rect.y))

		return action