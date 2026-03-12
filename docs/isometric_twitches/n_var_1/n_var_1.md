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

## How to generate these data

+ Follow the instructions for the [FiberSim demo](https://campbell-muscle-lab.github.io/FiberSim/pages/demos/sampling/latin_hypercube/latin_hypercube.html) but ...
+ ... run the command `python FiberPy.py sample "<path_to_this_repo>/simulations/n_vars_1/base/setup.json`

## Example of a single trial

<img src="images/trial_13.png" width="25%" alt="Single trial">

## Pair-plot

This figure shows the distribution of the parameter values. The histogram has a concave profile because the rate constant was sampled in log space and drawn in linear space.

<img src="images/pair_plot.png" width="25%" alt="Pair plot">



## 100 trials superposed

<img src="images/summary.png" width="25%" alt="Single trial">

Note that for some parameter values, the muscle activated at low Ca<sup>2+</sup> so that force rose early in the simulation and did not relax thereafter.

# Data

[Trace values](data_files/summary_n_vars_1_part_1.txt) is a 2500 x 301 tab-delimited text file with columns arranged as follows:

+ Time (s)
+ Ca<sup>2+</sup> conc (M) for simulation 1
+ Half-sarcomere length (nm) for simulation 1
+ Stress (N m<sup>-2</sup>) for simulation 1
+ Ca<sup>2+</sup> conc (M) for simulation 2
+ Half-sarcomere length (nm) for simulation 2
+ Stress (N m<sup>-2</sup>) for simulation 2
+ Ca<sup>2+</sup> conc (M) for simulation 3
+ Half-sarcomere length (nm) for simulation 3
+ Stress (N m<sup>-2</sup>) for simulation 3
+ ...
+ Ca<sup>2+</sup> conc (M) for simulation 100
+ Half-sarcomere length (nm) for simulation 100
+ Stress (N m<sup>-2</sup>) for simulation 100

[Parameter values](data_files/parameter_values.xlsx) is an Excel file where the nth row contains the parameter values for simulation n
