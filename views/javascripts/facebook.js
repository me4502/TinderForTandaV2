/**
 * Facebook login
 */
function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function send() {
    //var usercode = getParameterByName('id');
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    var data = {
        //"usercode": usercode,
        "username": username,
        "password": password
    };

    var json = JSON.stringify(data);

    console.log(json);
}