import momultiwalker_stability_v0
import numpy as np

env=momultiwalker_stability_v0.env(render_mode="human")


env.reset()
episode_rewards = []
for agent in env.agent_iter():
    # the rewards are vectors!
    observation, vec_reward, termination, truncation, info = env.last()
    """
    print("agent", agent)
    print("vec_reward", vec_reward)
    print()
    """
    episode_rewards.append(vec_reward)
    if termination or truncation:
        action = None
    else:
        action = env.action_space(agent).sample()
    env.step(action)
env.close()

# rewards are stored in a dictionary, can be accessed per agent
#print("episode_rewards", episode_rewards)

#print("finished AEC")

"""
# new parallel env
env = momultiwalker_stability_v0.parallel_env(render_mode="human")
observations, infos = env.reset()
episode_rewards = []
while env.agents:
    actions = {agent: env.action_space(agent).sample() for agent in env.agents}
    observations, vec_rewards, terminations, truncations, infos = env.step(actions)
    episode_rewards.append(vec_rewards)
env.close()

# rewards are stored in a dictionary, can be accessed per agent
episode_rewards[0]
# rewards of all agents from the first step
print()
print("episode_rewards[0]", episode_rewards[0])
print("episode_rewards[1]", episode_rewards[1])
print()

episode_rewards[0:len(env.possible_agents)]
print("episode_rewards[0:len(env.possible_agents)]", episode_rewards[0:len(env.possible_agents)])
print()
print("finished parallel")
"""