/* regex for username validation 


[a-zA-Z0-9_]{5,} to match at least five alphanumerics and the underscore
[a-zA-Z]+ to have at least one letter
[0-9]* to match zero to any occurrence of the given numbers range

*/

/* regex for password validation

Min 1 uppercase letter.
Min 1 lowercase letter.
Min 1 special character.
Min 1 number.
Min 8 characters.
Max 30 characters.

*/

/* regex for email validation


*/

function validate(){
var username=document.getElementById("username").value
var email=document.getElementById("email").value
var password=document.getElementById("password").value
var username_re= /^[a-zA-Z0-9_]{5,}[a-zA-Z]+[0-9]*$/
var email_re= /^[a-zA-Z0-9_-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$/
var password_re= /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$@!%&*?])[A-Za-z\d#$@!%&*?]{8,30}$/

if(username.match(username_re)){
    if(email.match(email_re)){
        if(password.match(password_re))
        return true
        else{
            alert("Invalid Password")
            return false
        }
    }
    else{
        alert("Invalid Email Address")
        return false
    }
}
else{
    alert("Invalid Username")
    return false
}
}

function change(){
   var password=document.getElementById('email')
   if(email.type == "password")
   email.type='text'
   else
   email.type='password'
}