//Accessed the objects that I am going to need to do various things
//related to authentication

const login_form = document.querySelector("#login_form")
const login_nav = document.getElementById("login_nav")
const logout_nav = document.getElementById("logout_nav")
const elements_nav = document.getElementById("elements_nav")
const elements_game_nav = document.getElementById("elements_game_nav")

//Parallel Array Strcutures
users = []

database.ref('/usersInfo/').once('value').then((snapshot) => {
			users = snapshot.val()
			console.log(users)
			
});



login_form.addEventListener('submit', (e) => {


	e.preventDefault()

	uname = login_form["user_name"].value
	pword = login_form["user_password"].value

	console.log(uname)
	console.log(pword)



	for (i = 0; i < users.length; i = i + 1) {

		if (users[i]["userName"] == uname) {

			if (users[i]["password"] == pword) {
				logout_nav.style.display = "block"
				elements_nav.style.display = "block"
				elements_game_nav.style.display = "block"
				login_nav.style.display = "none"
				cuser = users[i]
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
    userName: "new user",
    password: "password"
  };

  // Get a key for a new Post.
  var newPostKey = firebase.database().ref().child('usersInfo').push().key;

  // Write the new post's data simultaneously in the posts list and the user's post list.
  var updates = {};
  updates['usersInfo/' + newPostKey] = postData;

  return firebase.database().ref().update(updates);
}

newUser()

