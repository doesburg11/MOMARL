# The Project
This Multi-Objective Reinforcement Learning (MORL) project aimes to balance the objectives of survival and reproduction.

Consider a scenario modeling the behavior of an agent, such as an animal, using MORL. The agent has two primary objectives: **survival** and **reproduction**. This example could apply to a simulated ecosystem where animals need to balance finding food, avoiding predators, and seeking mates to reproduce.

### 1. **Definition of the Objectives:**

- **Survival:**
  - The agent needs to avoid threats (e.g., predators, environmental hazards) and maintain its energy levels by finding and consuming food. The longer the agent survives, the higher the reward.
  
- **Reproduction:**
  - The agent needs to find a mate and reproduce to ensure the survival of its species. Successfully reproducing yields a high reward, but finding a mate might expose the agent to risks (e.g., traveling to new areas with predators).

### 2. **Design of the Reward Functions:**

- **Survival Reward:**
  - The agent receives a continuous reward for staying alive. This could be a small positive reward at each time step that increases with the amount of time the agent survives.
  - R<sub><i>survival</i></sub> = 1 per time step alive.
  - The agent is penalized heavily for dying (e.g., being caught by a predator or starving).
  - R<sub><i>death</i></sub> = -100 when the agent dies.

- **Reproduction Reward:**
  - The agent receives a significant reward for successfully reproducing.
  - R<sub><i>reproduction</i></sub> = 50 for each successful reproduction.
  - The agent might also receive rewards for behaviors that increase the likelihood of finding a mate, such as moving towards a mating ground or performing a courtship display.
### 3. **Possible Training of the Agent:**

- **Environment Simulation:**
  - Create a simulation environment that includes food sources, predators, potential mates, and environmental hazards. The agent must navigate this environment, deciding when to search for food, avoid predators, or seek out a mate.


### Possible example Outcomes:

- **High Survival, Low Reproduction:** If the agent focuses too much on survival, it might avoid risky situations, like searching for a mate, leading to longer life but fewer offspring.
  
- **High Reproduction, Low Survival:** If the agent prioritizes reproduction, it might take greater risks to find mates, potentially leading to more offspring but shorter life due to exposure to predators or lack of food.

- **Balanced Behavior:** Ideally, the agent finds a balance where it survives long enough to reproduce multiple times, ensuring both its survival and the continuation of its species.

# The Implementation of the Project
Starting point for this project is [resource gathering](https://github.com/doesburg11/SurvivalReproduction/blob/main/MO_Gymnasium/resource_gathering/mpmoq_policy.py), as this is a crucial part of the **survival** objective. Initially, this is a modification of a [morl-baselines](https://github.com/LucasAlegre/morl-baselines) example. This is intially a multi-objective *single* agent environment. It is the intention to extend this to a multi-agent environment in the future.

</br>
<p align="center">
    <img src="https://github.com/doesburg11/SurvivalReproduction/blob/main/assets/myagent1.gif" width="200" height="200"/>
</p>






# References
- [A Practical Guide to Multi-Objective Reinforcement Learning and Planning](https://arxiv.org/abs/2103.09568)
<<<<<<< HEAD
- [An API standard for multi-objective multi-agent reinforcement learning (MOMARL)](https://momaland.farama.org/)
=======
- [An API standard for multi-objective multi-agent reinforcement learning (MOMARL)](https://github.com/Farama-Foundation/momaland)
>>>>>>> 2c6a383b83985aafb851638d44a29a5373b4fea3

