import gymnasium as gym
import mo_gymnasium as mo_gym
from mo_gymnasium.utils import MORecordEpisodeStatistics
import numpy as np
from morl_baselines.common.utils import make_gif
from morl_baselines.multi_policy.multi_policy_moqlearning.mp_mo_q_learning import MPMOQLearning

import time
import os

# create here your own directory to store the results
local_output_directory = "/home/doesburg/Dropbox/02_marl_results/momarl/morl/"
environment_name = "resource_gathering"

start_time = str(time.strftime("%Y-%m-%d_%H:%M:%S"))  # add seconds
file_name = f"{environment_name}_"

destination_directory_source_code = os.path.join(
                local_output_directory, start_time
            )



GAMMA = 0.9
ref_point = np.array([-1., -1., -2.])

env = mo_gym.make("resource-gathering-v0")
env = MORecordEpisodeStatistics(env, gamma=GAMMA)  # wrapper for recording statistics

eval_env = mo_gym.make("resource-gathering-v0") # environment used for evaluation

env.pareto_front(GAMMA) # known Pareto front

agent = MPMOQLearning(
    env,
    initial_epsilon=1.0,
    final_epsilon=0.05,
    epsilon_decay_steps=100000,
    gamma=GAMMA,
    dyna=True,
    gpi_pd=True,
    weight_selection_algo='gpi-ls',
    use_gpi_policy=True
)

agent.train(
    total_timesteps=100000, 
    timesteps_per_iteration=10000, 
    eval_env=eval_env, 
    num_eval_episodes_for_front=50, 
    ref_point=ref_point
    )


print("agent.linear_support.ccs", agent.linear_support.ccs)
print("env.pareto_front(GAMMA) ", env.pareto_front(GAMMA) )


env2 = mo_gym.make("resource-gathering-v0", render_mode='rgb_array')  # you need to set the render_mode to render the gifs


make_gif(env2, agent, weight=np.array([0.9, 0.1, 0.0]), fps=10, fullpath=destination_directory_source_code+"/myagent1")
make_gif(env2, agent, weight=np.array([0.3, 0.7, 0.0]), fps=10, fullpath=destination_directory_source_code+"/myagent2")
make_gif(env2, agent, weight=np.array([0.0, 1.0, 0.0]), fps=10, fullpath=destination_directory_source_code+"/myagent3")
