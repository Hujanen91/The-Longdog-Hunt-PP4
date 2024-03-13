# The Longdog Hunt

The Longdog Hunt is a simple blog based on the kids tv show Bluey and the easter eggs in the show called Longdogs that is hidden in plain sight in pretty much every episode. 

![Device Mockups]()
## Features

<a name="navbar"></a>
### __Navbar__

__Fully responsive navbar with links to:__

    - Home page
    - About page
    - Register section
    - Login section
    - Contact Section

__Logo hyperlinked to home page:__
![Logo](static/images/readme_files/File-01-color-1.png)

Featured on all pages across the site.

The navbar dapts to if user is authenticated or not (When logged in Login and Register will be hidden and Logout will be displayed in the navbar.)

__Navbar for non-authenticated users__:

![Navbar non auth]()
__Navbar for authenticated users__:

![Navbar auth]()

___Purpose of feature:___
Provide users with an easy and straight-forward way to navigate the site

<a name="footer"></a>
### __Footer__

Featured on all pages across the site.
The footer contains links to my personal GitHub, Instagram and Facebook.

![Footer]()

___Purpose of feature:___
Provide users with a way to connect with me and check out my GitHub profile and social media accounts.

<a name="home-page"></a>
### __Home page__

__The Home page consists of:__

    - Blog Section


__Blog Section__

The Blog Section features the blogposts created by the author and will be displayed the same no matter if the user is loged in or not.

![Blog Section]()


___Purpose of feature:___
Provide users with a welcoming landing page that is straight forward and clear for the user what the website is all about.



<a name="about-page"></a>
### __About page__

__The About page consists of:__

    - A profile picture of the blog admin
    - About section

![About page](img)

__Profile picture__

The About page displays an image of the admin next to the paragraph section.

___Purpose of feature:___
Provide users with some insight of who the admin is.

__About Section__

Gives a description of the blog and its content and gives a small presentation of who the admin is.

___Purpose of feature:___
Provide users with information about the blog and a description of the admin.

![About Section](img)

<a name="contact-page"></a>
### __Contact Page__

![Contact Page](img)

__The Contact page consists of:__

    - Contact Form

__Contact form__

The contact form gives the user a way to contact the admin of the blog if they have any questions etc.

The fields the user needs to fill in is:

- Name
- Email
- Message

_Additional_: All of the fields are required to be filled in, if it's not the user will be prompted to fill in the field before sending. 
The email field needs to contain an email with @ in it to be sent.

___Purpose of feature:___
Provide users with a way to contact the admin and creator of the site.

<a name="login-page"></a>
### __Login page__

![Login page](img)

__The Login page consists of:__

    - Login form

__Login form__

The login form allows the user to enter their credentials and authenticate to enter the sites authenticated state.

The login form also contains a link to the [Register page](#register-page) in case the user is not already registered.

___Purpose of feature:___
Provide users with a way to login to the site.

<a name="register-page"></a>
### __Register page__

![Register page](img)

__The Register page consists of:__

    - Sign up form

__Sign up form__

The Sign up form which is provided by django allows the user to enter credentials for registration on the site.

Through django it contains all the functionality for a secure registration and displays help text and error text to give the user feedback

The sign up form also contains a link to the [Login page](#login-page) in case the user already has an account.

___Purpose of feature:___
Provide users with a way to register an account on the site.

<a name="Blogpost-page"></a>
### __Blogpost page__

![Blogpost page](img)

__The Blogpost page consists of:__

    - A view of the blogpost
    - A commentfield under the blogpost

The Blogpost page displays the Title of the blogpost, the author, a time and date when the blogpost was created, possible images in the blogpost and the text content.

Below the blogpost there's a comment field and a textfield for a logged in user to write a comment in. If the user isn't logged in they can't comment and are prompted to login first along with links to the login page.

___Purpose of feature:___
Provide users with a way to see the specific blogposts and give logged in users a way to interact with the writer and share their opinion of the blogpost through comments.



<!-- __Like button__

The like button, placed on the right end of the screen in height with the project title, allows users to like or unlike a post.

_Additional_: The like button adapts to if the user is authenticated or not. If the user is not authenticated the like button is disabled and displays a tooltip on hover.

___Purpose of feature:___
Provide users with a way to to like posts they find interesting.

__Comment section__

![Comment section](media/commentsection.png)

The comment section allows users to post comments on a post aswell as delete their own comments using the X button in the above image.

_Additional_: The delete button displays a modal requiring the user to confirm deletion of the comment. -->
## Testing

__Manual testing__

<!-- _Tests done with DEBUG = False in settings.py_

___Case: Accessing authorization required links without logging in:___

| Link                                      | Expected Result          | Actual Result                  | Resolved by                               |
|-------------------------------------------|--------------------------|--------------------------------|------------------------------------------|
| [http://127.0.0.1:8000/profile_page/](http://127.0.0.1:8000/profile_page/) | Redirect to home page   | Server Error (500)            | Check user authenticated in associated view |
| [http://127.0.0.1:8000/project_submission/](http://127.0.0.1:8000/project_submission/) | Redirect to home page   | Project submission page loaded  | Check user authenticated in associated view |
| [http://127.0.0.1:8000/project_update/14/](http://127.0.0.1:8000/project_update/14/) | Redirect to home page   | Project update page loaded      | Check user authenticated and post author in associated view |
| [http://127.0.0.1:8000/delete_post/14/](http://127.0.0.1:8000/delete_post/14/) | Redirect to home page   | Server Error (500)            | Check user authenticated and post author in associated view |
| [http://127.0.0.1:8000/post_comment/14/](http://127.0.0.1:8000/post_comment/14/) | Redirect to home page   | Server Error (500)            | Check user authenticated in associated view |
| [http://127.0.0.1:8000/like_post/14/](http://127.0.0.1:8000/like_post/14/) | Redirect to home page   | Server Error (500)            | Check user authenticated in associated view |
| [http://127.0.0.1:8000/delete_comment/10/14/](http://127.0.0.1:8000/delete_comment/10/14/) | Redirect to home page   | Server Error (500)            | Check user authenticated and comment owner in associated view |

___Case: Inserting invalid or no data during project submission:___

| Test                                          | Expected Result                  | Actual Result                                       | Resolved by                               |
|-----------------------------------------------|----------------------------------|-----------------------------------------------------|------------------------------------------|
| Upload file larger than 10MB                  | Error message                    | Server Error (500)                                  | Write js script to validate inputs       |
| Upload file + toggle generate from link       | Error message / Toggle not available when file uploaded | Post uploaded using image generated from link | Write js script to validate inputs       |
| Post using a non-GitHub repo link in field    | Error message                    | Post uploaded successfully                           | Write js script to validate inputs       |

___Case: Inserting invalid or no data during update project:___

| Test                                          | Expected Result                  | Actual Result                                       | Resolved by                               |
|-----------------------------------------------|----------------------------------|-----------------------------------------------------|------------------------------------------|
| Upload file larger than 10MB                  | Error message                    | Server Error (500)                                  | Write js script to validate inputs       |
| Upload file + toggle generate from link       | Error message / Toggle not available when file uploaded | Post uploaded using image generated from link | Write js script to validate inputs       |
| Post using a non-GitHub repo link in field    | Error message                    | Post uploaded successfully                           | Write js script to validate inputs       | -->


__Unit testing__

<!-- Unit tests were written using PyTest and Selenium since Seleniums abillity to interact directly with the browser better reflects how the user actually would interact with the site. Tests were written with the AAA(Arrange, Act, Assert) principle in mind.

Unit test files:

    1. test_noauth_protection.py
        - Tests access to authorization required url routes when user is not authenticated
    2. test_auth.py
        - Tests sign up functionality
        - Tests login functionality
        - Tests access to profile page and project submission page when logged in
    3. test_misc.py
        - Tests access to login and signup page when already logged in
    4. test_like_comment.py
        - Tests like / unlike functionality
        - Tests comment / delete comment functionality
    5. test_submission_update.py
        - Tests invalid inputs in submission form
        - Tests invalid inputs in update project form -->

## Validators

__HTML & CSS__

All html and css files ran through the [Official W3C validator](https://validator.w3.org/)

___CSS___: All files valid

___HTML___: 100+ errors, all due to the use of Jinja templating

__Python__

All files ran through Code Institutes [Python Linter](https://pep8ci.herokuapp.com/#)

___hub_main/views.py___

| Line | Error                                  |
| ---- | -------------------------------------- |
| 77   | E501 line too long (138 > 79 characters) |
| 103  | E501 line too long (97 > 79 characters)  |
| 137  | E501 line too long (138 > 79 characters) |
| 229  | E501 line too long (81 > 79 characters)  |
| 287  | E501 line too long (93 > 79 characters)  |
| 304  | E501 line too long (91 > 79 characters)  |
| 314  | E501 line too long (93 > 79 characters)  |
| 320  | E501 line too long (93 > 79 characters)  |

___hub_main/urls.py___

| Line | Error                                  |
| ---- | -------------------------------------- |
| 6    | E501 line too long (96 > 79 characters) |
| 7    | E501 line too long (112 > 79 characters)|
| 8    | E501 line too long (94 > 79 characters) |
| 9    | E501 line too long (98 > 79 characters) |
| 10   | E501 line too long (110 > 79 characters)|
| 11   | E501 line too long (102 > 79 characters)|
| 12   | E501 line too long (127 > 79 characters)|
| 13   | E501 line too long (120 > 79 characters)|
| 14   | E501 line too long (90 > 79 characters) |
| 15   | E501 line too long (98 > 79 characters) |

___hub_main/models.py___

| Line | Error                                  |
| ---- | -------------------------------------- |
| 19   | E501 line too long (149 > 79 characters)|
| 21   | E501 line too long (91 > 79 characters) |
| 22   | E501 line too long (95 > 79 characters) |
| 25   | E501 line too long (91 > 79 characters) |
| 43   | E501 line too long (85 > 79 characters) |

___hub_main/tests.py:___ All clear, no errors found

___hub_main/apps.py:___ All clear, no errors found

___hub_main/admin.py:___ All clear, no errors found

___hub_main/tests/test_submission_update.py___

| Line | Error                                  |
| ---- | -------------------------------------- |
| 14   | E501 line too long (86 > 79 characters) |

___hub_main/tests/test_noauth_protection.py___

| Line | Error                                  |
| ---- | -------------------------------------- |
| 14   | E501 line too long (86 > 79 characters) |

___hub_main/tests/test_misc.py:___ All clear, no errors found


___hub_main/tests/test_like_comment.py___

| Line | Error                                  |
| ---- | -------------------------------------- |
| 14   | E501 line too long (82 > 79 characters) |
| 22   | E501 line too long (86 > 79 characters) |
| 23   | E501 line too long (81 > 79 characters) |
| 30   | E501 line too long (82 > 79 characters) |
| 38   | E501 line too long (86 > 79 characters) |
| 39   | E501 line too long (81 > 79 characters) |
| 46   | E501 line too long (81 > 79 characters) |
| 47   | E501 line too long (80 > 79 characters) |
| 64   | E501 line too long (102 > 79 characters)|
| 65   | E501 line too long (102 > 79 characters)|
| 68   | E501 line too long (82 > 79 characters) |
| 69   | E501 line too long (90 > 79 characters) |

___hub_main/tests/test_auth.py___

| Line | Error                                  |
| ---- | -------------------------------------- |
| 20   | E501 line too long (80 > 79 characters) |
| 21   | E501 line too long (82 > 79 characters) |
| 22   | E501 line too long (82 > 79 characters) |
| 29   | E501 line too long (81 > 79 characters) |
| 53   | E501 line too long (92 > 79 characters) |
| 62   | E501 line too long (107 > 79 characters)|

___hub_main/run_tests.py:___All clear, no errors found

___hub_main/helper_functions.py___

| Line | Error                                  |
| ---- | -------------------------------------- |
| 22   | E501 line too long (85 > 79 characters) |

___members/views.py:___ All clear, no errors found

___members/urls.py:___ All clear, no errors found

___members/tests.py:___ All clear, no errors found

___members/models.py:___ All clear, no errors found

___members/apps.py:___ All clear, no errors found

___members/admin.py:___ All clear, no errors found

Errors ignored since they make no impact on the functionality but might impact functionality if resolved.

__JavaScript__

All files run through the [JSHint Linter](https://jshint.com/)

___card_animations.js___

| Line | Warning                                                        |
| ---- | --------------------------------------------------------------- |
| 6    | Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (gsap, card) |
| 9    | Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (gsap, card) |

| Error |
| ----- |
| var gsap not declared (declared in script tag in template) |

___home_animations.js___

| Error |
| ----- |
| var gsap not declared (declared in script tag in template) |

___option_animations.js___

| Line | Warning                                                        |
| ---- | --------------------------------------------------------------- |
| 5    | Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (gsap, option) |
| 8    | Functions declared within loops referencing an outer scoped variable may lead to confusing semantics. (gsap, option) |

| Error |
| ----- |
| var gsap not declared (declared in script tag in template) |

___load_github.js:___ No errors or warnings.

___validate_inputs.js:___ No errors or warnings.

___word_animations.js___

| Error |
| ----- |
| var gsap not declared (declared in script tag in template) |

__Lighthouse__

All pages were analyzed by Lighthouse: [See reports](https://drive.google.com/drive/folders/1D13aGpjEhCFeHpAR_vUcITRPG4WzOIBk?usp=sharing)

## Deployment

This project was deployed to Heroku using these steps:

    1. Fork or clone this repository
    2. Create a new Heroku app
    3. Set the buildpacks to Python
    4. Set the config vars for your database connection and api keys
    4. Link the Heroku app to the repository
    5. Click on deploy

## Run Locally

Clone the project

```bash
  git clone https://github.com/linx02/project-hub.git
```

Go to the project directory

```bash
  cd project_hub
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Start the server

```bash
  python3 manage.py runserver
```

Note that you will have to setup your own database and API connections using these steps:

1. Create a file name "env.py" in the projects root directory.
2. Copy and paste this code in the env.py file and replace values with your own:

```python
import os

os.environ["DATABASE_URL"]=YOUR_DATABASE_URL
os.environ["SECRET_KEY"]=YOUR_SECRET_KEY
os.environ["CLOUDINARY_SECRET"]=YOUR_CLOUDINARY_SECRET
os.environ["THUMIO_AUTH"]=YOUR_THUMIO_AUTH_KEY
```

## Database schema

![Database schema](media/schema.png)

## Credits

__API's used__:

[GitHub' REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28): For fetching Readme.md file for Readme section in [Project page](#project-page).

[Thum.io's URL API](https://www.thum.io/documentation/api/url): For generating screenshots of provided links during project submission.

__Libraries and frameworks__:

[Bootstrap](https://getbootstrap.com/): CSS framework used.

[Django](https://www.djangoproject.com/): Web framework used.

[GreenSock's GSAP](https://greensock.com/): For animations.

[PyTest](https://docs.pytest.org/en/7.4.x/): For testing.

[Selenium](https://www.selenium.dev/): For testing.

__Data storing__:

[PostgreSQL](https://www.postgresql.org/): Database management system used.

[Cloudinary](https://cloudinary.com/): For storing image files in the cloud.

__Media__:

[Freepik](https://www.freepik.com/): For svg in the hero section.

[Haikei](https://haikei.app/): For background svg on the [home page](#home-page).

[FontAwesome](https://fontawesome.com/): For icons.