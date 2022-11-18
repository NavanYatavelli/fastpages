---
toc: false
layout: post
description: Binary Hacks!!!
categories: [Binary Hacks, week1]
title: Binary Hacks!!!
---
### Hack #1 - Click the below button to randomly generate a number and convert to Binary, Hex, Decimal and Octal.

<button name="button" onclick="getRandomBinaryHack1()" style="background-color:green; border-color:blue; color:white">Generate the next random number to convert!!!</button>
<br/>

<p id="randomBinary" style="background-color:yellow; color:black">Binary.</p>
<p id="randomDecimal" style="background-color:red; color:black">Decimal.</p>
<p id="randomOctal" style="background-color:green; color:black">Octal.</p>
<p id="randomHex" style="background-color:orange; color:black">Hex.</p>
<br/><br/><br/><br/>
### Hack #2 - Click the below button to randomly generate a number and convert to hex, decimal to set color.
<button name="button" onclick="getRandomBinaryHack2()" style="background-color:green; border-color:blue; color:white">Generate the next random number to change color!!!</button>
<br/>
<p id="colorBox" style="background-color:purple; color:black">The Color changes</p>
<p id="colorBoxHex"></p>


<script>
// this function is called upon button click
function getRandomBinaryHack1() {
	var time = new Date().getMilliseconds(); //get current time
	var random = time % 100; // get the value < 100
	var val = random;					       

    document.getElementById("randomBinary").innerHTML = "Binary: " + random.toString(2); 
    document.getElementById("randomDecimal").innerHTML = "Decimal: " + random.toString(10); 
    document.getElementById("randomOctal").innerHTML = "Octal: " + random.toString(8); 
    document.getElementById("randomHex").innerHTML = "Hexadecimal: 0x" + random.toString(16);
	
}
						       
// this function is called upon button click
function getRandomBinaryHack2() {
	var time = new Date().getMilliseconds(); //get current time
	var val = time % 100; // get the value < 100
	var hex = val.toString(16);
	
	// Set color					     
    document.getElementById("colorBox").style.backgroundColor = `rgb(${val}, ${val}, ${val})`;
    document.getElementById("colorBox").innerHTML = "Color Code: rgb(" + val + "," + val + "," + val + ")";
    document.getElementById("colorBoxHex").innerHTML = "Hex#" + hex + hex + hex;
}
						       
						       
</script>


