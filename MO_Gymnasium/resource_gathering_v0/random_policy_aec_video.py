import gymnasium as gym
import mo_gymnasium as mo_gym
# Create your environment
env = mo_gym.make("mo-mountaincar-v0", render_mode="rgb_array")
from gymnasium.wrappers.record_video import RecordVideo

import time
import os


local_output_directory = "/home/doesburg/Dropbox/02_marl_results/survivalreproduction_results/"
environment_name = "mountaincar"

start_time = str(time.strftime("%Y-%m-%d_%H:%M:%S"))  # add seconds
file_name = f"{environment_name}_"

destination_directory_source_code = os.path.join(
                local_output_directory, start_time
            )


env = RecordVideo(
    env, 
    destination_directory_source_code, 
    episode_trigger=lambda e: True,
    step_trigger=None,
    name_prefix="random_policy_aec",
    video_length=200,
    )



# Run the environment for a specified number of episodes
num_episodes = 1  # Set the number of episodes you want to run
for episode in range(num_episodes):
    n_steps = 0
    obs = env.reset()
    done = False

    while not done:
        n_steps += 1
        obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
        done = terminated or truncated

    print(f"Episode {episode + 1} done in {n_steps} steps")
    print("Terminated: ", terminated)
    print("Truncated: ", truncated)