function TandaLogin() {
    var url = "https://my.tanda.co/api/oauth/token?";
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var params = "username=" + username + "&password=" + password + "&scope=me&grant_type=password";

    var xhr = new XMLHttpRequest();
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");

    xhr.responseType = "json";
    xhr.send(params);

    xhr.onreadystatechange = function () {
        if(xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var access_token = xhr.response.access_token;
            var xhr2 = new XMLHttpRequest();
            var url2 = "https://my.tanda.co/api/v2/users/me";
            xhr2.open("GET", url2, true);
            xhr2.setRequestHeader("Authorization", "bearer " + access_token);
            xhr2.responseType = "json";
            xhr2.send();

            xhr2.onreadystatechange = function () {
                if(xhr2.readyState === XMLHttpRequest.DONE && xhr2.status === 200) {
                    var tanda_id = xhr2.response.id;
                    window.location = 'facebook.html?id=' + tanda_id;
                }
            };
        }
    };
}