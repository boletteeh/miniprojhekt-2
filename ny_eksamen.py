import pygame

# Erklærer en klasse ved navn MazeSolver
class PathFinder:
    
    # Initfunktionen 
    def __init__(self, grid, start_position, end_position):
        pygame.init()

        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Miniprojekt 2")

        self.width = 60
        self.height = 60

        self.grid = grid
        self.start_position = start_position
        self.end_position = end_position

        self.frontier = [start_position]
        self.came_from = {start_position: None}

    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 0:
                    pygame.draw.rect(self.screen, (255, 255, 255), (x * self.width, y * self.height, self.width, self.height))
                if cell == 1:
                    pygame.draw.rect(self.screen, (255, 0, 255), (x * self.width, y * self.height, self.width, self.height))

    def draw_start_end(self):
        pygame.draw.rect(self.screen, (0, 0, 255), (self.start_position[1] * self.width, self.start_position[0] * self.height, self.width, self.height))
        pygame.draw.rect(self.screen, (0, 0, 255), (self.end_position[1] * self.width, self.end_position[0] * self.height, self.width, self.height))

    def draw_path(self, path):
        for position in path:
            pygame.draw.circle(self.screen, (255, 255, 0), (position[1] * self.width + self.width // 2, position[0] * self.height + self.height // 2), 10)

    # Finder de gyldige naboer til en position. Til sidst for denne funktion returneres de gyldige naboer.
    def neighbors(self, position):
        x, y = position
        possible_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        valid_neighbors = []

        # Der bruges et forloop. 
        for neighbor in possible_neighbors:
            # Får adgang til x og y koordinaterne for den nuværende nabo.
            nx, ny = neighbor
            # Tjek om naboens position er inden for gitterets grænser.
            if 0 <= nx < len(self.grid) and 0 <= ny < len(self.grid[0]):
                # Tjek om naboen position ikke er en forhindring (værdi 1) eller en start- eller slutposition.
                if self.grid[nx][ny] != 1:
                    # Tilføjer de gyldige naboer til listen valid_neighbors
                    valid_neighbors.append(neighbor)
        # Der returners listen af gyldige naboer            
        return valid_neighbors


    def find_path(self):
        # Sålænge frontier listen ikke er tom, kører loopet.
        while self.frontier:
            # Fjerner den første position fra frontier listen
            current = self.frontier.pop()
            # Gennemgår naboerne til den nuværende position
            for next_position in self.neighbors(current):
                # Hvis nabopositionen ikke er besøgt
                if next_position not in self.came_from:
                    # Tilføj nabopositionen til frontier listen
                    self.frontier.append(next_position)
                    # Registrer at den nuværende postition er kommet fra nabopositionen
                    self.came_from[next_position] = current

        # Opsætter to variabler til at rekonstruere stien fra end_position til start_position
        current = self.end_position
        path = []
        # Rekonstruerer stien ved at gå tilbage fra end til start
        while current != self.start_position:
            # Tilføjer den nuværende position til stien
            path.append(current)
            # Gå tilbage til den position vi kom frem
            current = self.came_from[current]
        # Returnerer den beregnede sti    
        return path

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.draw_grid()
            self.draw_start_end()
            path = self.find_path()
            self.draw_path(path)

            pygame.display.flip()
            #print(self.came_from)


# Erklærer en variable ved navn grid, som indeholder en liste bestående af 10 lister. 
grid = [[0, 1, 0, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]]

# Angiver start- og slutpostion. Start position befinder sig således i liste nr. 2 samt i 1 element i listen
start_position = (2, 1)
end_position = (8, 8)

PathFinder(grid, start_position, end_position).run()