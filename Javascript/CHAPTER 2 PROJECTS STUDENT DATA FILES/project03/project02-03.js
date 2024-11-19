/*    JavaScript 7th Edition
      Chapter 2
      Project 02-03

      Application to return the shape of a clicked object
      Author: Tyler Jackson
      Date: 4/17/2024   

      Filename: project02-03.js
 */

// Attach onmouseover event handler to element with id "square"
document.getElementById("square").onmouseover = function() {
    document.getElementById("feedback").innerHTML = "You're hovering over the square";
};

// Attach onmouseout event handler to element with id "square"
document.getElementById("square").onmouseout = function() {
    document.getElementById("feedback").innerHTML = "";
};

// Attach onmouseover event handler to element with id "triangle"
document.getElementById("triangle").onmouseover = function() {
    document.getElementById("feedback").innerHTML = "You're hovering over the triangle";
};

// Attach onmouseout event handler to element with id "triangle"
document.getElementById("triangle").onmouseout = function() {
    document.getElementById("feedback").innerHTML = "";
};

// Attach onmouseover event handler to element with id "circle"
document.getElementById("circle").onmouseover = function() {
    document.getElementById("feedback").innerHTML = "You're hovering over the circle";
};

// Attach onmouseout event handler to element with id "circle"
document.getElementById("circle").onmouseout = function() {
    document.getElementById("feedback").innerHTML = "";
};
