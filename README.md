# Tuk Tuk Tours

## Introduction

This project is a full-stack site, Tuk Tuk Tours, that allows a database of registered users 
to manage and/or interact with a common dataset. The database is structured so that certain 
datasets can be managed by super users, other sets by authenticated users and some by any user. 
It can be accessed here: http://tuktuk-tours.herokuapp.com
The site is based around a travel company, who want to sell tours within the Yogyakarta area of Java, 
Indonesia. Super users can manage the database of tours available, as well as create blog posts 
that provide additional information to entice customers when choosing a tour. Any user can view 
and search all the tours and blog posts, while authenticated users have the additional ability 
to purchase a tour, submit reviews of tours and comment on posts. The site owner maintains 
overall admin control over the database. The company adds additional value by providing a 
service to customers that is not currently available in this style, offers local employment 
opportunities for guides and drivers and benefits the communities in which the tours are based. 

## UX

### Project Goals

The primary goal of Tuk Tuk Tours is to provide an e-commerce site for selling tours. 
The secondary goal is to attract additional visitors to the local area, by publishing interesting 
information in the form of blogs going beyond what you can just see and do.

### User Goals

- To find and purchase tours to go on when visiting Yogyakarta
 To find out additional information about the culture and history of the area 

### Developer / Business Goals

- Increase the volume of tourists to the area, by offering a new style of tour
- Make a site that looks professional, that users want to use and come back to and can trust to make secure purchases through
- Consolidate and expand knowledge of multiple programming languages

### User Stories

### Design Choices

**Overall Design** The site has a clear identity, with a consistent and predictable theme and style 
throughout. The rationale behind the style of the site is to represent a notice board that you might 
see in a guest house, with adverts and notices pinned to it. Shadowed cards displaying the tours, posts, 
forms etc. sit on top of a weathered wood background, as if attached to a real board.
The site layout is simple with a navbar at the top right, which collapses to a hamburger menu on 
smaller screen sizes, the site name as a home page link and a standard footer with contact information 
and links to social media pages (not active). All clickable links have clear actions and responses. 
The site is designed over multiple pages and each page's content is clear. It is easy to know where you are, or how to get where you want to be. There are additional helper buttons on pages, such as ‘Back to …’ buttons or quick links for superusers to edit or delete records. 
The elements and features are clear, legible, and disclosed progressively over different pages. 
The features currently offered provide the customer and business owner with what they need, and 
they are simple to implement and use. Future releases can add value in bite-size increments, 
such as displaying tours in a map format.


**Font** The google font, Caveat, was chosen for the site, as it is fun and friendly, and fits 
with the noticeboard style of the site (similar to a handwritten style).

**Colours** The colour scheme for the site is based around three main colours: royal blue, black and white.
 These colours were originally chosen based on the Cambodian flag, as this was the initial business location.
  The colour scheme is modern, simple and clear, and therefore has been retained for the change of business location.
White text stands out on royal blue and black banners for the menu, headers and notification messages 
(with a additional red background or red font on white background for error / warning messages).
 All action buttons are consistently coloured with white text on a blue background (with icons).
  Medium-dark grey text on a white background is used for clarity in the majority of the 
  detailed text in e.g. blog posts, tour information, shopping basket. 

**Card images** The images used on the site were chosen as they visually represent the tours or posts. 
They are all colourful, vibrant images, making the content more attractive to the users. 
They are also indicative of what the customer will see if they choose to buy a tour. 
The home page image has a similar colour palette to the theme of the site giving a coherent style to the front page,
 and additional images have been edited with consistent parameters (e.g. contrast and small vignette)

**Forms** The forms for superusers (creating and editing tours, blog posts and categories), 
the authentication system and user profiles (all users) and reviewing tours or commenting 
on posts (authenticated users) are clear and simple with easy-to-understand labelling. 
They all have a defensive design shown by warning signs, when a field is either not filled in 
correctly (with the correct format shown), or a required field is missing and display a red 
underline that turns green when validated. All action buttons have text and icons to 
make their actions clear. Forms use materialize card styling.

**Icons** Icons are used to enhance the experience of using e.g. the forms. 
They have been chosen for their obvious meaning and add a simple visual pointer, instead of just text. 

**Styling** The Home page uses a card panel to diplay the About Us information 
and several of the “most popular” 
tours are displayed in small cards (currently filtered by sku, but in a future release it would be filtered 
by user generated ratings). 

The tours are displayed as individual image cards with an eye-catching photo, category name, 
and tour name for easy visual filtering, and a snippet of the description. 
Clicking on a tour photo or name takes the user to the detailed tour information page, 
also displayed in a card format. The card has a simple layout, with bold headings, 
with the necessary information (details such as duration, start time etc.). 
There is a clear Leave Review option and existing reviews are displayed in small 
card panels within the main card, with a simple visual guide (emoji) for the rating. 

Blog posts are also all displayed on a single page in image card format, 
with an eye-catching photo, post title, author etc in the header and a snippet of the 
post content with a clear action button for the full post. The post detail is then displayed 
in a large card format with a clean layout and a clear Leave Comment section. 
Comments are displayed underneath the post as individual cards to look like small notes on a notice board.  

Forms have consistent style using the card format. 


## Features

Features include:
### Home app:
- **Home Page / About Us** - The Home page loads an About Us / Yogyakarta section on a card panel 
and several of the “most popular” tours are displayed in small cards (these currently filtered by sku, 
but in a future release it would be filtered by user generated ratings). 

### Tours app:
- **All Tours** - displaying all the tours available in an easy to read and view card format with links to tour details
- **Category Buttons** - users can click a category button to filter the tours displayed
- **Search Bars** - users can search the tours by keywords
- **Sorting Menus** - users can sort the tours by price (ascending / descending)
- **Individual Tour pages** - displaying all the deatiled tour information in an esy to read card format.
Also contains the "Add to Basket" (quantity and date), "Leave Review" and "Blog" apps
- **Individual Tour pages - Reviewing** - authenticated users can submit a review with a rating for a specific tour
(currently graphical, but has a numerical component)
- **Manage Tours** - superusers have access to simple forms to add new tours, edit existing tours and delete tours

### Authentication app:
- **Sign Up / Login / Log Out** - a signing up feature as only registered users can access specific areas or 
functions of the site. Users can easily log out at the end of a session

### Profiles app:
- **Account / Profile** - basic information about the user and a way to store order history and billing details.
- **Manage Categories** - a simple app for superusers to view, create, edit and delete tour categories 

### Blog app:
- **Blog** - a page displaying all posts added to the site with search / sort functions
- **Search Bars** - users can search the blog posts by keywords
- **Sorting Menus** - users can sort the and posts by date (oldest / newest) and title (A-Z / Z-A)
- **Individual Post pages** - to display the full content of individual posts, including comments
- **Individual Post pages - Commmenting** - a form for authenticated users to add comments to individual posts

### Contact Us app:
- **Contact Us** - for users to easily address queries to or ask for additional 
information from the site owner, with a clear input field for an order number if applicable

### Basket app:
- **Add to Basket** - included in the tour detail pages, there is a form consisting of quantity and date 
for users to add tours to their shopping basket
- **View Basket** - a page displaying the details of the contents, and price breakdown, 
of the user's basket in a session

### Checkout app:
- **Checkout form** - a page for users to see a summary of their intended order (inclduing price, discount and grand total) 
and enter billing details (which can be saved to the user profile if the user is authenticated) 
as well as a stripe element for secure card payment
- **Successful checkout** - a form reviewing the order the user has just made, with the details of what
was purchased (quantity, date) and the price, discount and grand total.

Future features:
- **Map of Tours** - tour locations can be displayed on a map
- **Advanced Search** - combining queries such as category and price
- **Social Media Login** - enabling users multiple methods of signing include
- **Delete Confirmation** - so superusers do not delete tours, categories and posts by accident
- **Saving Draft Posts** - new posts are published automatically at the moment, 
but a function to save a draft can be added
- **Moderate Comments** - add a moderator step for editing/deleting comments that breach acceptable standards
- **Moderate Reviews** - add a moderator step for editing/deleting reviews that breach acceptable standards
- **Most Popular/Reviewed Tours / Most Commented Posts** - an additional sorting system to allow users
to directly find the e.g. most popular tours or posts on the site


## Technologies used

- HTML: layout and content 
- CSS: styling
- JavaScript: contact us/email, back to top buttons, quantity decrease/increase buttons
- Python: connecting to Django and performing CRUD operations
- Django: for the database containing tours (and reviews), user profiles, a blog (posts and comments), shopping basket and checkout
- Font Awesome: icons that visually represent the form criteria and info display https://fontawesome.com
- Google Fonts: a back-up font family that represents the style and design of the site https://fonts.google.com
- Materialize (CSS, JavaScript/JQuery) for the functionality of the navbar, hamburger menu, 
forms, basic card and card reveal styling, dropdown menus, date and time pickers
    and the grid structuring of the site https://materialize.com

## Testing 

Additional testing of e.g checkout and basket apps before making this a vaiable e-commerce store. 

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
from Code Institute Django Project

https://github.com/kalwalkden/django-materializecss-form

https://djangocentral.com/creating-comments-system-with-django/

https://fontawesome.com/license

**Acknowledgements**
