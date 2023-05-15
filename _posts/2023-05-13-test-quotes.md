---
toc: false
layout: post
description: Test Quotes
title:Test Quotes!!!
---

#### Test JS
This Java Script fetches from a third party API, and display json data. This also uses the json data in JavaScript function as an object and prints the value. 

<br/><br/><br/><br/>


### Click the below button for JavaScript to fetch 3rd party API JSON data.

<button name="button" onclick="fetchStocks()" style="background-color:green; border-color:blue; color:white">Fetch Stocks!!!</button>
<br/>

<p id="tips" style="background-color:yellow; color:black">Click the above button to random facts in JSON format.</p>

<script>
async function fetchStocks() {
	
  const settings = {
	async: true,
	crossDomain: true,
	url: 'https://andruxnet-random-famous-quotes.p.rapidapi.com/?cat=famous&count=10',
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '61c6a629f7msh3c7c0f786cc7e20p158b5bjsnea9db1f03bc5',
		'X-RapidAPI-Host': 'andruxnet-random-famous-quotes.p.rapidapi.com'
	}
};

$.ajax(settings).done(function (response) {
	console.log(response);
  document.getElementById('tips').innerHTML = result;
});
  
}

</script>
