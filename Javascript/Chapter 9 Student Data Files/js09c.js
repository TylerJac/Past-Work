"use strict";
/*    JavaScript 7th Edition
      Chapter 9
      Chapter case
      
      Eating Well in Season Retrieving Data from Local Storage
      Author: Tyler Jackson
      Date: 3/19/2024  
      
      Filename: js09c.js
 */

let keys = ["name", "email", "phone", "address", "city", "state", "zip", "allergies", "frequency", "size"];
for (let item of keys) {
	let newRow = document.createElement("tr");
	
	let keyCell = document.createElement("td");
	keyCell.textContent = item;
	newRow.appendChild(keyCell);
	
	let keyValue = document.createElement("td");
	ketValue.textContent = localStorage.getItem(item);
	newRow.appendChild(keyValue);
	
	document.getElementById("prefTable").appendChild(newRow);
}

document.getElementById("removePrefBtn").onclick = function() {
	for (let item of keys) {
		localStorage.removeItem(item);
	}
}