

# User Sign In botton

-User can sign in over sign in form.User should put email and password fo get successful sign in

# User Sign Up botton
-User can create registration in two types of role.Mieter and Vermieter
-For both type user first need to put email.When user put email system make two check.Whether the email is already existed `or nor and another is the email is valid or nor.
-If this two condition are successful then system allow user to enable to click next button otherwise user can't click next button.It show error and disable the next button automatically.
-And once user go to the next page user need to put password and confirm password.If this two password are not matched then system show an error in instant time and disable the Submit button.If the user complete the password matching and mark the check box then automatically the submit button get enable.And get successfully ger registered.


# Category thats should be initialise in database before program run
 1. Familienstand
 2. Beziehung
 3. Stadtteil
 4. Wohnungstyp
 5. Type

# Installation of this project!

Follow the steps below:
 
 1. Install python3 and upgrade pip3

 2. Change directory to project folder

 3. Create `virtualenv` for this project, by following command:

		python3 -m venv .venv
		
 4. Activate `.venv` by following command:

		source .venv/Scripts/activate


 5. Install all packages via pip3:
	
		 pip3 install -r requirements.txt

 6. Migrate the changes of Database:
	
		python3 manage.py migrate
		 
 7. Create superuser by following command:

		python3 manage.py createsuperuser

 8. Now run the django project by following command

		python3 manage.py runserver

 9. Open this url: `127.0.0.1:8000`

Now you are good to go.

*Developed by,*
***S R Javed***