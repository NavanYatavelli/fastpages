---
toc: false
layout: post
description: Unit 3 Sections 12-13 Hacks
categories: [Unit 3 Sections 12-13 Hacks]
title: Unit 3 Sections 12-13 Hacks
---

### 3.12 Homework Part 1
Problem 1: This problem involves parameters

Qais is writing code to calculate formulas from his math class. He's currently working on a procedure to calculate average speed, based on this formula:

Average speed=

Total Time/Total Distance

Highlight which of these is the best procedure for calculating and displaying average speed.
<mark>PROCEDURE calcAvgSpeed (distance, time) { DISPLAY (distance/time) }</mark>
PROCEDURE calcAvgSpeed (distance) { DISPLAY (distance/time) }
PROCEDURE calcAvgSpeed (distance, time) { DISPLAY (time/distance) }


### Question 1 HACK

```
isCold = True
isRaining = True
stayInside = False

if ((isCold) or (isRaining)) :
    stayInside = True
else:
    stayInside = False

print("It is cold=" + str(isCold) + " and raining=" + str(isRaining) + " so stayInside=" + str(stayInside))
```


### Question 2 HACK
```
import random

def player_turn():
    greatest_number = 0
    for i in range(4):
        new_number = random.randint(1, 10)
        if new_number > greatest_number:
            greatest_number = new_number
    print(greatest_number)

player_turn()
player_turn()
```
## Question 3 HACK

```
{
if MOVE_FORWARD_ALLOWED{
    moveForwards
}
else{
    if TURN_RIGHT_ALLOWED{
        turnright
    }
    if TURN_LEFT_ALLOWED{
        turnleft
    }
}
}
```

## Question 4 & 5

<img src="{{site.baseurl}}/images/hack5q4.jpg" alt="Beebadger Blog Header">

Explanation: We would start our search for element 69 by looking at the middle index, 5 first (8 elements divide by 2, plus 1 index). We find 6. 6 being less than 69 would lead you to consider the greater than half. The middle index for this section is Seven (5+9 = 14/2 = 7). Index number seven is 11, which is lower than index number 69. The eighth index is next examined ((8+8)/2 = 8). We searched and discovered the right number because 8 = 69.

### Question 6 Diagram

<img src="{{site.baseurl}}/images/hack5q6.jpg" alt="Beebadger Blog Header">

### Question 7

Shown as below in alphabetical order, ascending, place these in this order. As numbers are greater, you can compare which numerical value of these ascii characters is greater, allowing these to be correctly compared.

```
["Market”, ”Ralphs”, “store”, "Target”, ”Walmart”]
```

### Question 8 HACK
The binary search automatically rules out half of the options with each iteration, it is much faster than sequential search. Since you begin at the middle index, you can either select the group that is higher or lower than the middle index. As a result, each time you divide, you will eliminate half of the potential outcomes.

### Question 9 HACK
From the list [64,36,16,11,9], we  should be looking for number 36. First, I would choose the middle element ((1+5)/2 = 3), and since 16 is less than 36, I would shift back (as the list is reversed). As a result, I would choose the second element (1+3/2 = 2), which equals 36, therefore it would take me just two tries to reach 36.
