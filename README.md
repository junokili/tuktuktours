# Tuk Tuk Tours

## Introduction

## UX

### Project Goals

### User Goals

### Developer / Business Goals

### User Stories

### Design Choices

**Overall Design**

**Font**

**Colours**

**Card images**

**Forms**

**Icons**

**Styling** 

## Features

Features include:
- **Home Page / About Us** - 
- **All Tours** - 
- **Tours by Category** - 
- **Search Bar** - so users can search the tours by keywords
- **Sorting** - users can sort the tours by price (ascending / descending) and rating (ascending / descending)
- **Sign Up / Login / Log Out** - a signing up feature as only registered users can access specific areas or 
functions of the site. Users can easily log out at the end of a session
- **My Profile** - basic information about the user and a way to store order history and billing details.
- **My Order History** - users can see what the have previously purchased
- **Review Tour** - users can submit a review with a rating for a tour
- **Manage Tours** - superusers have access to simple forms to add new tours, edit existing tours and delete tours
- **Contact Us Form** - a basic form for users to easily ask queries to for additional 
information from the site owner
- **Manage Categories** - a simple page for the site owner to view, create, edit and delete tour categories 
- **Blog** - users can read and comment on blogs about culture, history etc 
- **Toasts** - 

Future features:
- **Map of Events** - tour locations can be displayed on a map
- **Advanced Search** - combining queries such as category and price
- **Social Media Login** - enabling users multiple methods of signing include
- **Delete Confirmation** - so superusers do not delete tours and categories by accident
- **Saving Draft Posts** - new posts are published automatically at the moment, 
but a function to save a draft can be added
- **Moderate Comments** - add a moderator step for editing/deleting comments that breach acceptable standards
- **Moderate Reviews** - add a moderator step for editing/deleting reviews that breach acceptable standards

Additional testing of e.g checkout and basket apps before making this a vaiable e-commerce store. 

## Technologies used

- HTML: layout and content 
- CSS: styling
- JavaScript: google maps API, contact us/email, back to top buttons, quantity decrease/increase buttons
- Python: connecting to Django and performing CRUD operations
- Django: for the database with events, locations, users, and categories
- Font Awesome: icons that visually represent the form criteria and info display https://fontawesome.com
- Google Fonts: a back-up font family that represents the style and design of the site https://fonts.google.com
- Materialize (CSS, JavaScript/JQuery) for the functionality of the navbar, hamburger menu, 
forms, basic card and card reveal styling, dropdown menus, date and time pickers
    and the grid structuring of the site https://materialize.com

## Testing 

- **Links**

- **Sending emails**

- **Responsiveness**

- **Language Validation**

- **Testing of app functions**

- **Testing of User Stories**

## Deployment

This project was developed using Gitpod and deployed through Heroku. 
It can be accessed here: http://tuk-tuk-tours.herokuapp.com/

The steps taken to set up the project and to deploy it to Heroku were as follows:
1. Create a git repository
2. Create a .gitnore file and add non-publishable files e.g. pycache, env.py, pyc etc
5. Add the new files to the staging area in the terminal (git add)
6. Commit the files to the repository with an appropriate message (git commit -m "message")
7. Push the files to the repository (git push)
8. Login to Heroku (https://heroku.com, or sign up) and create a new app, following the prompts to name 
the project and select a region
9. Within the app go to the Resources tab and find Heroku Postgres in the Add-ons and choose a plan
10. In github install dj_database_package (terminal command - pip3 install dj_database_url)
11. And install psycopg2 (terminal command - pip3 install psycopg2-binary)
12. Update requirements.txt file (terminal command - pip3 freeze > requirements.txt)
13. Add dj_database_url to settings.py and add the link to the Heroku database (from Heroku > Settings > Reveal Config Vars)
14. Rerun all migrations and create a superuser
15. Set up an if statement in settings.py to connect to either the Heroku database or the original django one
16. Install gunicorn (terminal command - pip3 install gunicorn)
17. Update requirements.txt file (terminal command - pip3 freeze > requirements.txt)
4. Create a Procfile file in github (in file - web: gunicorn tuktuk_tours.wsgi:application)
19. Login to Heroku in the CLI (heroku login -i)
20. Add heroku app to ALLOWED_HOSTS in settings.py
21. Temporarily disable collecting static files (heroku config:set DISABLE_COLLECTSTATIC=1 --app tuktuk-tours)
21. set git remote to heroku in CLI (heroku git:remote -a tuktuk-tours)
22. Push to Heroku (git push heroku master) and open app to check it has been successfully deployed
8. Within the app in heroku go to the Deploy tab
9. Select Deployment method: GitHub - Connect to GitHub
10. Check your username, enter the repository name, click Search. 
11. When the repository has been found, click Connect and Enable Automatic Deployment
11. Get a django secret key and add it to Heroku Settings > Config Vars
11. Add the secret key variable to settings.py
12. Set up AWS account to host static files ....
13. In Github pip3 install boto3, and pip3 install django_storages
14. Update requirements.txt file (terminal command - pip3 freeze > requirements.txt)
25. Add storages to installed apps in settings.py




12. Go to the Settings tab and click Reveal Config vars
13. Enter the Key-Value pairs for the Config Vars (IP (0.0.0.0), PORT (5000), SECRET_KEY (hidden variable),
 MONGO_URI (from MongoDB) and MONGO_DBNAME (from MongoDB))

To run the app locally in GitHub:
1. Login to GitHub 
2. Navigate to the project repository (https://github.com/junokili/tuktuktours)
3. Click on the Gitpod button and a new, local workspace will be created within Gitpod

## Credits

**Content**

**Media**
Tuktuk icon:
<div>Icons made by <a href="http://www.creaticca.com/" title="Creaticca Creative Agency">Creaticca Creative Agency</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

JS for increment / decrement buttons, 
Toasts
from Code Institute Django Project

https://github.com/kalwalkden/django-materializecss-form

https://djangocentral.com/creating-comments-system-with-django/

https://fontawesome.com/license

**Acknowledgements**
