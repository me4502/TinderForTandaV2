/**
 * Facebook login
 */
function send() {
    var username = document.getElementById('username');
    var password = document.getElementById('password');

    var data = {
        "username": username,
        "password": password
    }

    var json = JSON.stringify(data);

    console.log(json);
}