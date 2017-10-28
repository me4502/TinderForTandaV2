/**
 * Tanda login
 */
function TandaLogin() {

var url = "https://my.tanda.co/api/oauth/token";
var username = document.getElementById("login").value;
var password = document.getElementById("password").value;
var params = "username=" + username + "&password=" + password + "&scope=me&grant_type=password";

console.log(username, password, params);
var xhr = new XMLHttpRequest();
xhr.open("POST", url, true);
xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

xhr.send(params);

}