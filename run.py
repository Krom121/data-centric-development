from blog import app

"""

This file is now only for running the application
I have turn the app into packaged app to aviod 
circular imports that may cause errors as i build out the app
This file will now run the blog folder file called blog with 
the __init__.py file.

This will also help the package app have readability and 
Scalability

"""

if __name__ == '__main__':
    app.run(debug=True)