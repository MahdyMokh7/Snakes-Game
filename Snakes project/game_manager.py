import consts
import pygame
from cell import Cell


class GameManager:

    def __init__(self, size, screen, sx, sy, block_cells):
        self.screen = screen
        self.size = size
        self.cells = []
        self.sx = sx
        self.sy = sy
        self.snakes = list()
        self.turn = 0
        for i in range(self.size):
            tmp = []
            for j in range(self.size):
                tmp.append(Cell(screen, sx + i * consts.cell_size, sy + j * consts.cell_size))
            self.cells.append(tmp)
        for cell in block_cells:
            self.get_cell(cell).set_color(consts.block_color)

    def add_snake(self, snake):
        self.snakes.append(snake)

    def get_cell(self, pos):
        try:
            return self.cells[pos[0]][pos[1]]
        except:
            return None

    def kill(self, killed_snake):
        self.snakes.remove(killed_snake)

    def get_next_fruit_pos(self): # returns tuple (x, y) that is the fruit location
        ret = -1, -1
        mx = -100

        for i in range(0, self.size):
            for j in range(0, self.size):

                mn = 100000000

                for x in range(0, self.size):
                    for y in range(0, self.size):
                        if self.get_cell((x, y)).color != consts.back_color:
                            mn = min(mn, int( abs(x-i) + abs(y-j) ))

                if mn > mx:
                    mx = mn
                    ret = i, j

        return ret

    def handle(self, keys, player1, player2):
        print("now gameManager")
        print(self.snakes)
        for snake in self.snakes:
            snake.handle(keys)
        for snake in self.snakes:
            snake.next_move()
        self.turn += 1
        if self.turn % 10 == 0:
            cell = self.get_next_fruit_pos()
            cell = self.get_cell(cell)
            cell.set_color(consts.fruit_color)

        self.render_scoreboard(player1, player2)

    def render_scoreboard(self, player1, player2):
        self.clear_score_area()
        # Render the scores
        font = pygame.font.Font(None, 25)
        player1_text = font.render(f"{player1}: {self.snakes[0].get_score()}", True, (0, 0, 0))
        player2_text = font.render(f"{player2}: {self.snakes[1].get_score()}", True, (0, 0, 0))
        # Blit the scores onto the screen
        self.screen.blit(player1_text, (50, 20))
        self.screen.blit(player2_text, (150, 20))
        pygame.display.flip()

    def clear_score_area(self):
        # Clear the area where the scores are displayed
        score_area = pygame.Rect(30, 10, 250, 35)  # Define the area to clear
        pygame.draw.rect(self.screen, (255, 255, 255), score_area)
