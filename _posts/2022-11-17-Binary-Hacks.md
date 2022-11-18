---
toc: false
layout: post
description: Binary Hacks!!!
categories: [Binary Hacks, week1]
title: Binary Hacks!!!
---
### Hack #1 - Click the below button to randomly generate a binary number.

<button name="button" onclick="getRandomBinary()" style="background-color:green; border-color:blue; color:white">Generate the next random Binary!!!</button>
<br/>

<p id="randomBinary" style="background-color:yellow; color:black">Click the above button to generate random Binary.</p>

<script>
// this function is called upon button click
function getRandomBinary() {
	var time = new Date().getMilliseconds(); //get current time
	var random = time % 10; // get the arrray index value < 10
	document.getElementById("randomBinary").innerHTML = toBinary(random); // replace the text 
}
function toBinary(decimal) {
	while (decimal > 0) {
		if (decimal & 1) {
			binary = "1" + binary;
		} else {
			binary = "0" + binary;
		}
		decimal = decimal >> 1;
	}
	return binary;
}
								  
								  
								  
								  
								  
</script>


