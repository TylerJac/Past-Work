/*    JavaScript 7th Edition
      Chapter 2
      Project 02-01

      Celsius <-> Farenheit Coverter
      Author: Tyler Jackson
      Date: 4/17/2024  

      Filename: project02-01.js
 */

function FahrenheitToCelsius(degree) {
    return (degree - 32) / 1.8;
}

// Function to convert Celsius to Fahrenheit
function CelsiusToFahrenheit(degree) {
    return degree * 1.8 + 32;
}

// Attach onchange event handler to element with id "cValue"
document.getElementById("cValue").onchange = function() {
    var cDegree = parseFloat(document.getElementById("cValue").value);
    document.getElementById("fValue").value = CelsiusToFahrenheit(cDegree);
};

// Attach onchange event handler to element with id "fValue"
document.getElementById("fValue").onchange = function() {
    var fDegree = parseFloat(document.getElementById("fValue").value);
    document.getElementById("cValue").value = FahrenheitToCelsius(fDegree);
};