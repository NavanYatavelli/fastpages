---
toc: true
layout: post
description: AppLab Notes.
categories: [AppLab, week3]
title: AppLab Notes!!
---
# AppLab Notes

## App#1 - Quiz 

Link to the Quiz Game App
[Quiz Game App](https://studio.code.org/projects/applab/7C7Wx87SDmZ-pGtIjQ5nYRIn2ZEZ8s3MdYTCSud-hMQ)
<a href="https://studio.code.org/projects/applab/7C7Wx87SDmZ-pGtIjQ5nYRIn2ZEZ8s3MdYTCSud-hMQ" title="Quiz Game App">QuizGame-App</a>


Program Purpose: The purpose of the quiz game is knowledge and entertainment. The requirement for this task is to do atlease 3 question quiz. We  narrowed down to ask Countries questions since this would bring more versatile audience interested in playing the game. As suggested this game is a quick and easy fun game for any new players to play.

Functionality: The functionality of the Quiz game is built on navagation of screens as user answers each question. As part of the Design -- we started doing the outline of the quiz rather than going straight to the coding. Functionality of the Quiz Game is listed captured as a flowchart. It is a diagram of the sequence of movements and actions of interactions involved in our game. One screen to next screen functionality is captured below in each box.  

How it works

1)    This quiz is about identifying different countries by the clues provided about the country

2)    Defined and set the variable “score” to 0

3)    Started on homescreen with Instructions “How To” and “Start Quiz” buttons

4)    Selecting “How To” shows Instructions of playing the quiz. From here we can start the quiz or go back to homepage

5)    When “Start the Quiz” button is selected, “The Country”quiz starts with the first question.

6)    The first question is about Brazil. A picture of Brazil is shown with 4 options indicating different countries. Options are provided as Buttons

7)    If the correct country, for this first question Brazil, is selected, Correct Answer screen pops up. This screen provided more fun facts about the country in question 1

8)    When user answers Brazil, score is incremented by 1

9)    Selecting “Next Question” in the screen, takes user to the second question

10) In this second question, a phrase is shown. User has to guess the country to which the phrase belongs and enter the correct answer in the text box provided

11) If he correctly guesses it as “America”, score is incremented, Fun facts about America are provided, and Next question button is presented

12) When user selects this Next question button, Question 3 showing a countries flag is presented with 4 coutnry options to guess

13) If the correct country, for this third question India, is selected, Correct Answer screen pops up and score is again incremented by 1. This screen provided more fun facts about the country in question 3

14) End Quiz button is provided on the third questions fun facts screen, selecting it would take the user to “How did you do?” screen, with a button to get the score is provided

15) Pressing this button shows the score that’s stored in the store variable 

### Design 

![Design of Game]({{site.baseurl}}/images/quiz_design.jpg)


### Successes

* The App Screens are Designed fairly simple and very user-friendly. 
* Any novice user can immediately start play the Quiz game
* The screen to screen colors, text, buttons and text entry are very attractive for users to keep playing
* Score calculation logic was implemented using a variable and shows simple status at the end of the Game. Very easy to follow and understand the Game.


### Discoveries & Challanges

* Discovered how to use OnEvent() fairly quickly 
* I had challanges in getting the user text submission to work 
* Setting up right varibles took some exploration

## App#2 - Piano 
The Piano App is here 
[Piano App](https://studio.code.org/projects/applab/35N9tDBlcOcZeakwvdU2D8WcUEbokAIC_yMBKHTpXTY)

Program Purpose: The purpose of the Piano App is entertainment and learning. The requirement for this task is to do atlease 3 music keys. I narrowed down to simple keys since this would bring more versatile audience interested in playing the music game. As suggested this game is a quick and easy fun game for any new players to play and learn music.

 
### Design Functionality: 

1) This program mimicks a Piano Player with only 7 keys
2) Program starts with a homescreen with a Piano image and Start button
3) Upon selecting the Start button, user is presented with 7 keys, A, B, C, D, E, F
4) When each key is selected, a different sound associated with the key is play


### Successes
* The Music App Screens are Designed fairly simple and very user-friendly. 
* The whole program was written in less than an hour

### Challanges & Discoveries 

* Discovered that the sound played has delay after the key is pressed
* The delay in sound may be due to the file load takes time
* Challanges was to extend the game to more functionality


