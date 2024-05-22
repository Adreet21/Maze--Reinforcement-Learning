# MAZE Solving (Reinforcement Learning)

This is a maze problem where there are keys, fires, and a door. The environment was modeled as an MDP (Markov decision process).

The objective is for the agent to escape through the exit door using the key while avoiding the fire.

What is Q-Learning?
I used Q-Learning to solve the maze. Q-Learning is a reinforcement learning algorithm that finds an optimal action selection policy for any finite MDP environment.
Q-Learning helps an agent learn to maximize the total reward over time through repeated interactions with the environment, even when the model of that environment is not known.

How have I implemented it?
For exploring the environment, I used the epsilon-greedy behavior policy.

The formula used:
New Q(s,a) = Q(s,a) + α[R(s,a) + γ max Q'(s',a') - Q(s,a)] where s = State
                                                                 a = Action
                                                                 α = Learning Rate
                                                                 γ = Discount Rate
                                                                 Q(s,a) = Current Q-Value
                                                                 max Q'(s',a') = Maximum expected future reward
                                                                 R(s,a) = Reward for taking an action at that state
The values used were: Step Size = 0.25
                      Epsilon = 0.1
                      γ(Gamma) = 0.95
                                                            


## Installation

Make a clone of all the files in the repository.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following:

```bash
pip install matplotlib
pip install numpy
pip install pygame
pip install tqdm
```
Make sure you are using the correct Python (ideally Python 3).
Keep all the documents in the same folder; if not, redirect them to the codes accordingly.
Run the main.py file

## Output

After successfully running the code in the terminal, there should be a progress bar.
After it reaches 100%, a maze map will automatically open in another window and visually show you the best path taken by the agent.

## Not functioning?
If you run into difficulties or error in the code please feel free to reach out.
Email: contact@shahmeer.xyz