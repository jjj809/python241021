import pygame
import random

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 게임 보드 크기
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLOCK_SIZE = 30

# 테트로미노 모양
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]]
]

class Tetris:
    def __init__(self):
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = self.new_piece()
        self.game_over = False
        self.score = 0

    def new_piece(self):
        shape = random.choice(SHAPES)
        return {
            'shape': shape,
            'x': BOARD_WIDTH // 2 - len(shape[0]) // 2,
            'y': 0
        }

    def valid_move(self, piece, x, y):
        for i, row in enumerate(piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    if (x + j < 0 or x + j >= BOARD_WIDTH or
                        y + i >= BOARD_HEIGHT or
                        self.board[y + i][x + j]):
                        return False
        return True

    def merge_piece(self):
        for i, row in enumerate(self.current_piece['shape']):
            for j, cell in enumerate(row):
                if cell:
                    self.board[self.current_piece['y'] + i][self.current_piece['x'] + j] = 1
        self.clear_lines()
        self.current_piece = self.new_piece()
        if not self.valid_move(self.current_piece, self.current_piece['x'], self.current_piece['y']):
            self.game_over = True

    def clear_lines(self):
        lines_cleared = 0
        for i in range(BOARD_HEIGHT):
            if all(self.board[i]):
                del self.board[i]
                self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])
                lines_cleared += 1
        self.score += lines_cleared ** 2 * 100

    def move(self, dx, dy):
        if self.valid_move(self.current_piece, self.current_piece['x'] + dx, self.current_piece['y'] + dy):
            self.current_piece['x'] += dx
            self.current_piece['y'] += dy
            return True
        return False

    def rotate(self):
        rotated = list(zip(*self.current_piece['shape'][::-1]))
        if self.valid_move({'shape': rotated, 'x': self.current_piece['x'], 'y': self.current_piece['y']}, self.current_piece['x'], self.current_piece['y']):
            self.current_piece['shape'] = rotated

    def draw(self, screen):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, BLUE, (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))

        if self.current_piece:
            for i, row in enumerate(self.current_piece['shape']):
                for j, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(screen, BLUE, 
                            ((self.current_piece['x'] + j) * BLOCK_SIZE, 
                             (self.current_piece['y'] + i) * BLOCK_SIZE, 
                             BLOCK_SIZE - 1, BLOCK_SIZE - 1))

def main():
    pygame.init()
    screen = pygame.display.set_mode((BOARD_WIDTH * BLOCK_SIZE, BOARD_HEIGHT * BLOCK_SIZE))
    pygame.display.set_caption("테트리스")

    clock = pygame.time.Clock()
    game = Tetris()
    fall_time = 0
    fall_speed = 50  # 낮을수록 빠름

    while not game.game_over:
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            if not game.move(0, 1):
                game.merge_piece()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    game.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    game.move(0, 1)
                elif event.key == pygame.K_UP:
                    game.rotate()

        screen.fill(BLACK)
        game.draw(screen)
        pygame.display.flip()

    print(f"게임 오버! 점수: {game.score}")
    pygame.quit()

if __name__ == "__main__":
    main()