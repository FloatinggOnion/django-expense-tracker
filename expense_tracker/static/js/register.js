const username = document.querySelector('#usernameField');
const feedBackArea = document.querySelector('.invalid_feedback');
const email = document.querySelector('#emailField');
const emailFeedBackArea = document.querySelector('.emailFeedBackArea');
const usernameSuccessOutput = document.querySelector('.usernameSuccessOutput');
const emailSuccessOutput = document.querySelector('.emailSuccessOutput');
const showPassword = document.querySelector('.showPassword');
const password = document.querySelector('#passwordField');

const handleToggleInput = (e) => {

    if(showPassword.textContent==='Show'){
        showPassword.textContent = 'Hide';
        password.setAttribute("type", "text");
    }else{
        showPassword.textContent = 'Show';
        password.setAttribute("type", "password");
    }

};



username.addEventListener("keyup", (e) => {
    console.log('');

    const usernameVal = e.target.value;
    usernameSuccessOutput.style.display = 'block';
    usernameSuccessOutput.textContent = `Checking ${usernameVal}...`;
    
    username.classList.remove("is-invalid");
    feedBackArea.style.display = "none";

    if (usernameVal.length > 0) {
        fetch('/auth/validate-username', {
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data", data);
            usernameSuccessOutput.style.display = 'none';
            if (data.username_error) {
                username.classList.add("is-invalid");
                feedBackArea.style.display = "block";
                feedBackArea.innerHTML=`<p>${data.username_error}</p>`;
            }
        });        
    }

})



email.addEventListener("keyup", (e) => {
    console.log('');

    const emailVal = e.target.value;

    emailSuccessOutput.style.display = 'block';
    emailSuccessOutput.textContent = `Checking ${emailVal}...`;
    
    email.classList.remove("is-invalid");
    emailFeedBackArea.style.display = "none";

    if (emailVal.length > 0) {
        fetch('/auth/validate-email', {
            body: JSON.stringify({email: emailVal}),
            method: "POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data", data);
            emailSuccessOutput.style.display = 'none';
            if (data.email_error) {
                email.classList.add("is-invalid");
                emailFeedBackArea.style.display = "block";
                emailFeedBackArea.innerHTML=`<p>${data.email_error}</p>`;
            }
        });        
    }

})



showPassword.addEventListener("click", handleToggleInput);