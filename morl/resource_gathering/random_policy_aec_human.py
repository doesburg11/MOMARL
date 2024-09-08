import mo_gymnasium as mo_gym

# Create your environment
env = mo_gym.make("resource-gathering-v0", render_mode="human")

# Reset the environment
env.reset()
done = False

# Run the environment for a specified number of episodes
num_episodes = 1  # Set the number of episodes you want to run
for episode in range(num_episodes):
    n_steps = 0
    obs = env.reset()
    done = False

    while not done:
        n_steps += 1
 