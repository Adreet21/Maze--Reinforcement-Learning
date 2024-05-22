import os
import numpy as np
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3  # agents actions


class Maze():
    """
    A maze gridworld environment
    """

    def __init__(self):
        self.grid = np.zeros((12, 12))

        # populate grid with walls
        walls = [
            [2, 2],
            [3, 2],
            [4, 2],
            [5, 2],
            [6, 2],
            [2, 4],
            [3, 4],
            [4, 4],
            [9, 2],
            [9, 3],
            [9, 4],
            [9, 5],
            [8, 5],
            [7, 5],
            [6, 5],
            [5, 6],
            [5, 7],
            [5, 8],
            [5, 9],
            [2, 7],
            [2, 8],
            [2, 9],
            [3, 7],
            [3, 8],
            [3, 9],
            [10, 7],
            [9, 7],
            [8, 7],
            [7, 7],
            [7, 8],
            [7, 9],
            [8, 9]
        ]

        # add outer borders
        self.grid[0, :] = np.ones_like(self.grid[0, :])
        self.grid[11, :] = np.ones_like(self.grid[11, :])
        self.grid[:, 0] = np.ones_like(self.grid[:, 0])
        self.grid[:, 11] = np.ones_like(self.grid[:, 11])

        for wall in walls:
            self.grid[wall[0], wall[1]] = 1 # 1 signifies wall

        self.key = [4, 6]
        self.has_key = 0

        self.start = [10, 1]
        self.end = [8, 8]

        self.fires = [
            [5, 4],
            [4, 9]
        ]

        self.loc = self.start  # the location of the agent

        self.episode_length = 0
        self.MAX_LENGTH = 1000
        self.dimension = [2, 12, 12]


    def reset(self):
        self.has_key = 0
        self.loc = self.start
        self.episode_length = 0
        return [self.has_key] + self.loc


    def step(self, action):
        self.episode_length += 1
        row, col = self.loc  # row major format

        if action == UP:
            row -= 1
        elif action == RIGHT:
            col += 1
        elif action == DOWN:
            row += 1
        elif action == LEFT:
            col -= 1

        if self.grid[row, col]:  # if agent hits a wall,
            row, col = self.loc

        if [row, col] == self.end:
            if self.has_key:
                reward = 1.0
                is_done = True
            else:
                reward = 0.0
                is_done = False
        elif [row, col] in self.fires:
            reward = -100.0
            is_done = False

        elif [row, col] == self.key:
            reward = 0.0
            self.has_key = 1
            is_done = False
        else:
            reward = 0.0
            is_done = False

        self.loc = [row, col]

        if self.episode_length >= self.MAX_LENGTH:
            is_done = True

        return [self.has_key] + self.loc, reward, is_done, None


    def render(self, screen):
        def load_and_tranform_img(path, size):
            '''
            loads an image from path and scales it to be size
            '''
            img = pygame.image.load(path)
            img = pygame.transform.scale(img, size)
            return img

        screen.fill((0, 0, 0))
        width, height = screen.get_size()
        # indices are reversed since self.grid is row major format
        width_pix_per_tile = width//self.grid.shape[1]
        height_pix_per_tile = height//self.grid.shape[0]

        wall_img = load_and_tranform_img(os.path.join(
            'assets', 'wall.png'), (width_pix_per_tile, height_pix_per_tile))

        # draw the walls
        y_pos = 0  # start at the top
        for row in range(self.grid.shape[0]):
            x_pos = 0
            for col in range(self.grid.shape[1]):
                if self.grid[row, col]:
                    screen.blit(wall_img, (x_pos, y_pos))
                x_pos += width_pix_per_tile
            y_pos += height_pix_per_tile

        # draw the key
        if not self.has_key:
            key_img = load_and_tranform_img(os.path.join(
                'assets', 'key.png'), (width_pix_per_tile, height_pix_per_tile))
            screen.blit(
                key_img, (self.key[1]*width_pix_per_tile, self.key[0]*height_pix_per_tile))

        # draw the door
        door_img = load_and_tranform_img(os.path.join(
            'assets', 'door_cropped.png'), (width_pix_per_tile, height_pix_per_tile))
        screen.blit(
            door_img, (self.end[1]*width_pix_per_tile, self.end[0]*height_pix_per_tile))

        # draw fire obstracles
        fire_img = load_and_tranform_img(os.path.join(
            'assets', 'fire.png'), (width_pix_per_tile, height_pix_per_tile))
        for fire in self.fires:
            screen.blit(
                fire_img, (fire[1]*width_pix_per_tile, fire[0]*height_pix_per_tile))

        # draw the agent
        if not (np.array_equal(self.loc, self.end) and self.has_key):
            agent_img = load_and_tranform_img(os.path.join(
                'assets', 'agent.png'), (width_pix_per_tile, height_pix_per_tile))
            screen.blit(
                agent_img, (self.loc[1]*width_pix_per_tile, self.loc[0]*height_pix_per_tile))

        pygame.display.update()
