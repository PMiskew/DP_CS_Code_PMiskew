//In this file we deal with anything that has to do with authenticaing someone. 

//CLASS GOAL:
//If you authenticate using option 1 it becomes a challenge loading new pages
//since you cannot pass along the information (easily)

//EXTENSION BASED ON SITUATION:
//If you authenticate using firebase your browser gets "authenticated" this means
//when a page is loaded you run a function that checks to see if the person is valid
//and if they are it updates the page. 
console.log("TEST")

const login_form = document.querySelector("#login-form")
const login_nav = document.getElementById("login_nav")
const logout_nav = document.getElementById("logout_nav")
const the_elements_nav = document.getElementById("the_elements_nav")
const learn_more_nav = document.getElementById("learn_more_nav")

var cUser = null

try {
	
	login_form.addEventListener('submit',(e) => {
		e.preventDefault() //stops page from reloading
		
		email = login_form["user_name"].value
		password = login_form["user_password"].value
		console.log(email)
		console.log(password)

		//Option 1: Verify against a predefined list - for learning

		login_nav.style.display = "none"
		logout_nav.style.display = "block"
		the_elements_nav.style.display = "block"
		learn_more_nav.style.display = "block"


		//Option 2: Send to Firebase for authorization - for real. 
		auth.signInWithEmailAndPassword(email, password).then((userCredential) => {
		
	    	var user = userCredential.user;
	  	

	  		login_nav.style.display = "none"
			logout_nav.style.display = "block"
			the_elements_nav.style.display = "block"
			learn_more_nav.style.display = "block"

	  	
	  	}).catch((error) => {
	    	console.log('ERROR')
	    	var errorCode = error.code;
	    	var errorMessage = error.message;
	  	});

		//General
		const modal = document.querySelector('#login_modal'); 
		M.Modal.getInstance(modal).close();
		login_form.reset()

	});

}
catch(error) {
	console.log("No form")
}


logout_nav.addEventListener('click',(e) => {

	login_nav.style.display = "block"
	logout_nav.style.display = "none"
	the_elements_nav.style.display = "none"
	learn_more_nav.style.display = "none"
	
	firebase.auth().signOut()
	window.open("index.html","_self");

});



//****************************************************
auth.onAuthStateChanged(user => {
	console.log("^^^^^^",user)
	cUser = user

	if (user === null) {

		login_nav.style.display = "block"
		logout_nav.style.display = "none"
		the_elements_nav.style.display = "none"
		learn_more_nav.style.display = "none"
	}
	else {

  		login_nav.style.display = "none"
		logout_nav.style.display = "block"
		the_elements_nav.style.display = "block"
		learn_more_nav.style.display = "block"

	}


});


