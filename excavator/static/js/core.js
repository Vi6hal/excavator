document.addEventListener('DOMContentLoaded', function()
{
    'use strict';
    var xhr = new XMLHttpRequest()
    xhr.open('POST', 'http://127.0.0.1:8000/welcome',true)
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }));
    xhr.onload = () => {
        if (xhr.status >= 200 && xhr.status < 300) {
            console.log(xhr.responseText);
            window.location.replace("https://www.google.com/"); 
        }
    };
});
