---
toc: false
layout: post
description: Post that uses HTML fragments and JavaScript data  to build a table.
categories: [Java Script, week5]
title: Post that uses HTML fragments and JavaScript data!!
---
### This Post uses HTML fragments and JavaScript data to build a table.
### Below table is built with Java Script data and HTML fragments

### AP Computer Science Principles -- Assignments Data
<table id="t1">
</table>

<script>
// define a function to hold data for a Assignment
function Assignment(week, topic, description, link) {
    this.week = "Week#" + week;
    this.topic = topic;
    this.description = description;
    this.link = link;
}

// define a Assignment Array 
var assignments = [ 
    new Assignment(0,"Tools and Equipment", 
    "Tool Setup Sprint and Pair Programming", 		"https://github.com/NavanYatavelli/fastpages/issues/2"),
    new Assignment(1,"Introduction to Python", 
    "Fastpages Frontend Development & Bash Tutorial", 		"https://github.com/NavanYatavelli/fastpages/issues/3"),
    new Assignment(2,"Data Abstraction in Python", 
    "HTML Fragments", 		
    "https://github.com/NavanYatavelli/fastpages/issues/4"),
    new Assignment(3,"Creative Development Sprint", 
    "Program Design with App Lab by Code.org", 		"https://github.com/NavanYatavelli/fastpages/issues/5"),
    new Assignment(4,"Python Web Server Project", 
    "Flask/Python Web Application & Fastpages local server", 		"https://github.com/NavanYatavelli/fastpages/issues/6"),
    new Assignment(5,"UI Starters", 
    "JavaScript Tutorial", 	"https://github.com/NavanYatavelli/fastpages/issues/7"),

];

// define a course and build Course objects
function Course(name, assignments){ 
    this.name = name; // name of the course
    this.assignments = assignments; //assignments for this course
}

// make a Computer Science Course - with name and assignements
apcompsci = new Course("AP Computer Science Principles", assignments);

// define an HTML conversion "method" associated with Course
Course.prototype._toHtml = function() {
  // HTML Style is build using inline structure
  var style = (
    "display:inline-block;" +
    "border: 2px solid grey;" +
    "box-shadow: 0.8em 0.4em 0.4em grey;"
  );

  // HTML Body of Table is build as a series of concatenations (+=)
  var body = "";
  
  // Heading for Array Columns
  body += "<tr>";
  body += "<th><mark>" + "Week" + "</mark></th>";
  body += "<th><mark>" + "Topic" + "</mark></th>";
  body += "<th><mark>" + "Description" + "</mark></th>";
  body += "<th><mark>" + "HW Link" + "</mark></th>";
  body += "</tr>";
  // Data of Array, iterate through each row of compsci.classroom 
  for (var row of apcompsci.assignments) {
    // tr for each row, a new line
    body += "<tr>";
    // td for each column of data
    body += "<td>" + row.week + "</td>";
    body += "<td>" + row.topic + "</td>";
    body += "<td>" + row.description + "</td>";
    body += "<td>" + "<a href=\"" + row.link + "\">" + row.topic + "</a>" + "</td>";
    body += "<tr>";
  }
 
   // Build and HTML fragment of  body
  return (
        body 
  );

};

// Fill teh body of the table using the Java Script data
document.getElementById("t1").innerHTML = apcompsci._toHtml();
</script>

### Here is the Java Script code explanation

#### This Java Script snippet defines HW Assignment function to hold assignment data 
```
// define a function to hold data for a Assignment
function Assignment(week, topic, description, link) {
    this.week = "Week#" + week;
    this.topic = topic;
    this.description = description;
    this.link = link;
}
```
#### HW Assignment array initilization used to populate the table
```
// define a Assignment Array 
var assignments = [ 
    new Assignment(0,"Tools and Equipment", 
    "Tool Setup Sprint and Pair Programming", 		"https://github.com/NavanYatavelli/fastpages/issues/2"),
    new Assignment(1,"Introduction to Python", 
    "Fastpages Frontend Development & Bash Tutorial", 		"https://github.com/NavanYatavelli/fastpages/issues/3"),
    new Assignment(2,"Data Abstraction in Python", 
    "HTML Fragments", 		
    "https://github.com/NavanYatavelli/fastpages/issues/4"),
    new Assignment(3,"Creative Development Sprint", 
    "Program Design with App Lab by Code.org", 		"https://github.com/NavanYatavelli/fastpages/issues/5"),
    new Assignment(4,"Python Web Server Project", 
    "Flask/Python Web Application & Fastpages local server", 		"https://github.com/NavanYatavelli/fastpages/issues/6"),
    new Assignment(5,"UI Starters", 
    "JavaScript Tutorial", 	"https://github.com/NavanYatavelli/fastpages/issues/7"),

];
```

#### Below defines the Course function and also constructs its instance 
```
// define a course and build Course objects
function Course(name, assignments){ 
    this.name = name; // name of the course
    this.assignments = assignments; //assignments for this course
}

// make a Computer Science Course - with name and assignements
apcompsci = new Course("AP Computer Science Principles", assignments);
```

#### This snippet builds the HTML table body using fragments and Java Script 
```
// define an HTML conversion "method" associated with Course
Course.prototype._toHtml = function() {
  // HTML Style is build using inline structure
  var style = (
    "display:inline-block;" +
    "border: 2px solid grey;" +
    "box-shadow: 0.8em 0.4em 0.4em grey;"
  );

  // HTML Body of Table is build as a series of concatenations (+=)
  var body = "";
  
  // Heading for Array Columns
  body += "<tr>";
  body += "<th><mark>" + "Week" + "</mark></th>";
  body += "<th><mark>" + "Topic" + "</mark></th>";
  body += "<th><mark>" + "Description" + "</mark></th>";
  body += "<th><mark>" + "HW Link" + "</mark></th>";
  body += "</tr>";
  // Data of Array, iterate through each row of compsci.classroom 
  for (var row of apcompsci.assignments) {
    // tr for each row, a new line
    body += "<tr>";
    // td for each column of data
    body += "<td>" + row.week + "</td>";
    body += "<td>" + row.topic + "</td>";
    body += "<td>" + row.description + "</td>";
    body += "<td>" + "<a href=\"" + row.link + "\">" + row.topic + "</a>" + "</td>";
    body += "<tr>";
  }
 
   // Build and HTML fragment of  body
  return (
        body 
  );
```

