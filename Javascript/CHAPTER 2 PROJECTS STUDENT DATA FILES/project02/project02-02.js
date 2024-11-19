/*    JavaScript 7th Edition
      Chapter 2
      Project 02-02

      Application to test for completed form
      Author: Tyler Jackson
      Date: 4/17/2024 

      Filename: project02-02.js
 */
 
 // Function to verify form submission
function verifyForm() {
    // Get values from input controls
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;

    // Check if all fields are filled out
    if (name && email && phone) {
        // Display thank you message
        window.alert("Thank you!");
    } else {
        // Display error message
        window.alert("Please fill in all fields");
    }
}

// Attach event listener to submit button
document.getElementById("submit").addEventListener("click", verifyForm);
