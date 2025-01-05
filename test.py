import pygame

pygame.init()

cell_size = 100
rows, cols = 5, 5
width, height = cols * cell_size, rows * cell_size

colors = {
    0: (255, 255, 255),
    1: (100, 100, 100),
    2: (0, 255, 0)
}

magazyn = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 2, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wizualizacja magazynu")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(rows):
        for col in range(cols):
            color = colors[magazyn[row][col]]
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, (0, 0, 0), (col * cell_size, row * cell_size, cell_size, cell_size), 1)  # Siatka

    pygame.display.flip()

pygame.quit()
