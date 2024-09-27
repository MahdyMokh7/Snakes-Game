import pygame, consts, sys
from game_manager import GameManager
from snake import Snake


def main():
    player1 = input("First player write your name: ")
    player2 = input("Second player write your name: ")
    pygame.init()
    screen = pygame.display.set_mode((consts.height, consts.width))
    screen.fill(consts.back_color)
    game = GameManager(consts.table_size, screen, consts.sx, consts.sy, consts.block_cells)
    snakes = list()
    for snake in consts.snakes:
        snakes.append(Snake(snake['keys'], game, (snake['sx'], snake['sy']), snake['color'], snake['direction']))

    while True:
        events = pygame.event.get()
        keys = []
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                keys.append(event.unicode)

        game.handle(keys, player1, player2)
        pygame.time.wait(200)


if __name__ == '__main__':
    main()
