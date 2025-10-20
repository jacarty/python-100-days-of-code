Sign up to a hosting provider and create your web service
Create an account with a hosting provider

There are many different hosting providers to choose from when it comes to making your app go live on the internet. Features and pricing vary between them and their pricing plans can change. It's up to you who you want to choose. For this tutorial, I will show you how to host on render.com


Provider                   ~Cost / Month           Name of Plan

Heroku                                $5                      Eco & Basic

render                                  $0                      Individual

Cyclic                                   $0                      Free Forever

Glitch                                   $0                      Starter

Vercel                                  $0                       Hobby

PythonAnywhere              $0                       Beginner 


The nice thing about most of these providers is that they can easily deploy your app straight from a GitHub repo. We've done most of the difficult bits already. There are just a few steps left:

1. Create an account with the hosting provider

2. Link our GitHub repo with the host

3. Set up a PostgreSQL database with the host

4. Store the key-value pairs for our environment variables with our host


Create an account e.g., on render.com


Heroku discontinued their free plan, but other providers are still offering one. You can create an account on render.com simply by signing up via Github.


Click "authorize" and confirm your email address. Job done.
Create a new Web Service


Choose your blog app that you've uploaded to GitHub and connect your repo
Edit the Start Command

Most of render.com's defaults are fine. All you need to do is pick a name for your project and then change the Start Command to:

gunicorn main:app



Add your first environment variable

Before you create your web service, click "Advanced" and add your environment variable your Flask app.

Scroll to the bottom and create your web service.

Your web app won't work yet, however. We first need to set up our database and set the environment variable for SQLAlchemy. 