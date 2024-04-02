# Testing

Return back to the [README.md](README.md) file.

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


## Code Validation
__HTML & CSS__

All html and css files ran through the [Official W3C validator](https://validator.w3.org/)

___CSS___: All files valid

___HTML___: All html passed except for the blogpost page and signup page. 
Errors displayed below are errors caused by Allauth and by Summernote and is nothing I can do anythin about considering the errors are caused by code from other packages and not my direct code.
Errors ignored since they are not caused by my code and make no impact on the functionality but might impact functionality and the visual aspects if resolved.

__Python__

All files ran through Code Institutes [Python Linter](https://pep8ci.herokuapp.com/#)

Every .py file has passed without any issues or errors.


__JavaScript__

All files run through the [JSHint Linter](https://jshint.com/)

Javascript file passed without any issues or errors.

__Lighthouse__

All pages were analyzed by Lighthouse: [See reports]()


## Bugs

| Screenshot | Notes |
| --- | --- |
| ![screenshot](docs/bug__linetoolong.png) |  Three lines of code in option-picking the riddles was given the "line too long" warning in the validator. I tried everything to break the lines in two and make it work and everything came back giving errors in either the terminal or in the validator. The only thing that actually worked without errors was a backward slash but instead this created a big gap between the line telling the user to pick an answer and the "(1-4)". I decided to edit the printed text to make it short enough to be on the same line to make it work and look the best it could without awkward gaps. |

---