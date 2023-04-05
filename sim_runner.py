import pygame

from default import parts
from main import update
from simulation import _strip

def main():
    pygame.init()
    pygame.font.init()
    sections = [ parts.BODY1, parts.BODY2, parts.BODY3, parts.BODY4, parts.BODY5, parts.BODY6, 
                 parts.BODY7, parts.BODY8, parts.BODY9, parts.RB_UP, parts.RB_DOWN, parts.LB_UP,
                 parts.LB_DOWN, parts.PANEL ]
    screen = pygame.display.set_mode((1920, 20 * (len(sections) + 1)))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("monospace", 16)
    running = True
    dt = 0
    texts = []
    for section in sections:
        texts.append(font.render(section.name, True, (255, 255, 255)))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        update(dt)
        
        for i, section in enumerate(sections):
            x = 100
            y = 20 + 20 * i
            text = texts[i]
            screen.blit(texts[i], (x - 20 - text.get_width(), y - text.get_height() / 2))
            for j, n in enumerate(range(section.start, section.end)):
                color = _strip[n]
                pygame.draw.circle(screen, color, (x + 20 * j, y), 8)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    pygame.quit()

main()