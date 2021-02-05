//Accessed the objects that I am going to need to do various things
//related to authentication

const login_form = document.querySelector("#login_form")
const login_nav = document.getElementById("login_nav")
const logout_nav = document.getElementById("logout_nav")
const elements_nav = document.getElementById("elements_nav")
const elements_game_nav = document.getElementById("elements_game_nav")
const newUserBTN = document.querySelector("#newUserBTN")
console.log(newUserBTN)
//Parallel Array Strcutures
users = []

userNames = []
passwords = []

/*
database.ref('/users/').once('value').then((snapshot) => {
			users = snapshot.val()
			///console.log(users)
		
			//This is a for each loop that will loop through a collection
			//the same as C.hasNext()
			//This short hand loop form just automatically goes through all elements in 
			//the collection - it is designed to give me the key for every value as it passeses
			//it
			for (key in users) {
				userNames.push(users[key]["userName"])
				passwords.push(users[key]["password"])

			}		

			console.log(userNames)
			console.log(passwords)
});
*/


database.ref('/users/').on('value',(snapshot) => {
			users = snapshot.val()
			///console.log(users)
		
			//This is a for each loop that will loop through a collection
			//the same as C.hasNext()
			//This short hand loop form just automatically goes through all elements in 
			//the collection - it is designed to give me the key for every value as it passeses
			//it
			for (key in users) {
				userNames.push(users[key]["userName"])
				passwords.push(users[key]["password"])

			}		

			console.log(userNames)
			console.log(passwords)
});


login_form.addEventListener('submit', (e) => {


	e.preventDefault()

	uname = login_form["user_name"].value
	pword = login_form["user_password"].value

	console.log(uname)
	console.log(pword)



	for (key in users) {

		if (users[key]["userName"] == uname) {

			if (users[key]["password"] == pword) {
				logout_nav.style.display = "block"
				elements_nav.style.display = "block"
				elements_game_nav.style.display = "block"
				login_nav.style.display = "none"
				cuser = users[key]
			}
			else {
				alert("Invalid User")
				break;
			}
		}
	}


	const modal = document.querySelector('#login_modal')
	M.Modal.getInstance(modal).close();

});

newUserBTN.addEventListener('click', (e) => {

	newUser()


})
//add an event listener to logout_nav
//In teh function swap the display of the various element
logout_nav.addEventListener('click', (e) => {
	console.log(e)
	logout_nav.style.display = "none"
	elements_nav.style.display = "none"
	elements_game_nav.style.display = "none"
	login_nav.style.display = "block"

});


function newUser() {

  var postData = {
    userName: "user5",
    password: "pass5"
  };

  // Get a key for a new Post.
  var newPostKey = firebase.database().ref().child('users').push().key;

  // Write the new post's data simultaneously in the posts list and the user's post list.
  var updates = {};
  updates['users/' + newPostKey] = postData;

  return firebase.database().ref().update(updates);
}


