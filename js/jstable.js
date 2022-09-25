<!DOCTYPE html>
<html>
<body>

<h2>My First Web Page</h2>

<p>This is my Table built with JavaScript.</p>

<style>
body {
	background-color:powderblue;
}

table, td {
  border:1px solid black;
  border-collapse: collapse;
  padding: 15px;
  background-color: #D6EEEE;
}

th {
  text-align: middle;
  border:1px solid black;
  border-collapse: collapse;
  padding: 15px;
  background-color: #D6EEEE;
  color: #ff6347;
} 

</style>


<table id="t1">
</table>

<script>
function logIt(output) {
    console.log(output);
}

//logIt(msg);

function logItType(output) {
    console.log(typeof output, ";", output);
}


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
    //body += "<td>" + "<a href=row.link>" + row.topic + "</a>" + "</td>";
    // tr to end line
    body += "<tr>";
  }
 
   // Build and HTML fragment of div, table, table body
/*
return (
    "<div style='" + style + "'>" +
      "<table>" +
        body +
      "</table>" +
    "</div>"
  );
*/
console.log("PRINTING BODY!!!");
console.log(body);
console.log("PRINTING BODY DONE!!!");
  return (
        body 
  );

};


document.getElementById("t1").innerHTML = apcompsci._toHtml();
</script>




</body>
</html> 
