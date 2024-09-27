import consts


class Snake:

    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    direction_opposite = dict()
    direction_opposite['UP'] = 'DOWN'
    direction_opposite['DOWN'] = 'UP'
    direction_opposite['LEFT'] = 'RIGHT'
    direction_opposite['RIGHT'] = 'LEFT'

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)
        self.score = 0

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def next_move(self):
        cell_head = self.get_head()
        cell_head = cell_head[0] + self.dx[self.direction], cell_head[1] + self.dy[self.direction]   # ################

        # for the states that the snake goes out of the border
        cell_head = self.val(cell_head[0]), self.val(cell_head[1])
        if self.game.get_cell(cell_head).color != consts.fruit_color and\
        self.game.get_cell(cell_head).color != consts.back_color:
            self.game.kill(self)
        elif self.game.get_cell(cell_head).color == consts.fruit_color:
            self.cells.append(cell_head)
            self.game.get_cell(cell_head).set_color(self.color)
            self.score += 1
        elif self.game.get_cell(cell_head).color == consts.back_color:
            self.cells.append(cell_head)
            self.game.get_cell(cell_head).set_color(self.color)
            self.game.get_cell(self.cells[0]).set_color(consts.back_color)
            self.cells.pop(0)

    def handle(self, keys):
        for key in keys:
            if key in self.keys.keys():
                if self.keys[key] != self.direction and\
                self.keys[key] != self.direction_opposite[self.direction]:
                    self.direction = self.keys[key]
                    return

    def get_score(self):
        return self.score
