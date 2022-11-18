---
toc: false
layout: post
description: Binary Hacks!!!
categories: [Binary Hacks, week1]
title: Binary Hacks!!!
---
### Hack #1 - Click the below button to randomly generate a binary number.

<button name="button" onclick="getRandomBinary()" style="background-color:green; border-color:blue; color:white">Generate the next random number!!!</button>
<br/>

<p id="randomBinary" style="background-color:yellow; color:black">Binary.</p>
<p id="randomDecimal" style="background-color:red; color:black">Decimal.</p>
<p id="randomOctal" style="background-color:green; color:black">Octal.</p>
<p id="randomHex" style="background-color:orange; color:black">Hex.</p>

<script>
// this function is called upon button click
function getRandomBinary() {
	var time = new Date().getMilliseconds(); //get current time
	var random = time % 100; // get the value < 100

    document.getElementById("randomBinary").innerHTML = "Binary: " + random.toString(2); 
    document.getElementById("randomDecimal").innerHTML = "Decimal: " + random.toString(10); 
    document.getElementById("randomOctal").innerHTML = "Octal: " + random.toString(8); 
    document.getElementById("randomHex").innerHTML = "Hexadecimal: " + random.toString(16);
}
</script>


