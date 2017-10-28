/**
 * Facebook login
 */
FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
});