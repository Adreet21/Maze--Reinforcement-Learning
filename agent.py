'''
Name:Syed Shahmeer Rahman
CCID: 1756142
'''

import numpy as np
from action_value_table import ActionValueTable

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
GAMMA = 0.95
STEP_SIZE = 0.25
EPSILON = 0.1

class QLearningAgent:
    def __init__(self, dimension):
        self.actions = [UP, DOWN, LEFT, RIGHT]
        num_actions = len(self.actions)
        self.values = ActionValueTable(dimension, num_actions)
        self.gamma = GAMMA
        self.step_size = STEP_SIZE
        self.epsilon = EPSILON

    def update(self, state, action, reward, next_state, done):
        current = self.values.get_value(state, action)
        if not done:
            next_max = -np.inf
            for x in self.actions:
                value = self.values.get_value(next_state, x)
                if value > next_max:
                    next_max = value
            target = reward + self.gamma * next_max
        else:
            target = reward
        update = current + self.step_size * (target - current)
        self.values.set_value(state, action, update)

    def get_action(self, state):
        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.actions)
        else:
            values = []
            for action in self.actions:
                value = self.values.get_value(state, action)
                values.append(value)
            max_value = np.max(values)
            best_actions = []
            for action, value in zip(self.actions, values):
                if value == max_value:
                    best_actions.append(action)
            action = np.random.choice(best_actions)
        return action

    def get_greedy_action(self, state):
        values = []
        for action in self.actions:
            value = self.values.get_value(state, action)
            values.append(value)
        max_value = np.max(values)
        best_actions = []
        for action, value in zip(self.actions, values):
            if value == max_value:
                best_actions.append(action)
        action = np.random.choice(best_actions)
        return action