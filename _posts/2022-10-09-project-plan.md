---
toc: true
layout: post
categories: [markdown, plan, week7]
comments: true
title: Project Plan
---

# Project Plan 

The project that our team decided to create initially was a website that allowed users to post inspirational quotes and like their friends’ posts. However, we wanted to incorporate a random quotes API into our project and decided to change it. The design we came up with after hours of tireless work is shown below.

# Design 

Our group decided to use Google Drawings to mock up what our website will look like. We have decided to use Bootstrap in order to design the components. The adjusted plan includes random quotes that people can like rather than posting their own.

# UI Design 

![]({{ site.baseurl }}/images/quotes.png)

In this picture as you, the design shows inspiration quotes from prevalent speakers such as DJ Khaled and Martin Luther King Jr. This satisfies the Collegeboard criteria as follows:

# Program Purpose & Function

- A website to display random inspirational quotes
- Users can create accounts and save quotes by liking them
- Allow users to share there goals and find new quotes

# Data Abstraction

We will store user data
- Number of likes
- Number of comments
- Comments messages
- Quotes
- Data will be stored in a SQLite relational database 
- Data will be accessed using the sqlite3 library, a Python interface for SQLite

# Procedural Abstraction

- We will implement separate functions and HTML templates for different views
- Quote API abstraction using a function to access the RapidAPI 

# Algorithm Implementation 
The software development will employ Linux Ubuntu OS, VS Code, HTML, JavaScript, Python and Github will be used to host the code. 
Following are some of the DB fields
- User ID
- Follower ID
- Likes 
- Messages
- Quotes

# Testing
The Striver website will emply manual testing. After code is developed unit testing will be done by the developeer and integration testing will be done in phases. We'll use of print statements to debug API issues. 

# Release
There will be multiple releases os the product and one final releases. We make a build everyday for team members to test. 

# Roles
Here are the Roles for our Project 

Safin: Scrum Leader
Alex: Back- end
Kalani: Front End
Navan: Dev ops
