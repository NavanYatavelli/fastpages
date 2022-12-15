---
toc: false
layout: post
description: Unit 3 Section 16 Hacks
categories: [Unit 3 Section 16 Hacks]
title: Unit 3 Section 16 Hacks
---

### Answer Table

| Question    | Answer |
| ----------- | ----------- |
| Name(First+Last)      | Navan Yatavelli       |
| 1   | NA        |
| 2   | NA        |
| 3   | (C) To make the simulation more accurate        |
| 4   | (C) Imperfections on aircraft        |
| 5   | (C) Situation considered        |
| 6   | (A) simulation        |
| 7   | (A) simulation       |
| 8   | NA        |
| 9   | (B) experiment/calculation |


#### Explanation 
- (3) The reason not to use a pseudo-random number generator when making a simulation is to make the simulation more accurate
- (4) The least likely factor to be removed from a flight(air traffic) simulation for functionality is due to imperfections on aircraft
- (5)  The difference between a experiment and a simulation is situation considered
- (6)  A car company needs to know how safe it's customers will be if it's new car crashes uses Simulation because it's too dangerous to have this be an experiment
- (7)  A environmental group wants an accurate guess on the impact the greenhouse effect will have on the environment would like to do simulation. Also, we don't want to experiment with this because it could cause great harm on the environment 
- (9)  A teacher want's to find the average score from a final using expirement because there is no need to simulate anything, this will only be a simple calculation of the average       

#### Reflection (Vocab )
A simulation is an simpler abstraction of an very complicated natural phenomena.  Simulations help for people to learn more and predict important data which they can use to better improve algorithms and products. Simulations are often much cheaper and have no safety limits compared to real life experiments. I found these problems to be a little challenging, but a good review of simulations. Simulations are needed for modeling complicated situations in a much simpler way so that any user can still manage most aspects of the model without delving into complexities.

### Extra Simulation
```
import random

print("=====================================================")
print("Simulation of the gender of the newly born -- Pandas!")
print("=====================================================")

births = 1000 #  sample size
male_pandas = 0
female_pandas = 0
 
for i in range(births):
    gender = random.randint(0,1) # get a random number between 0 and 1
    if gender == 1: # head
        male_pandas = male_pandas + 1
    else:         # tail
        female_pandas = female_pandas + 1
 
print('Number of newly born pandas are male:', male_pandas, " and their percentage is ", (100*male_pandas/births), "%" )
print('Number of newly born pandas are female:', female_pandas, " and their percentage is ", (100*female_pandas/births), "%" )
```

Output

```
================================================
Simulation of the gender of newly born -- Pandas!
================================================
Number of newly born pandas are male: 493  and their percentage is  49.3 %
Number of newly born pandas are female: 507  and their percentage is  50.7 %
```
Here is a simulation of a pandas birth, which accurately simulates how many male or female pandas would be born if there were 1000 births. Using a simulation is much more efficient, better and replicates the real world situation. The simulation here also caluclates the percentage of male vs female born. In both cases the percentage is closer to 50%.
