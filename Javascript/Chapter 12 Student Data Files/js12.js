"use strict";

/*  JavaScript 7th Edition
    Chapter 12
    Chapter case

    Bonsai Expressions FAQ 
    Author: Tyler Jackson
    Date: 4/28/2024  

    Filename: js12.js
*/
$(() => {
    $("section > h1").css({
        fontSize: 0,
        opacity: 0
    })
    .animate({
        fontSize: "2.3em",
        opacity: 1
    }, 600);
    
    $("#faq")
    .hide()
    .effect("clip", {
        mode: "show",
        direction: "horizontal"
    }, 600);
    
    $("#faq dt").click((e) => {
        let question = $(e.target);
        let answer = $(question.next());
        
        $(question).toggleClass("hiddenAnswer");
        
        if ($(question).hasClass("hiddenAnswer")) {
            $(answer).slideUp(600);
        } else {
            $(answer).slideDown(600);
        }
    });
});
