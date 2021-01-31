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

### **Strategy**

**Project Goals**

The primary goal of Tuk Tuk Tours is to provide an B2C e-commerce site for selling tours. 
The goal is achieved by providing a site that is fun and compelling, with a unique design that stands out.
There are a limited number of button clicks between viewing products and purchase
The secondary goal is to attract additional visitors to the local area, by publishing interesting 
information in the form of blogs going beyond what you can just see and do.

**User Goals**

To find and purchase tours to go on when visiting Yogyakarta. 
This goal is acheived by making the site look credible and trustworthy, with easy actions for the user to get what they want with a 
minimum of button clicks. 
To find out additional information about the culture and history of the area 
This goal is acheived by the addition of a blog app, which is related to the tours. 

**Developer / Business Goals**

- Increase the volume of tourists to the area, by offering a new style of tour
- Make a site that looks professional, that users want to use and come back to and can trust to make secure purchases through
- Consolidate and expand knowledge of multiple programming languages

**User Stories**

User stories can be found in a seperate document here:

### **Scope**

The existing features provide the users with what they currently need. The business owner can add new tours to 
their site, update existing ones and view customer orders.
Customers can easily view the information they need to make a purchase and go through the minimum number
 of steps to complete a purchase. 
 Future releases will add value to the site, by increasing the management capability for the owner, 
 and range of information and search functions for the user. 

### **Structure**

The site has a consistent theme and style with the site name as a home page link and a menu at the top right. 
All clickable links have clear actions and responses. The site is designed over multiple pages 
and the key information for each pages’ content is clear. It is easy to know where you are, 
and how to get where you want to be with e.g. Back to All Tours, Back to All Posts and a back to top button on certain longer pages.
Buttons change colour on hover, making it clear that they are action links.

The information architecture allows users to easily move through the content, with related content 
displayed together tied to the users' needs. 

### **Skeleton**

Information is revealed across a small number of pages, with the key elements in the navbars and 
linked to from the home page in several places. The limited number of pages keeps the site simple 
and easy to navigate to find the information the user needs, leading the user to continue the experience. 
Choices are simple so the user is not overwhelmed with options, and each click provides 
immediate value with specific content.
Familiar icons and names with consistent colours and text are used for ease of navigation. All apps and 
functions are designed in a similar way giving easy useability. 

### **Surface**

- **Overall Design** The site has a clear identity, with a consistent and predictable theme and style 
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

- **Font** The google font, Caveat, was chosen for the site, as it is fun and friendly, and fits 
with the noticeboard style of the site (similar to a handwritten style). The font is used in all aspects 
of the site, including forms, as this remains on brand with the playful nature of a travel site 
(the stripe card element is the one place a more simple font style is used). 

- **Colours** The colour scheme for the site is based around three main colours: royal blue, black and white.
 These colours were originally chosen based on the Cambodian flag, as this was the initial business location.
  The colour scheme is modern, simple and clear, and therefore has been retained for the change of business location.
White text stands out on royal blue and black banners for the menu, headers and notification messages 
(with a additional red background or red font on white background for error / warning messages).
 All action buttons are consistently coloured with white text on a blue background (with icons).
  Medium-dark grey text on a white background is used for clarity in the majority of the 
  detailed text in e.g. blog posts, tour information, shopping basket. 

- **Images** The images used on the site were chosen as they visually represent the tours or posts. 
They are all colourful, vibrant images, making the content more attractive to the users. 
They are also indicative of what the customer will see if they choose to buy a tour. 
The home page image has a similar colour palette to the theme of the site giving a coherent style to the front page,
 and additional images have been edited with consistent parameters (e.g. contrast and small vignette)

- **Forms** The forms for superusers (creating and editing tours, blog posts and categories), 
the authentication system and user profiles (all users) and reviewing tours or commenting 
on posts (authenticated users) are clear and simple with easy-to-understand labelling. 
They all have a defensive design shown by warning signs, when a field is either not filled in 
correctly (with the correct format shown), or a required field is missing and display a red 
underline that turns green when validated. All action buttons have text and icons to 
make their actions clear. Forms use materialize card styling.

- **Icons** Icons are used to enhance the experience of using e.g. the forms. 
They have been chosen for their obvious meaning and add a simple visual pointer, instead of just text. 

- **Styling** The Home page uses a card panel to diplay the About Us information 
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

### Authentication app:
- **Sign Up / Login / Log Out** - a signing up feature as only registered users can access specific areas or 
functions of the site. Users can easily log out at the end of a session

### Profiles app:
- **Account / Profile** - basic information about the user and a way to store order history and billing details.

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
- **Manage Categories** - superusers have access to simple forms to view, create, edit and delete tour categories 

### Blog app:
- **Blog** - a page displaying all posts added to the site with search / sort functions
- **Search Bars** - users can search the blog posts by keywords
- **Sorting Menus** - users can sort the and posts by date (oldest / newest) and title (A-Z / Z-A)
- **Individual Post pages** - to display the full content of individual posts, including comments
- **Individual Post pages - Commmenting** - a form for authenticated users to add comments to individual posts
- **Manage Posts** - superusers have access to simple forms to view, create, edit and delete blog posts 
- **Driver/guide app** - superusers can add information about the drivers and guides to show a more
personal service to the customers. 

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
was purchased (quantity, date) and the price, discount and grand total. Superusers can access order details 
in the admin and in stripe. 


Future features:
- **Map of Tours** - tour locations can be displayed on a map
- **Advanced Search** - combining queries such as category and price
- **Social Media Login** - enabling users multiple methods of signing including e.g. faccebook, twitter, instagram etv
- **Delete Confirmation** - so superusers do not delete tours, categories and posts by accident
- **Saving Draft Posts** - new posts are published automatically at the moment, 
but a function to save a draft can be added, and has been already created in the model
- **Moderate Comments** - add a moderator step for editing/deleting comments that breach acceptable standards
- **Moderate Reviews** - add a moderator step for editing/deleting reviews that breach acceptable standards
- **Most Popular/Reviewed Tours / Most Commented Posts** - an additional sorting system to allow users
to directly find the e.g. most popular tours or posts on the site


## Technologies used

- HTML: layout and content 
- CSS: styling
- JavaScript: contact us/email, back to top buttons, quantity decrease/increase buttons
- Python: connecting to Django and performing CRUD operations
- Django: for the database containing tours (and reviews), user profiles, a blog (posts and comments), 
shopping basket and checkout
- Font Awesome: icons that visually represent the form criteria and info display https://fontawesome.com
- Google Fonts: a back-up font family that represents the style and design of the site https://fonts.google.com
- Materialize (CSS, JavaScript/JQuery) for the functionality of the navbar, hamburger menu, 
forms, basic card and card reveal styling, dropdown menus, date and time pickers
    and the grid structuring of the site https://materialize.com


## Testing 

- **Links**
All internal and external links have been tested. The links to external sites (e.g. facebook, instagram) 
display a "coming soon" image as the social media for the site has not yet been created. 
Internal links, such as button clicks, menu links, back-to-top buttons have all been tested to check 
that they perform as expected.

- **Responsiveness**
During the development process the responsiveness of the site was checked through 
chrome developer tools for main device formats. The grid structuring uses responsive 
parameters for display effectiveness in e.g. displaying parallel event cards (4 on large screens, 
3 on medium screens and 1 on small screens), font sizes, image sizes, stacking some divs vertically
on small screens and horizontally on larger screens (e.g. individual post and tour pages) and 
for the navbar collapsing below medium screen widths. 
The site has also been tested successfully on different browsers e.g. Chrome, Firefox, Edge.

- **Language Validation**
    - The HTML was validated through W3C HTML Validation Service (https://validator.w3.org/nu/). 
A significant number of errors are thrown up, however these are due to the templating language.
Some additional errors were noted e.g.
The validator sees an h1 element in the checkout page is blank, 
but this element actually only contains an icon with the loading spinner
The validator also threw upstray tag errors for the table in the basket, but all of these are paired. 
It could not process the html beyond {% for tour in basket_not_empty %} so I had to validate this page in two chunks
Also the includes e.g. navbars throw up errors, due to not having body elements.
Any other errors that were encountered were fixed. 

    - The CSS was validated with no reported errors through 
W3C CSS Validation Service (https://jigsaw.w3.org/css-validator/).

    - The JavaScript files were validated through JSHint (https://jshint.com/) with the only errors being the 
use of functionality only with ES6 (for which a comment was added) and apparent unused functions, 
however these are all invoked within other functions or button clicks, likewise the apparent 
undefined variables are all defined and utilised.

    - The Python code was validated through PEP8 Online (http://pep8online.com/) 
with the only errors being a handful of "line too long" errors in e.g. calculations.
 
- **Testing of app functions**

All functions of apps have been tested manually. Some basic automated tests have been added, such
as getting the correct page response and form validation, but due to time constraints these are limited.
All forms display the correct validation parameters, with a warning for how to correctly enter the data, 
or if data is missing (e.g. "Please fill out this field."). 
Form labels also add extra information to assist the user. 

Testing of apps can be found in a seperate document here:


- **Testing of User Stories**

Testing of User Stories can be found in a seperate document here:


- **Additional Comments**

During the build the postgres database was accidentally exposed when intially deployment, so 
the first heroku app was deleted and a new app, with a new database was created. 
Further testing of e.g checkout and basket apps would ne required before making this a vaiable e-commerce store. 


## Deployment

This project was developed using Gitpod and deployed through Heroku. 
It can be accessed here: http://tuk-tuk-tours.herokuapp.com/

Set up the project and deploy it to Heroku:
1. Create a git repository
2. Create a .gitnore file and add non-publishable files e.g. pycache, env.py, pyc etc
3. Add the new files to the staging area in the terminal (CLI - git add)
4. Commit the files to the repository with an appropriate message (CLI - git commit -m "message")
5. Push the files to the repository (CLI - git push)
6. Login to Heroku (https://heroku.com, or sign up) and create a new app, following the prompts to name 
the project and select a region
7. Within the app go to the Resources tab and find Heroku Postgres in the Add-ons and choose a plan
8. In github install dj_database_package (CLI - pip3 install dj_database_url)
9. In github install psycopg2 (CLI - pip3 install psycopg2-binary)
10. Update requirements.txt file (CLI - pip3 freeze > requirements.txt)
11. Add dj_database_url to settings.py and add the link to the Heroku database 
(from Heroku > Settings > Reveal Config Vars) - do not push to git while the postgres database is exposed
12. Rerun all migrations and create a superuser 
13. Set up an if statement in settings.py to connect to either the remote Heroku database 
or the local sql database (to allow local deployment / development mode)
14. Install gunicorn (terminal command - pip3 install gunicorn)
15. Update requirements.txt file (CLI - pip3 freeze > requirements.txt)
16. Create a Procfile file in github (in file - web: gunicorn tuktuk_tours.wsgi:application)
17. Login to Heroku in the CLI (heroku login -i)
18. Add heroku app to ALLOWED_HOSTS in settings.py
19. Temporarily disable collecting static files (CLI - heroku config:set DISABLE_COLLECTSTATIC=1 --app tuktuk-tours)
20. Set git remote to heroku in CLI (heroku git:remote -a tuktuk-tours)
21. Push to Heroku (CLI - git push heroku master) and open app to check it has been successfully deployed
22. Within the app in Heroku go to the Deploy tab
23. Select Deployment method: GitHub - Connect to GitHub
24. Check your username, enter the repository name, click Search. 
25. When the repository has been found, click Connect and Enable Automatic Deployment
26. Get a django secret key (via the internet browser) and add it to Heroku Settings > Config Vars
27. Add the secret key variable to settings.py (do not expose the secret key)
28. App should be successfully deployed (without static files). Open app in Heroku

Set up an Amazon Web Services Account to host static files:
1. Create an AWS account (www.aws.amazon.com) or login to your existing account
2. In the Management Console go to S3
3. Click on Buckets and create a new bucket withan appropriate name, region, and unblock all public access
4. In Properties > Enable Static web hosting with default conditions
5. In Permissions > CORS config set the CORS configuration (see Learn More for what to add)
6. In Bucket Policy > Policy Generator, create an S3 Bucket Policy with (effect: allow, principal: *,
actions: get object, arn: from the Bucket Policy info provided by AWS) > Add Statement > Generate Policy
7. Copy Policy into Bucket Policy input, remembering to add /* at the end of the resources key
8. In Access Control > Check Everyone has List Permissions
9. In Management Console > IAM > Groups > Add New Group (give it a name, ig nore subsequent tabs for now)
10. In Policies > Create Policy > JSON > Import Management Policy > Amazon S3 Full Access > Import
11. In the policy change the resources to "["arn: ...", "arn: .... /*"] > Review Policy (add a name and description) > Create Policy
12. In Group > Permissions > Attach Policy (find it by name)
13. In Users > Add New User > give a name and allow programmable access > Add to Group > Create User
14. Download and safely store csv file with key information
15. Add AWS keys to Heroku > Settings> Config Vars
16. In github install boto3 (CLI - pip3 install boto3)
17. In github install django-storages (CLI - pip3 install django-storages)
18. Update requirements.txt file (CLI - pip3 freeze > requirements.txt)
19. Add 'storages' to INSTALLED APPS in settings.py, and add AWS Bucket Name, region and key variables, 
add AWS custom domain
20. Create a custom_storages.py file at the project level to hold classes for media and static storage locations
21. Add storage and static / media file locations and urls to settings.py
22. Add AWS Object Parameters for the cacheing of files to settings.py
23. Push to Heroku and check the AWS bucket now has the static files
24. In AWS > S3 > Bucket > Create Folder named media
25. Upload required media files, grant Public read access in Additional Settings
26. App should be successfully deployed with static files. Open app in Heroku

Set up Stripe for payments:
1. Create a Stripe account, or login (www.stripe.com)
2. Go to Stripe > Dashboard and find user keys
3. Add Stripe public and secret keys to Heroku > Settings > Congfig Vars (do not expose keys)
4. Add a new webhook for the heroku app (https://tuktuk-tours.herokuapp.com/checkout/wh/)
5. Select Recieve all Evens and Add Endpoint
6. Copy the webhook signing secret and add to Heroku > Settings > Config Vars
7. Test the webhook
8. App should be successfully deployed for demo stripe payments. Oppen app in Heroku

To run the app locally in GitHub:
1. Login to GitHub 
2. Navigate to the project repository (https://github.com/junokili/tuktuktours)
3. Click on the Gitpod button and a new, local workspace will be created within Gitpod
4. Install required dependencies (CLI - pip3 install django, pip3 install django-allauth)
5. create a superuser (CLI - python3 manage.py createsuperuser)
6. Install additional required dependencies (using CLI pip3 install) for django-countries, pillow, stripe,
materializecss, gunicorn, boto3, psycopg2-binary, django-storages
7. Create requirements.txt file (CLI - pip3 freeze > requirements.txt)
8. Run site (CLI - python3 manage.py runserver)


## Credits

**Content**
All content is the developer's own, unless otherwise accredited. 
Resources used, but modified have come from:
Code Institutue (DJango walkthrough project) e.g. javascript used for increment / decrement buttons, 
sort selector, python for basket tools and context, 
https://github.com/kalwalkden/django-materializecss-form
https://djangocentral.com/creating-comments-system-with-django/
https://gist.github.com/tommorris/cd1048418cccfa346fef

**Media**
All images are the developers own except:
Tuktuk icon from Creaticca Creative Agency (http://www.creaticca.com) 
Coming Soon image from Vectorstock 
https://www.vectorstock.com/royalty-free-vector/coming-soon-neon-sign-coming-soon-badge-in-vector-21133321

**Acknowledgements**
Thanks to my mentor, Sebastian Immel, for giving insight into how the project looked and 
adding additional value to how the project should function
Toby, for the business name.