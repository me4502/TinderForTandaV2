/**
 * Facebook login
 */
function send() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    var data = {
        "username": username,
        "password": password
    };

    var json = JSON.stringify(data);

    console.log(json);
}