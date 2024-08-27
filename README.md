# Multi-Objective Multi-Agent Reinforcement Learning Experiments

## Resource Gathering (MORL)
Starting point for this project is [resource gathering](https://github.com/doesburg11/MOMARL/blob/main/MO_Gymnasium/resource_gathering/mpmoq_policy.py), a modification of a [morl-baselines](https://github.com/LucasAlegre/morl-baselines) example. This is a multi-objective single agent solution.

</br>
<p align="center">
    <img src="https://github.com/doesburg11/MOMARL/blob/main/assets/myagent1.gif" width="200" height="200"/>
</p>

## Item Gathering (MOMARL)

A MOMARL [environment with random policy agents](https://github.com/doesburg11/MOMARL/blob/main/MOMALand/item_gathering/random/random_policy_aec_human.py). 

## Multi-Objective Beach Problem Domain (MO-BPD)

In the Multi-Objective Beach Problem Domain (MO-BPD), each agent represents a tourist starting at a specific beach section, and then deciding at which section of the beach they will spend their day. Agents can choose to move to an adjacent section (move_left or move_right), or to stay_still.
Each beach section is characterised by a certain capacity and each agent is characterised by one of two static types: A or B. These properties, together with the location of the agents on the beach sections, determine the vectorial reward received by agents, having two conflicting objectives: “capacity” and “mixture”. The environment can be configured in two modes, “individual” or “team” reward: the agents can either receive their own individual local rewards, based on the beach section they are located in (i.e., individual reward setting), or the
global reward, based on the sum of rewards over all the available beach sections (i.e., team reward setting).

The Pareto Coverage Set is simulated with the [Independent Q-Learners algorithm](https://github.com/Farama-Foundation/momaland/blob/main/momaland/learning/iql/iql.py):

</br>
<p align="center">
    <img src="https://github.com/doesburg11/MOMARL/blob/main/assets/pareto.png" width="400" height="200"/>
</p>

Furthermore, a MO-BPD solution is also applied with the [Cooperative Discrete MOMAPPO algorithm](https://github.com/doesburg11/MOMARL/blob/main/MOMALand/beach/cooperative_momappo/discrete_momappo.py).

# References

- [MOMAland: A Set of Benchmarks for Multi-Objective Multi-Agent Reinforcement Learning (MOMARL). Florian Felten and Umut Ucak and Hicham Azmani and Gao Peng and Willem Röpke and Hendrik Baier and Patrick Mannion and Diederik M. Roijers and Jordan K. Terry and El-Ghazali Talbi and Grégoire Danoy and Ann Nowé and Roxana Rădulescu](https://momaland.farama.org/)
- [Multi-Objective Multi-Agent Decision Making: A Utility-based Analysis and Survey](https://arxiv.org/abs/1909.02964)
- [A Practical Guide to Multi-Objective Reinforcement Learning and Planning](https://arxiv.org/abs/2103.09568)
- [Pettingzoo: Gym for multi-agent reinforcement learning. 2021-2024. Terry, J and Black, Benjamin and Grammel, Nathaniel and Jayakumar, Mario and Hari, Ananth and Sullivan, Ryan and Santos, Luis S and Dieffendahl, Clemens and Horsch, Caroline and Perez-Vicente, Rodrigo and others](https://pettingzoo.farama.org/)  

