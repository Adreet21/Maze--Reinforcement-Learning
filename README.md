# MAZE Solving (Reinforcement Learning)

This is a maze problem where there are keys, fires, and a door. The environment was modeled as an<br>MDP (Markov decision process).

The objective is for the agent to escape through the exit door using the key while avoiding the fire.

What is Q-Learning?<br>
I used Q-Learning to solve the maze. Q-Learning is a reinforcement learning algorithm that finds an optimal action selection policy for any finite MDP environment.<br>
Q-Learning helps an agent learn to maximize the total reward over time through repeated interactions with the environment, even when the model of that environment is not known.

How have I implemented it?<br>
For exploring the environment, I used the epsilon-greedy behavior policy.<br>

The formula used:<br>
New Q(s,a) = Q(s,a) + α[R(s,a) + γ max Q'(s',a') - Q(s,a)] where s = State<br>
                                                                 a = Action<br>
                                                                 α = Learning Rate<br>
                                                                 γ = Discount Rate<br>
                                                                 Q(s,a) = Current Q-Value<br>
                                                                 max Q'(s',a') = Maximum expected future reward<br>
                                                                 R(s,a) = Reward for taking an action at that state<br>

The values used were: Step Size = 0.25<br>
                      Epsilon = 0.1<br>
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
Make sure you are using the correct Python (ideally Python 3).<br>
Keep all the documents in the same folder; if not, redirect them to the codes accordingly.<br>
Run the main.py file

## Output

After successfully running the code in the terminal, there should be a progress bar.<br>
After it reaches 100%, a maze map will automatically open in another window and visually show you the best path taken by the agent.

## Not functioning?
If you run into difficulties or error in the code please feel free to reach out.<br>
Email: contact@shahmeer.xyz