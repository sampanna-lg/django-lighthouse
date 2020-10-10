function validateform(){
    var fname = document.getElementById('fname').value;
    var lname = document.getElementById('lname').value;
    var pass1 = document.getElementById('password').value;
    var pass2 = document.getElementById('pass2').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;
    if(fname == ""){
        document.getElementById('first-name').innerHTML = " * Enter your first name ";
        return false;
    }
    if((fname.length <= 2) || (fname.length > 20)){
        document.getElementById('first-name').innerHTML = " * Enter valid username ";
        return false;
    }
    if(!isNaN(fname)){
        document.getElementById('first-name').innerHTML = " * Enter valid username ";
        return false;
    }
    if(lname == ""){
        document.getElementById('last-name').innerHTML = " * Enter your last name ";
        return false;
    }
    if((lname.length <= 2) || (lname.length > 20)){
        document.getElementById('last-name').innerHTML = " * Enter valid last name ";
        return false;
    }
    if(!isNaN(lname)){
        document.getElementById('last-name').innerHTML = " * Enter valid last name ";
        return false;
    }
    if(pass1 == ""){
        document.getElementById('passwords').innerHTML = " * Enter your password ";
        return false;
    }
    if((pass1.length <= 5) || (pass1.length > 20)){
        document.getElementById('passwords').innerHTML = " * password must be betwwen 5-20 ";
        return false;
    }
    if(pass2 == ""){
        document.getElementById('repass').innerHTML = " *  Re-Enter your password ";
        return false;
    }
    if(pass1!=pass2){
        document.getElementById('repass').innerHTML = " *  password deosnot match ";
        return false;
    }
    if(email == ""){
        document.getElementById('emails').innerHTML = " * Enter your email adress ";
        return false;
    }
    if(phone == ""){
        document.getElementById('ph-num').innerHTML = " * Enter your phone number ";
        return false;
    }
    if(isNaN(phone)){
        document.getElementById('ph-num').innerHTML = " * Enter a valid number ";
        return false;
    }
    if(phone.length!=10){
        document.getElementById('ph-num').innerHTML = " * Enter a valid number. Number must be 10 digit ";
        return false;
    }
};