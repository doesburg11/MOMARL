import gymnasium as gym
import mo_gymnasium as mo_gym
from gymnasium.wrappers.record_video import RecordVideo
import time
import os

# Create your environment
env = mo_gym.make("resource-gathering-v0", render_mode="rgb_array")

local_output_directory = "/home/doesburg/Dropbox/02_marl_results/momarl/morl/"
environment_name = "resource-gathering-v0"

start_time = str(time.strftime("%Y-%m-%d_%H:%M:%S"))  # add seconds
file_name = f"{environment_name}_"

destination_directory_source_code = os.path.join(
    local_output_directory, start_time
)

# Wrap the environment to record video
env = RecordVideo(env, video_folder=destination_directory_source_code)

try:
    # Your code to interact with the environment goes here
    observation = env.reset()
    done = False
    while not done:
        action = env.action_space.sample()  # Replace with your action selection logic
        obs, reward, terminated, truncated, info  = env.step(action)
finally:
    # Ensure the environment is closed properly
    env.close()