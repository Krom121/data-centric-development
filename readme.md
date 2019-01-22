# Purpose of application

The purpose of this app is to allow registered/login users to post on a blog app that can be used
Desktop through to moblie devices. Users can create posts update posts and delete posts.
Users can also view other users posts as well.Users can update their account information and add thier
own profile image.

Futher more this blog app allows user to blog anywhere at anytime, on any device.



## Tech Used for this app

* Flask 

    * was used for the primary framework.

* Html 5 
    * was used for the structure of the app pages.

* CSS 

    * was used to style the app.

* Bootstrap 

    * was used for grid layout. And componets of the website.

* Sqlite 

    * was used as a development database for testing.

* SQLprocress 

    * was used as a main production database.

* Heruko

    * was used as a production server

---

## From development to production

The app was developed as a need for users to have the ablitiy to post on any device, anywhere.
As there is a need for moblie friendly blog websites.I decided to develop a blog app. Looking
at other blog websites users are bombarded with ads and videos.

The design process was to produce an app that is easy to use and ad free,
Making the users experince alot better. The colors I wanted to use where to be light and not 
overbrearing to the overall desing of the flask app. Colors where to complement the 
typography of the app, to make the app easy to read for the user.

The colors flow through the entire design of the Flask app.

The only changes in colors are the form validations.

The layout is a simple grid layout from boostrap, making the app easy to use and very responsive.
I chosed to make the layout as mordern, clean, with plenty of white space as possiable. Giving the content 
room to breathe, the content will be more readable/understandable for the user.

For a bit of extra securitiy i decided to make the login and register pages have no navbar.
The user would have to register before logging in making the app more secure.
This would help put trust in the user and end up with more users using the app for blogging.

SQLite was the development database for the purpose of testing, ensuring the python logic was correct, allowing for bugfixs.

For the production database i decided to go with sqlprogre

Flask was decided on for the frameworks light weight in production and ease of use.

---

## Unit Testing

### Manual testing

All forms where tested when built, before saving data to the database. When the python logic was add to save the data to the database, I test the forms again and queried the database to known that the user information was implemented correctly.

Once this was done i added the form errors for validation. Then re-tested the forms to see the validation in place. Flash messages where used to inform the user of what is happening.

### Test.py file




---

## Refrences


---

## Extra Notes