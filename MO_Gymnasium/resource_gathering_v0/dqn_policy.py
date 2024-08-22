import mo_gymnasium as mo_gym
import stable_baselines3 as sb3
import numpy as np
from mo_gymnasium.utils import MORecordEpisodeStatistics
import numpy as np
from morl_baselines.multi_policy.multi_policy_moqlearning.mp_mo_q_learning import (
    MPMOQLearning,
)
from morl_baselines.common.utils import make_gif


# Create your environment
#env = mo_gym.make("resource-gathering-v0", render_mode="human")


# Linear scalarizes the environment
env = mo_gym.LinearReward(
    mo_gym.make("resource-gathering-v0"), weight=np.array([0.9, 0.1, 0.0])
)

# Run DQN agent!
agent = sb3.DQN("MlpPolicy", env)
agent.learn(100000)

GAMMA = 0.9
ref_point = np.array([-1.0, -1.0, -2.0])

env = mo_gym.make("resource-gathering-v0")
env = MORecordEpisodeStatistics(env, gamma=GAMMA)  # wrapper for recording statistics

eval_env = mo_gym.make("resource-gathering-v0")  # environment used for evaluation

env.pareto_front(GAMMA)  # known Pareto front

# Your code here:
agent = MPMOQLearning(
    env,
    initial_epsilon=1.0,
    final_epsilon=0.05,
    epsilon_decay_steps=100000,
    gamma=GAMMA,
    dyna=True,
    gpi_pd=True,
    weight_selection_algo="gpi-ls",
    use_gpi_policy=True,
)

agent.train(
    total_timesteps=100000,
    timesteps_per_iteration=10000,
    eval_env=eval_env,
    num_eval_episodes_for_front=50,
    ref_point=ref_point,
)

env.pareto_front(0.9)
agent.linear_support.ccs

env2 = mo_gym.make(
    "resource-gathering-v0", render_mode="rgb_array"
)  # you need to set the render_mode to render the gifs

# Your code here:
make_gif(env2, agent, weight=np.array([0.9, 0.1, 0.0]), fps=10, fullpath="./myagent1")
make_gif(env2, agent, weight=np.array([0.3, 0.7, 0.0]), fps=10, fullpath="./myagent2")
make_gif(env2, agent, weight=np.array([0.0, 1.0, 0.0]), fps=10, fullpath="./myagent3")
