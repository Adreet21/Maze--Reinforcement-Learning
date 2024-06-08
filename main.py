
"""
This is the main file that will run the agent in agent.py on the environment specified
in environment.py. The agent will learn to navigate the maze using Q-learning.
"""

import time
import numpy as np
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import matplotlib.pyplot as plt 

from environment import Maze
from agent import QLearningAgent

from tqdm import tqdm


NUM_EPISODES = 1000

def plot_learning(episode_lengths):
    '''
    Plots the length of the episodes
    '''

    episode_lengths = np.convolve(episode_lengths, np.ones(10)/10, mode='valid')  
    plt.xlabel('Episode')
    plt.ylabel('Length of episode')
    plt.savefig('learning_curve.png', bbox_inches='tight', dpi=300)


def display_final_epsiode(agent, env):
    '''
    Displays a single episode of the agent acting greedily in the environment. 
    '''
    state = env.reset()
    pygame.init()
    
    # if the screen is very small or very large, change these values to desired resolution
    screen = pygame.display.set_mode((900, 900))
    running = True

    env.render(screen)
    time.sleep(0.2)
    while running:
        action = agent.get_greedy_action(state)
        new_state, reward, done, _ = env.step(action)
        state = new_state
        env.render(screen)
        time.sleep(0.2)

        # check if epsode has terminated, if so, return
        if done == True:
            time.sleep(1)
            return
        # check if window has been exited, if so, return
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


def run_qlearning():
    env = Maze()
    agent = QLearningAgent(env.dimension)

    episode_lengths = [] # stores the length of each episode

    t = tqdm(range(NUM_EPISODES))

    for episode in t:
        if len(episode_lengths) >= 10:
            t.set_description('Avg. length of last 10 episodes: {:.1f}'.format(
                np.mean(episode_lengths[-10:])))

        state = env.reset()  # get the initial state of the environment
        done = False  # boolean whether the episode has terminated
        episode_length = 0  # counter for the length of the episode

        while not done:
            action = agent.get_action(state)
            new_state, reward, done, _ = env.step(action)
            agent.update(state, action, reward, new_state, done)
            state = new_state
            episode_length += 1

        episode_lengths.append(episode_length)

    display_final_epsiode(agent, env)
    plot_learning(episode_lengths)


if __name__ == "__main__":
    run_qlearning()
