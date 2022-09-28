---
toc: false
layout: post
description: JavaScript Tips Generator!!!
categories: [Java Script, week5]
title: JavaScript Tips Generator!!!
---
### Click the below button to generate JavaScript Tips.

<button name="button" onclick="getJavascriptTips() style="background-color:green; border-color:blue; color:white">Generate next JavaScript Tip!!!</button>
<br/>

<p id="tips" style="background-color:yellow;"></p>

<script>
// Array of 10 tips
var tipsArray = [
"JavaScript took just 10 days to develop.",
"JavaScript was probably named after Java.",
"GitHub says JavaScript is the Most Popular language in the world.",
"JavaScript is responsible for Web2.",
"JavaScript has many implementations.",
"JavaScript was initially created as a browser-only language.",
"JavaScript is the Programming Language Of The Web.",
"JavaScript is single threaded. ",
"Along with HTML an CSS, JavaScript is one of the three main things of the www (World Wide Web).",
"In JavaScript semi colon can be used at the beginning of a statement.",
];

// this function is called upon button click
function getJavascriptTips() {
	var time = new Date().getMilliseconds(); //get current time
	var arrayIndex = time % 10; // get the arrray index value < 10
	document.getElementById("tips").innerHTML = tipsArray[arrayIndex]; // replace the tip 
}
</script>


<br/><br/><br/><br/>
#### Here is the Java Script code explanation

```
// Array of 10 tips
var tipsArray = [
"JavaScript took just 10 days to develop.",
"JavaScript was probably named after Java.",
"GitHub says JavaScript is the Most Popular language in the world.",
"JavaScript is responsible for Web2.",
"JavaScript has many implementations.",
"JavaScript was initially created as a browser-only language.",
"JavaScript is the Programming Language Of The Web.",
"JavaScript is single threaded. ",
"Along with HTML an CSS, JavaScript is one of the three main things of the www (World Wide Web).",
"In JavaScript semi colon can be used at the beginning of a statement.",
];
								       
// this function is called upon button click
function getJavascriptTips() {
	var time = new Date().getMilliseconds(); //get current time
	var arrayIndex = time % 10; // get the arrray index value < 10
	document.getElementById("tips").innerHTML = tipsArray[arrayIndex]; // replace the tip 
}
```
