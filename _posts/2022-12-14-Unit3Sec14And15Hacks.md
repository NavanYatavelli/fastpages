---
toc: false
layout: post
description: Unit 3 Sections 14-15 Hacks
categories: [Unit 3 Sections 14-15 Hacks]
title: Unit 3 Sections 14-15 Hacks
---

### Unit 3 Sections 14-15 Homework
#### Reflection
Documentation is important for others or for yourself to understand your code later on. This lesson emphasized ways that which code can be efficiently and effectively written through use of libraries, documentation, and APIs. Libraries consist of pre-written code that can be utilizing in other programs. They help to simplify code by storing code segments and features in a separate place, this way, the code being run only has code that the user has written. A library's documentation describes the different features of a library.  Libraries are collections of code and scripts that can provide faster solvents to problems. 


#### Problem 2: Multiple Choice

##### (1) What does the random(a,b) function generate?
- A. A random integer from a to be exclusive
- <mark>B. A random integer from a to b inclusive.</mark>
- C. A random word from variable a to variable b exclusive.
- D. A random word from variable a to variable b inclusive.

##### (2) What is x, y, and z in random.randrange(x, y, z)?

- <mark> A. x = start, y = stop, z = step</mark>
- B. x = start, y = step, z = stop
- C. x = stop, y = start, z = step
- D. x = step, y = start, z = stop

##### (3) Which of the following is NOT part of the random library?

-  <mark> A. random.item </mark>
- B. random.random
- C. random.shuffle
- D. random.randint

#### Problem 3:  Short Answer Questions

##### (1) What is the advantage of using libraries?
Libraries have a distinct advantage of having pre-written code that can provide efficiency at a linear level. Libraries help to simplify complex programs by allowing the code to reference pre-written code. This reduces the workload for the user writing the code and improves reliability. This cuts out time that the user has to write repetitive code. The user can spend more time on the creative and work process then repetitive code writing.

##### (2) Write a thorough documentation of the following code.
```
import random 

# Saves user input in the in the comma seperated format
names_string = input("Give me everybody's names, seperated by a comma.")

# splits the stored user input by the character, comma, and stores each element in the list names
names = names_string.split(",")

# get the length of names
num_items = len(names)

# get random number within < num_items
random_choice = random.randint(0, num_items - 1)

# figuring out randomly who to play
person_who_will_pay = names[random_choice]

# Prints the name random person name with message
print(f"{person_who_will_pay} is going to buy the meal today!")
```
Output
```
 Brady is going to buy the meal today!
``` 

#### Problem 4:  Coding Challenges!

##### (1) Create a program to pick five random names from a list of at least 15 names
```
import random

# list of random names
random_names = ["Aaron Rodgers","Rob Gronkowski", "Patrick Mahomes", "Odell Beckham ", "Ben Roethlisberger", "Russell Wilson", "Cam Newton", "Lamar Jackson", "Antonio Brown", "JJ Watt", "Adrian Peterson", "Keira", "Deshaun Watson", "	Lionel Messi", "Jerry Rice"] 

i = 0
# printing 5 random names
print("The five random names are:")
while i < 5:
    print(random.choice(random_names))
    i += 1
```
Output

```
Lamar Jackson
Ben Roethlisberger
Russell Wilson
Adrian Peterson
Deshaun Watson
```
