# Purpose of application

The purpose of this app is to allow registered/login users to post on a blog app that can be used
Desktop through to moblie devices. Users can create posts update posts and delete posts.
Users can also view other users posts as well.Users can update their account information and add thier
own profile image.

Futher more this blog app allows user to blog anywhere at anytime, on any device.

## Features

* Registration form for users to register. (Users must register      to use app)


* Login form where users can use the recently created details.


* Account page where users can update there user info & update      thier profile image. No need to update username or email.


* Users can create posts.


* Users can update thier posts.


* Users can delete thier posts.


* Users can view thier posts and other users posts on post.html.


---


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

* Linux server cloud

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

For the production database i decided to go with PostgreSQL

Flask was decided on for the frameworks light weight in production and ease of use.

At first I started Flask the usual way, a simple structure. Until I started getting errors form the imports. From there I changed the app into a package this resolved any issuses the app had with circular imports. 

As the app got larger I came across a part of stackoverflow where the decussion was about changing a singular pakage into many using blueprints. 

Blueprints allowed me to split the app into many managable readable parts. Doing this will allow the app to expand alot easier in the future.

---

## Unit Testing

### Manual testing

All forms where tested when built, before saving data to the database. When the python logic was add to save the data to the database, I test the forms again and queried the database to known that the user information was implemented correctly.

Once this was done i added the form errors for validation. Then re-tested the forms to see the validation in place. Flash messages where used to inform the user of what is happening.

I created mulitple users to test the app can handle multiple users. And created multiple posts to test that all posts created
by the users where rendered into the post.html template. Then I 
updated the posts to ensure all posts where updated and rendered correctly.

I proceded to delete all users posts. Queried the database through the python terminal to make sure all posts where delete correctly.

Users account profile was tested updating users email and username to make sure the database was updated with new user information. By upating the user profile image, to test that the image saved correctly. And that the output size was changed to what was set in the code, no matter what size of image was uploaded.

By doing this i also made sure the users image name was changed to a set of numbers, set out by random hex. I uploaded a image with the same name cat, to know that no errors accured. This will make sure every image has a unique name.

### Test.py file

The first test i coded where just simple tests to check that flask testing was install correctly test the pages loaded correctly and redirects where followed. See below the tests:

```python

from flask_testing import TestCase
import unittest
from blog import app, db

# This test is to check that all works correctly.

class FlaskTestCase(unittest.TestCase):

    # This test is to check the index page loads correctly.

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Start Posting' in response.data)

    # This test is to check that login page works correctly.

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Login' in response.data)

    # This test is to check that login form works as expected.
    # follows the redirect to account page.

    def test_login_form(self):
        tester = app.test_client(self)
        response = tester.post('/login', 
            data=dict(email="admin", password="admin"),
            follow_redirects=True
        )
        self.assertTrue(b'Login was successful. Happy posting', response.data)    
    
    # This test will test the login form being invalid details.
    
    def test_login_form_invalid(self):
        tester = app.test_client(self)
        response = tester.post('/login', 
            data=dict(email="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertTrue(b'Login unsuccessful. Please check email and password', response.data)

    # Test the logout function works as expected

    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', 
            data=dict(email="admin", password="admin"),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(b'You have been logged out successfuly', response.data)

if __name__ == '__main__':
    unittest.main()

```
### Results
```
-----------------------------------------------------------------
Ran 5 tests in 0.234s

OK

---
```


## Refrences


---

## Extra Notes