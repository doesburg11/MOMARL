

from momaland.envs.item_gathering import moitem_gathering_v0
import numpy as np
import time

sleep_time = 0.01

DEFAULT_MAP = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 0],
        [0, 0, 4, 0, 4, 5, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 3, 3, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
    ]
)

alternative_map = np.array(
    [
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 2, 4, 0, 0, 0, 0],
        [0, 0, 4, 2, 4, 5, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 3, 0, 5, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 4, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]
)


env=moitem_gathering_v0.env(
    num_timesteps=500,
    initial_map=DEFAULT_MAP, 
    render_mode="human"
    )

env.reset()
episode_rewards = []
for agent in env.agent_iter():
    # the rewards are vectors!
    observation, vec_reward, termination, truncation, info = env.last()
    #print(f"Agent {agent} received reward: {vec_reward}")
    episode_rewards.append(vec_reward)
    if termination or truncation:
        action = None
    else:
        action = env.action_space(agent).sample()
    env.step(action)
    time.sleep(sleep_time) 
env.close()

