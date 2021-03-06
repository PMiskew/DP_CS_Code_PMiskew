//Accessed the objects that I am going to need to do various things
//related to authentication

const login_form = document.querySelector("#login_form")
const login_nav = document.getElementById("login_nav")
const logout_nav = document.getElementById("logout_nav")
const elements_nav = document.getElementById("elements_nav")
const elements_game_nav = document.getElementById("elements_game_nav")

//Parallel Array Strcutures
users = ["user1","user2","user3"]
pwords = ["pword1","pword2","pword3"]
cuser = ""


//Step 1 (not on site) 
//Set up your database with a users collection - in that collection easy approach is to have each
//object have a user and pword key. 

//Step 2 (on load of site)
//Pull from the database the user information and store in an object called userData
//This can be done using the once function.
//
//You can then run alogirhtm when the user clicks login based on the data pull that is because
//the time it takes the user to click login, type in details and hit submit you know the pull is done

//Step 3:
//Your just authenticate based on the list
//

//Step 4 (Create new User):
//
//If you create a new user you then add it to the list in your file. 
//Then you push the entire list back to the database




login_form.addEventListener('submit', (e) => {


	e.preventDefault()

	uname = login_form["user_name"].value
	pword = login_form["user_password"].value

	console.log(uname)
	console.log(pword)


	//Option 1: Verify against a predefined list - for learning
	//Cross check credentials against a list in web page

	//Task: 
	//Write a loop that checks that uname and pword match.  If they match
	//"login" the user by changing the nav bar display. 

	for (i = 0; i < users.length; i = i + 1) {

		if (users[i] == uname) {

			if (pwords[i] == pword) {
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

