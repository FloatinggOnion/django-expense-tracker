const username = document.querySelector('#usernameField');
const feedBackArea = document.querySelector('.invalid_feedback');

username.addEventListener("keyup", (e) => {
    console.log('');

    const usernameVal = e.target.value;
    
    username.classList.remove("is-invalid");
    feedBackArea.style.display = "none";

    if (usernameVal.length > 0) {
        fetch('/auth/validate-username', {
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        }).then(res=>res.json()).then(data=>{
            console.log("data", data);
            if (data.username_error) {
                username.classList.add("is-invalid");
                feedBackArea.style.display = "block";
                feedBackArea.innerHTML=`<p>${data.username_error}</p>`;
            }
        });        
    }

})