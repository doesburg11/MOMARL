

from momaland.envs.beach import mobeach_v0
import numpy as np
import time

sleep_time = 0.1

"""
Arguments environment mobeach_v0.env:
num_timesteps (int): number of timesteps in the domain. Default: 1
num_agents (int): number of agents in the domain. Default: 100
reward_mode (str): the reward mode to use (‘individual’, or ‘team’). Default: individual
sections (int): number of beach sections in the domain. Default: 6
capacity (int): capacity of each beach section. Default: 7
type_distribution (tuple): the distribution of agent types in the domain. Default: 2 types equally distributed (0.3, 0.7).
position_distribution (tuple): the initial distribution of agents in the domain. Default: uniform over all sections (None).
render_mode (str): render mode. Default: None
"""

env=mobeach_v0.env(
    num_timesteps=1,
    num_agents=10,
    reward_mode="individual",
    sections=6,
    capacity=7,
    render_mode="human"
    )

env.reset()
episode_rewards = []
for agent in env.agent_iter():
    # the rewards are vectors!
    observation, vec_reward, termination, truncation, info = env.last()
    print(f"Agent {agent} received observation: {observation}")
    #print(f"Agent {agent} received reward: {vec_reward}")
    episode_rewards.append(vec_reward)
    if termination or truncation:
        action = None
    else:
        action = env.action_space(agent).sample()
    env.step(action)
    time.sleep(sleep_time) 
env.close()

