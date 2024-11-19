"use strict";
/*    JavaScript 7th Edition
      Chapter 9
      Chapter case
      
      Eating Well in Season 
      Author: Tyler Jackson
      Date: 3/19/2024  
      
      Filename: js09b.js
 */

let qString = location.search.slice(1);

qString = qString.replace(/\+/g, " ");
qString = decodeURIComponent(qString);

let formData = qString.split(/&/g);
for (let items of formData) {
	let fieldValuePair = items.split(/=/);
	let fieldName = fieldValuePair[0];
	let fieldValue = fieldValuePair[1];
	
	let fieldLabel = document.createElement("label");
	fieldLabel.textContent = fieldName;
	document.getElementById("contactInfo").appendChild(fieldLabel);
	
	let inputBox = document.createElement("input");
	inputBox.id = fieldName;
	inputBox.name = fieldName;
	inputBox.value = fieldValue;
	inputBox.disabled = true;
	
	document.getElementById("contactInfo").appendChild(inputBox);
}

document.getElementById("signupBtn").oneclick = function() {
	let formFields = document.querySelectorAll("#contactInfo input, input[type=radio], textarea");
	for (let fields of formFields) {
		localStorage.setItem(fields.name, fields.value);
	}
	console.log(localStorage);
}