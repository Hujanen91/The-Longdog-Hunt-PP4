## Manual Functional Testing

<details>
<summary><b>Navigation</b></summary>
<br>
<summary>
<b>Navigation Links</b>

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

- Home -> index.html

![Home](static/images/readme_files/testing_gifs/clickhometoindex.gif)
- About -> about.html

![About](static/images/readme_files/testing_gifs/clickabout.gif)
- Contact -> contact.html

![Contact](static/images/readme_files/testing_gifs/clickcontact.gif)
- Likes -> liked_posts.html

![Like post](static/images/readme_files/testing_gifs/likes-posts-page.gif)
- Logout -> Sign out all auth page

![Logout](static/images/readme_files/testing_gifs/logout-gif.gif)
- Login -> Sign in all auth page

![Login](static/images/readme_files/testing_gifs/clicklogin.gif)
- Register -> Sign up all auth page

![Register](static/images/readme_files/testing_gifs/clickregister.gif)
- Clicking on blogposts in index.html -> post_detail.html

![Blogpost](static/images/readme_files/testing_gifs/blog_post_view.gif)

- Link to login on register -> Sign up all auth page
- Link to login on post_detail.html -> Sign in all auth page
- Link to sign up all auth page on login page -> Sign up all auth page

- Navigation menu will scale down to a hamburger menu when screen size gets smaller and the longdog dog icon will be hidden to save space on page. Instead a longdog icon is hidden at the top of the collapsed menu.

![Blogpost](static/images/readme_files/testing_gifs/menu-collapse.gif)

All navigation links directed to the correct pages as expected.
</summary>
</details>

<hr>

<details>
<summary><b>Contactform</b></summary>
<summary>
<br>
<hr>

- The contactform can be used no matter if the user is authenticated or not and will give the same results regarding required fields and prompted messages.

<hr>
Description:

Make sure a user can send a message with the contact form

Steps:

1. Navigate to the contact page
2. Fill in the fields
3. Press send, the user should get a confirmation message

<hr>

Expected:

The user should get a message confirming the message is sent.

Actual: 

The confirming message is displayed when user clicks on submit.

![Contact form](static/images/readme_files/docs/contact-form-sent-confirm.png)

<hr>

Description:

Make sure a user fills in the form correctly before sending message.

Steps:

1. Navigate to the contact page
2. Do not add any information.
3. Press send, the user should get a message telling them to fill in the name field.
4. Add only a name.
5. Press send, the user should get a message telling them to fill in the email field.
6. Add email but no message.
7. Press send, the user should get a message telling them to fill in the message field.
8. Add message.
9. Press send, the user should now get the confirmation message that the message is sent now that all required fields are filled in.

<hr>

Expected:

The user should get a message prompting them to fill in the required field that is missing content on each field that is empty in the contact form.

Actual: 

The message is prompted on each field when the user has left them empty. 
When every required field is filled the message is sent and the user gets the confirmation message.

![Name required](static/images/readme_files/testing/contact-name-req.png)
![Email required](static/images/readme_files/testing/contact-email-req.png)
![Email required](static/images/readme_files/testing/contact-email-req-2.png)
![Message required](static/images/readme_files/testing/contact-msg-req.png)
![Message sent](static/images/readme_files/docs/contact-form-sent-confirm.png)

</summary>
</details>

<hr>

<details>
<summary><b>Authentication</b></summary>
<summary>
<br>

Description:

Ensure a user can register to the website

Steps:

1. Navigate to [The longdog Hunt](https://the-longdog-hunt-9f116eb214b4.herokuapp.com/accounts/signup/) and click Register
2. Enter email, username and password 
3. Click Sign up

<hr>

Expected:

If a user has entered everything correctly they should be logged in upon clicking on sign up.

Actual: 

The users is logged in upon clicking on sign up.

![Signup](static/images/readme_files/testing_gifs/signup-gif.gif)

<hr>

Description:

Ensure a user can log in once signed up

Steps:
1. Navigate to [The Longdog Hunt login](https://the-longdog-hunt-9f116eb214b4.herokuapp.com/accounts/login/)
2. Enter login details created in previous test case
3. Click login

<hr>

Expected:

User is successfully logged in and redirected to the home page

Actual:

User is successfully logged in and redirected to the home page

![Signup](static/images/readme_files/testing_gifs/login-gif.gif)

<hr>

Description:

Ensure a user can sign out

Steps:

1. Login to the website
2. Click the logout button
3. Click confirm on the confirm logout page

<hr>

Expected:

User is logged out

Actual:

User is logged out

![Signup](static/images/readme_files/testing_gifs/logout-gif.gif)

<hr>

Description:

Ensure the user is required to enter username and correct password according to the requirements

Steps:

1. Navigate to [Signup](https://the-longdog-hunt-9f116eb214b4.herokuapp.com/accounts/signup/)
2. Enter details but skip the username
3. Click sign up

<hr>

Expected:

The user is prompted to fill out the username field. If user does not fill the name out a message should appear prompting the user to fill out that field.

Actual:

The username field displays a message telling the user to fill out the missing field.

![Signup](static/images/readme_files/testing/sign-up-username-req.png)


No password:

1. Navigate to [Signup](https://the-longdog-hunt-9f116eb214b4.herokuapp.com/accounts/signup/)
2. Enter details but skip the password
3. Click sign up

<hr>

Expected:

The user is prompted to fill out the password field

Actual:

An alert message appears and is prompting the user to fill out the password field.

![Signup](static/images/readme_files/testing/sign-up-password-req.png)


Wrong password:

1. Navigate to [Signup](https://the-longdog-hunt-9f116eb214b4.herokuapp.com/accounts/signup/)
2. Enter details but enter a password that is not correct
3. Click sign up

<hr>

Expected:

The user is prompted to fill out the correct password according to the requirements.

Actual:

An alert message appears and is prompting the user to fill out the password the correct way.

![Signup](static/images/readme_files/testing/sign-up-password-req-2.png)
![Signup](static/images/readme_files/testing/sign-up-password-req-3.png)
![Signup](static/images/readme_files/testing/sign-up-password-req-4.png)

</summary>
</details>

<hr>

<details>
<summary><b>Authenticated user functions</b></summary>
<summary>
<br>
<b>User comment creation</b><br>
Description:

Ensure user can successfully create a comment.

Steps:
1. Login as a user.
2. Click on a blogpost and scroll down to the comments field.
3. Write a comment and click post, the user should get a confirmation message.
4. The comment is now displayed with the correct "edit" and "delete" buttons.

<hr>

Expected:

Comment is posted with a confirmation message and the comment is displayed straight away with correct buttons below (buttons only visible for the author of the comment)

Actual:

Comments, confirmation message and buttons are all displayed as they are supposed to without any issues.

![Signup](static/images/readme_files/testing_gifs/comment-submit.gif)
![Signup](static/images/readme_files/testing_gifs/new-comment-displayed.gif)

<hr>

<b>Edit and delete own comments</b><br>
Description:

Ensure user can only edit and delete their own comment.

Steps:
1. Login as a user
2. Go to a post with comments you've created or create a comment.
3. Others comments should not have any buttons visible, buttons should only be displayed on the users own comment.

<hr>

Expected:

The user can only edit and delete their own comments

Actual:

The edit and delete buttons are only visible to the author of said comment.

![Signup](static/images/readme_files/docs/comments.png)

<hr>

<b>User edit comment</b><br>
Description:

Make sure a user can edit their comment with a confirmation message when posting their comment again.

Steps:

1. Navigate to the blogpost with users own comments on it.
2. Click the edit button on the comment.
3. The comment should now appear in the comment window to the right (or below on smaller screens) and the user can now edit the comment and click on submit.
4. Click on submit, user should now get a confirmation message and the new comment is now posted.

<hr>

Expected:

Users comments can be edited when clicking Edit below the users comment. When clicking submit the confirmation message should appear and the new comment should be displayed.

Actual:

The comment can be edited, message is displayed when new comment is submitted and the new comment is visible in the commentsfield.

![Comment edit](static/images/readme_files/testing_gifs/edit-comment.gif)

<hr>

<b>User delete comments</b><br>
Description:

Make sure the user can delete their comment.

Steps:

1. Navigate to the blogpost with users own comments on it.
2. Click the delete button on the comment.
3. A modal making sure the user wants to delete their comment should now appear.
4. After user confirms a confirmation message is displayed and comment is deleted

<hr>

Expected:

User should be abled to press the delete comment, confirm in the modal that they want to delete and then get a message confirming that comment now is deleted.
The comment should now have been deleted.

Actual:

The comment is deleted as expected.

![Comment delete](static/images/readme_files/testing_gifs/comment-delete-and-confirm.gif)

<hr>

<b>User likes</b><br>
Description:

Ensure user can like and dislike a post when logged in

Steps:
1. Login as a user
2. Go to a post and scroll down.
3. Click on the like button (a heart) and the user should now get a message that they liked the post and the heart should now be a solid white heart and the number should change with a +1.
4. Click on the like button again and another message should display telling the user they've unliked the post and the heart should now be hollow and the number should have changed with -1.

<hr>

Expected:

The user can like and unlike a post and get a message telling them they did.
The heart should turn from hollow to solid when liked and then back again if unliked.
The number on the like button should change with a +1 if liked and -1 if unliked.

Actual:

The like button works as expected above.
![Like](static/images/readme_files/testing_gifs/like-post-and-confirmation.gif)
![Unlike](static/images/readme_files/testing_gifs/unlike-post-confirmation.gif)

<hr>

<b>Liked posts page</b><br>
Description:

When a user is authenticated a new page in the navbar appears, the Likes page.
The user can navigate to the Likes page to view all their liked posts. 
From here they can reach each post by clicking on them.

Steps:

1. Navigate to the Likes page in the navbar.
2. Now the list of liked posts should be displayed for the user.

<hr>

Expected:

The user can view all their liked posts by navigating to the Likes page.

Actual:

The Likes page works as it should and the users liked posts are displayed.
![Liked posts](static/images/readme_files/testing_gifs/likes-posts-page.gif)

</summary>
</details>

<hr>

<details>
<summary><b>Non authenticated user</b></summary>
<summary>
<br>

<b>Can't comment or like</b><br>

Description:
Ensure that a user that isn't authenticated can't comment or like blogposts

steps:
1. Navigate to a blogpost without signing in.
2. Scroll down to comments.
3. A message next to the comments should be displayed telling the user they need to be logged in to comment or like.
4. When clicking on the like button above the comments nothing should happen.

<hr>

Expected:

The comment textfield should not be displayed for a non authenticated user and a message should tell them to sign in to comment or like and a link to the login page should be provided.

Actual:

The commenfield is not displayed and the message is showing with a link to the login page.

![Commentfield](static/images/readme_files/testing/comment-login-required.png)

Expected:

Clicking on the like button as a non authenticated user will do nothing to the like button. 

Actual:

The like button is disabled and the non authenticated user can't click on the like button.

![Like button](static/images/readme_files/testing_gifs/like-post-signin-req.gif)

Expected:

As a user that isn't authenticated the navbar should display Home, About, Contact, Register and Sign in.

Actual:

The navbar displays the exptected links.

![Navbar logged out](static/images/readme_files/docs/navbar-complete.png)

</summary>
</details>

<hr>

<details>
<summary><b>Confirmation</b></summary>
<br>
<summary>
<b>Confirmation messages</b>

Confirmation messages are prompted whenever the user makes any type of change: 

- Sign in - "Successfully signed in as -username-"
- Sign up - "Successfully signed in as -username-"
- Sign out - "You have signed out"
- Submits a comment - "Comment submitted successfully"
- Edit a comment - "Comment updated!"
- Deletes a comment - "Comment deleted!" 
- Sends a messade with the contact form - "Thank you for your message. I will get back to you as soon as possible"
- Likes a post - "You have successfully liked this post"
- Unlikes a post - "You have successfully unliked this post"


These have all been tested and are prompted as they should:

![Signing in](static/images/readme_files/testing/login-confirmation.png)
![Singing up](static/images/readme_files/testing/sign-up-confirmation.png)
![Signing out](static/images/readme_files/testing/signed-out-confirm.png)
![Post Comment](static/images/readme_files/testing/comment-confirm.png)
![Edit comments](static/images/readme_files/testing/edit-comment-confirm.png)
![Delete comments](static/images/readme_files/testing/comment-delete-confirm.png)
![Send message in contactform](static/images/readme_files/testing/contact-form-sent-confirm.png)
![Like a post](static/images/readme_files/testing/Liked-post-confirmation.png)
![Unlike a post](static/images/readme_files/testing/unliked-confirm-msg.png)

</summary>
</details>

<hr>

<details>
<summary><b>Admin Panel Testing</b></summary>
<summary>

The adminpanel testing was done by clicking my way trough and manually test the functions.
Everything that was already set from the walkthrough works as it should, nothing is bugged.

I added a Season and Episode selection to the admin create post panel.
This makes it possible to pick Season and Episode that the post is gonna be about.
If non of them are selected there will be nothing posted next to the date/time on blogposts. If the user selects Season and Episode then they will show next to date/time on the blogpost.

The only bug that needs to be fixed later on is when creating a post.
Admin can pick already known users that has liked the post but only one at a time. 
If multiple users are picked then the admin is prompted to create users.
This field will be removed in later edits when I have more time.


</summary>
</details>

**Footer**

Testing was performed on the footer links by clicking the font awesome icons and ensuring that the facebook icon opened facebook in a new tab, that the instagram icon opened instagram in a new tab and the github icon opened the github respitory in another tab. These behaved as expected.


## Code Validation
__HTML & CSS__

All html and css files ran through the [Official W3C validator](https://validator.w3.org/)

___CSS___: All files valid<br>

![CSS](static/images/readme_files/docs/Validation-css-clear.png)

___HTML___: All html passed whitout any errors except for the blogpost page and signup page.

![HTML](static/images/readme_files/docs/Validation-HTML-index-clear.png)

Errors displayed below are errors <b>caused by Allauth and by Summernote and is nothing I can do anything about</b> considering the errors are caused by code from other packages and not my direct code.

Summernote adds styling to the HTML code on blogposts and about page that I have not added myself and this is then causing errors in the validation.
Errors ignored since they are not caused by my code and make no impact on the functionality but might impact functionality and the visual aspects if resolved.

![HTML Errors](static/images/readme_files/docs/Validation-HTML-signup-errorsfromdjangoform.png)
![HTML Errors](static/images/readme_files/docs/Validation-HTML-signup-errorsfromdjangoform-details.png)
![HTML Errors](static/images/readme_files/docs/Validation-HTML-blogpost-error-summernote.png)
![HTML Errors](static/images/readme_files/docs/Validation-HTML-blogpost-error-summernote-2.png)

The warning in the code is known and is nothing I can change as it would throw off my styling and layout of the blogtitle. The h1 is the top level, it's the first h1 element in the code, moving it around would make the layout change so I left it as it is.

<b>Error nr.13 above is also caused by summernote. The image below displays the lines of code that is (according to the validator) wrong. The error is again caused by summernote adding styling in my html code on the livesite.

![HTML Errors](static/images/readme_files/docs/code-error-validation-source.png)



__Python__

All files ran through Code Institutes [Python Linter](https://pep8ci.herokuapp.com/#)<br>
Every .py file has passed without any issues or errors.<br>

![python](static/images/readme_files/docs/Validation-python-clear.png)

__JavaScript__

All files run through the [JSHint Linter](https://jshint.com/)
Javascript file passed without any issues or errors.

![javascript](static/images/readme_files/docs/Validation-js.png)

__Lighthouse__

Website was analyzed with Lighthouse: ![Lighthouse](static/images/readme_files/docs/Lighthouse.png)<br>

Performance can be improved with changing how cloudinary handles the images.
Some of the issues that had negative impact on the perfomance had to do with Heroku itself and the database, things I can't change at this moment.

__Wave__

The website was checked through wave [Wave](https://wave.webaim.org/)
No Errors are showing up in Wave.

![Wave](static/images/readme_files/docs/Validation-wave-index-clear.png)


## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

Steps to test:

- Open browser and navigate to [The Longdog Hunt](https://the-longdog-hunt-9f116eb214b4.herokuapp.com/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Set the zoom to 50%
- Click and drag the responsive window to maximum width

Expected:<br>
Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:<br>
Website behaved as expected.

Website was also opened on the following devices and no responsive issues were seen:

Google Pixel 8 Pro<br>
Huawei p20 pro



## Bugs

There are no current bugs on the website that I know of.

Bugs that I bumped into in production but managed to solve:

- Got errors and warnings on livesite. 
This was solved by looking at my other code from I think therefore I blog and compare it. I then realized I hade to move endblocks to correct places and that solved the problem.

- Removing approval on comments did not work at first. 
This was solved when I found out that I missed one approval.

- Comments recently posted by user duplicates if user refreshes the page.
This was solved by removing post.comments.all() in views.py due to it retrieving all comments related to the post and instead add "return HttpResponseRedirect(request.path_info)" and " comments = post.comments.filter(approved=True).order_by("-created_on")" to the post_detail view.

- Got bad request 400 on Heroku after deployment and after trying to install cloudinary storage for staticfiles. 
This was eventually solved by adding a code above cloudinary storage codes in settings.py that promted cloudinary to send https instead of http that threw errors.
This bug is related to the bug below:

- Got errors in devtools telling me I had mixed content requested as insecure element (http) and had to automatically be upgraded to HTTPS. Solved this error by import coudinary in settings and then adding cloudinary.config(secure=True) above my static files, now everything works without any issues.
This solution also made the cloudinary storage of staticfiles possible.