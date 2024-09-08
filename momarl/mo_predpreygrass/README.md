


[![Python 3.11.9](https://img.shields.io/badge/python-3.11.7-blue.svg)](https://www.python.org/downloads/release/python-3117/)
[![PettingZoo version dependency](https://img.shields.io/badge/PettingZoo-v1.24.3-blue)]()
[![API test](https://img.shields.io/badge/API_test-passed-brightgreen)]()
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Wiki](https://img.shields.io/badge/Wiki-background-green)]()
</br>
<p align="center">
    <img src="https://github.com/doesburg11/PredPreyGrass/blob/main/assets/images/readme/predpreygrass.png" width="700" height="80"/> 
</p>
</br>

## The environment
A multi-objective multi-agent reinforcement learning (MARL) environment. An extension of the [PredPreyGrass](https://github.com/doesburg11/PredPreyGrass) environment. The envrionment has two objectives: 

maximize the cumulative reproduction reward of Predators
maximize the cumulative reproduction reward of Prey 


Learning agents Predators (red) and Prey (blue) both expend energy moving around, and replenish it by eating. Prey eat Grass (green), and Predators eat Prey if they end up on the same grid cell. In the base case for simplicity, the agents obtain 100% of the energy from the eaten Prey or Grass. However, in the 'real world' this is much less because the [ecological efficiency](https://en.wikipedia.org/wiki/Ecological_efficiency) is only around 10% in most cases. Predators die of starvation when their energy is zero, Prey die either of starvation or when being eaten by a Predator. The agents asexually reproduce when energy levels of learning agents rise above a certain treshold by eating. When reproducing, learning eagents recieve a reproduction reward.

## Installation

**Editor used:** Visual Studio Code 1.93.0 on Linux Mint 21.3 Cinnamon

Broadly similar to the [PredPreyGras](https://github.com/doesburg11/PredPreyGrass?tab=readme-ov-file#installation) environment
    
## Getting started

### Visualize a random policy

Broadly similar to the [PredPreyGras](https://github.com/doesburg11/PredPreyGrass?tab=readme-ov-file#visualize-a-random-policy) environment

# References

- [MOMAland: A Set of Benchmarks for Multi-Objective Multi-Agent Reinforcement Learning (MOMARL). Florian Felten and Umut Ucak and Hicham Azmani and Gao Peng and Willem Röpke and Hendrik Baier and Patrick Mannion and Diederik M. Roijers and Jordan K. Terry and El-Ghazali Talbi and Grégoire Danoy and Ann Nowé and Roxana Rădulescu](https://momaland.farama.org/)
- [Multi-Objective Multi-Agent Decision Making: A Utility-based Analysis and Survey](https://arxiv.org/abs/1909.02964)
- [A Practical Guide to Multi-Objective Reinforcement Learning and Planning](https://arxiv.org/abs/2103.09568)
- [Pettingzoo: Gym for multi-agent reinforcement learning. 2021-2024. Terry, J and Black, Benjamin and Grammel, Nathaniel and Jayakumar, Mario and Hari, Ananth and Sullivan, Ryan and Santos, Luis S and Dieffendahl, Clemens and Horsch, Caroline and Perez-Vicente, Rodrigo and others](https://pettingzoo.farama.org/)  
- [Multi-Agent Reinforcement Learning: Foundations and Modern Approaches. Stefano V. Albrecht, Filippos Christianos, and Lukas Schäfer](https://www.marl-book.com/download/marl-book.pdf)
