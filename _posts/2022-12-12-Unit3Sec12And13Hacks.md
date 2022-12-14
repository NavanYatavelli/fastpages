---
toc: false
layout: post
description: Unit 3 Sections 12-13 Hacks
categories: [Unit 3 Sections 12-13 Hacks]
title: Unit 3 Sections 12-13 Hacks
---

### 3.12 Homework Part 1
#### Problem 1: This problem involves parameters

Qais is writing code to calculate formulas from his math class. He's currently working on a procedure to calculate average speed, based on this formula:

Average speed=
Total Time/Total Distance

Highlight which of these is the best procedure for calculating and displaying average speed.
- <mark>PROCEDURE calcAvgSpeed (distance, time) { DISPLAY (distance/time) }</mark>
- PROCEDURE calcAvgSpeed (distance) { DISPLAY (distance/time) }
- PROCEDURE calcAvgSpeed (distance, time) { DISPLAY (time/distance) }


#### Problem 2: Procedures with return values

James Hunter is looking through his classmate's program and sees a procedure called heightenEmotions: PROCEDURE heightenEmotions(myEmotion)

{ moreEnergy ← CONCAT(myEmotion, "!!!")

moreVolume ← UPPER(moreEnergy)

RETURN moreVolume }

That procedure manipulates strings using two built-in procedures, CONCAT for concatenating two strings together, and UPPER for converting a string to uppercase.

James Hunter then sees this line of code:

heightenEmotions("im mad")

After that line of code runs, will nothing be displayed?

- <mark>True</mark>
- False

#### Problem 3: Procedures with return values

Bubz is writing a program to calculate the carbon footprint of his activities. The procedure calcFlightFootprint calculates the pounds of carbon dioxide produced per passenger in a flight that covers a given number of miles and seats a given number of passengers.

```
PROCEDURE calcFlightFootprint(numMiles, numPassengers) { CO2_PER_MILE ← 53.29

carbonPerFlight ← numMiles * CO2_PER_MILE

carbonPerPassenger ← carbonPerFlight / numPassengers

RETURN carbonPerPassenger

}
```

Bubz wants to use that procedure to calculate the total footprint for his two upcoming flights: LA to NY: 2,451 miles and 118 passengers NY to London: 3,442 miles and 252 passengers

Which of these code snippets successfully calculates and stores her total footprint? Highlight 2 answers.

- <mark>totalFootprint ← calcFlightFootprint(2451, 118) + calcFlightFootprint(3442, 252)</mark>
- totalFootprint ← calcFlightFootprint(2451, 118 + 3442, 252)
- <mark>totalFootprint ← calcFlightFootprint((2451, 118) + (3442, 252))</mark>
- laNyCarbon ← calcFlightFootprint(2451, 118) nyLondonCarbon ← calcFlightFootprint(3442, 252) 
- totalFootprint ← laNyCarbon + nyLondonCarbon


### 3.12 Homework Part 2
#### (1)
```
PROCEDURE find a ()
{ 
c <-- 9
b <-- 9 * 9
a <-- b * c
Print (a)
}
```
What is a?
```
c = 9
b = 9 * 9 = 81
a = b c = 81 9 = 729
```
<mark>a=729</mark>

#### (2)
```
cost <-- 173 tax - 10%
PROCEDURE applytax (cost, cpercentDiscounted) { 
temp <-- 100 + percentTaxed
temp <-- temp / 100
cost <-- cost x temp
Print(cost)}
```
What is the cost?

```
temp = 110
110/100 = 1.1
173 * 1.1 = $190.30
```
<mark>$190.30</mark>
#### (3)
```
Tempature - 103 Degrees
PROCEDURE convet Fahrenheit (tempature)
{
Celsius <-- tempature - 32
Celsius <-- Celsius x 5/9
Print (Celsius)}
103 - 32 = 71
71 x (5/9) = 39.44 degrees Celsius
}
```
<mark>39.44 degrees Celsius</mark>

### 3.13 Hacks
#### (1)
Create a procedure that is meant to replace the top running backs yards per game in one season if the current running back has more yards per game
Necessary Parameters: toprbyardspg(100), currentrbyards(1260), totalGames(12)

```
def replaceRrunningBackYards(toprbyardspg, currentrbyards, totalGames):
    if ((toprbyardspg/totalGames) < (currentrbyards/totalGames)):
        toprbyardspg = currentrbyards
    print(toprbyardspg)
replaceRrunningBackYards(100, 1260, 12)
```

<mark>1260</mark>

#### (2)
Write a procedure that will allow the A+ to get to the 1, while avoiding the black boxes.

```
PROCEDURE APlus(){
If (canMoveForward):
Move_Forward
Else (canMoveRight):
Rotate_Right
Move_Forward
If (canMoveLeft);
Rotate_Left
Move_forward
}
```
#### (3)
Which Is the Correct Way to define the Name of a Procedure?
- A. PROCEDURE MYLIST
- B. <mark>PROCEDURE MyList</mark>
- C. procedure mylist
Since the procedure should be in all capital and part of the procedure name should be capitalized

#### (4)
Write A Procedure That gets the BeachBall To the Green Square
```
PROCEDURE toGreenSquare {
Rotate_Left
    move_forward
    move_forward
    move_forward
    move_forward
    move_forward
    move_forward
    rotate_left
    rotate_left
    rotate_left
}
```






