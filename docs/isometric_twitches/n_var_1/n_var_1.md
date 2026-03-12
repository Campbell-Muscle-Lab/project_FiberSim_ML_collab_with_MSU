---
layout: default
title: One variable
parent: Isometric twitches
has_children: false
nav_order: 1
---

# Sampling of 1 variable

This dataset consists of n=100 isometric twitches simulated with 1 ms resolution.

Simulations were run with values of the following variables selected based on a Latin hypercube design.


| Variable | Description | Min value (multiple of base) | Max value (multiple of base) | Base value |
| --- | --- | --- | --- | --- |
| m_1_2_2_1 | A myosin rate constant | 10<sup>-0.5</sup> | 10<sup>0.5<sup> | 200 |


In this example, m_1_2_2_1 ranged between 10<sup>-0.5</sup> * 200 = 63 and 10<sup>0.5</sup> * 200 = 632.

## Example of a single trial

<img src="images/trial_13.png" width="25%" alt="Single trial">

## 100 trials superposed

<img src="images/summary.png" width="25%" alt="Single trial">

Note that for some parameter values, the muscle activated at low Ca<sup>2+</sup> so that force rose early in the simulation and did not relax thereafter.

# Data

[Trace values](../../../simulations/summaries/summary_n_vars_1_part_1.txt) is a 2500 x 301 tab-delimited text file with columns arranged as follows:

+ Time (s)
+ Ca<sup>2+</sup> conc (M) for sim 1
+ Half-sarcomere length (nm) for sim 1
+ Stress (N m<sup>-2</sup>) for sim 1
+ Ca<sup>2+</sup> conc (M) for sim 2
+ Half-sarcomere length (nm) for sim 2
+ Stress (N m<sup>-2</sup>) for sim 2
+ Ca<sup>2+</sup> conc (M) for sim 3
+ Half-sarcomere length (nm) for sim 3
+ Stress (N m<sup>-2</sup>) for sim 3
+ ...
+ Ca<sup>2+</sup> conc (M) for sim 100
+ Half-sarcomere length (nm) for sim 100
+ Stress (N m<sup>-2</sup>) for sim 100
