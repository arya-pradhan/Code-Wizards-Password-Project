## Product Description
In our Wizard Pass project, students learn about the importance of cybersecurity in an ever-evolving cyber landscape. Specifically, password security is one of the most fundamental aspects of good cyber hygiene. Throughout this project, students will build a password generator application that allows users to create strong passwords, and educates them about the characteristics of strong passwords. Additionally, students will build several advanced features of the application that will allow for a more personalized user experience. 

[Link To Figma](https://www.figma.com/file/oR4Gi2TXxp0UegPFX6iGmY/WizardPass?node-id=11%3A183&t=SSGGsExFh2HwEYMM-0)

## Standard Functionality

<details>
<summary>Click to Expand!</summary>
<!-- Standard Functionality Information Here -->
<strong>Important:</strong> all screens should be responsive! Mobile has separate but similar designs.

1. About page implemented, as shown in the design
    * The last line for contacting CodeWizardsHQ should hyperlink to https://www.codewizardshq.com/contact-us/
2. Password generator function (for now just generate a single password and show it on the front end, the multiple passwords at once comes later)
    1. The help/question mark icon, when clicked, opens a modal as shown in the design with information about different password types
    2. Ignore everything under the password type for now
    3. Also ignore the right column, except displaying the one generated password
    4. Password generation logic should be as follows:
        1. Simple passwords should concatenate a random adjective with a random noun, followed by a single number, picked at random
        2. Moderate passwords should concatenate a random adjective with a random noun, followed by three numbers, picked at random. Additionally, at least one of the letters in the password should be a symbol. For instance, an ‘s’ might become a $, a ‘u’ might become a #, etc.
        3. Strong passwords should be a random mix of letters, numbers, and symbols. Eventually, the user will be able to set rules to better control the password
    5. Ignore the password security tips carousel, that’s a future project
3. Let’s add some layers of complexity
    1. Strong passwords - allow the user to fill out the following settings aspects of the design and implement them in the password generation process:
    2. Have at least Y symbols
    3. Use no more than Z numbers
    4. *If the user does not fill them out, assume they don’t care
4. Let’s scale this up a bit. Suppose a user wants to create several passwords at once, all using the same settings
    1. Implement multiple simultaneous password generation, and add the field for “how many passwords” as shown in the design
    2. Show each password on the front end in the right column (don’t worry about the buttons in the right column yet)
    3. At this point, the entire middle column should match the design
5. Users who generate lots of passwords don’t want to have to copy them one by one.
    1. Implement an “Export to CSV” feature as shown in the design, which will export the current passwords on screen to a CSV file
    2. Perhaps users have some passwords on screen that they don’t like. Make a delete feature so they can remove passwords that have already been generated for them. Use a confirm() dialog to ask the user to confirm before removing.
    3. If users can remove, we should also let them add after they’ve generated passwords. Implement the “generate another like these” feature, which uses the settings provided to make another password and adds it to the front end without refreshing the page
    4. Give users a button to “copy to clipboard”, as shown in the design, which copies the password associated with the button to the user’s clipboard
    5. At this point, the entire right column should match the design.
6. Good applications understand what their users do. Let’s add some basic usage tracking to the application.
    1. Any time a password is generated, write an entry to the statistics table. Every entry will have a password type and a number of passwords. Only strong passwords will have the other fields filled out. Leave them blank if the user doesn’t provide them or they are not applicable to the password type. Use the database schema below to determine what information should be tracked.
    2. Build the statistics page as shown in the design to display this information in a summary view:
        1. Use google charts JS library (included in page template and docs are here https://developers.google.com/chart/interactive/docs to generate pie charts for any chart in the design
        2. The rest of the information should be self-explanatory

</details>

## Bonus Functionality

<details>
<summary>Click to Expand!</summary>
<!-- Bonus Functionality Information Here -->
In order, what to work on if there is time remaining in the project

1. Dark Mode
    1. Add a toggle switch as shown in the design for the user to switch to dark mode. Bonus points if the toggle auto selects based on what the user’s desktop settings are. The toggle switch will be on every page, so consider adding the code to switch to dark mode as shared code to the page template. 
    2. Each screen then needs to adapt to dark mode color scheme based on the user’s choice, as shown in the design
    3. The user’s choice of dark mode/light mode should be stored in the user’s browser, so that it remembers which they were on, the next time they come back to the site and switches to that mode. The default should be to light mode if the user does not have it stored one way or another.
2. Cybersecurity Survey
    1. Implement the cybersecurity survey page as shown in the design
    2. Responses will be stored in the survey table. The columns are set up as question1, question2, etc. in the database schema. Each survey submission is a unique row. 
    3. Responses will be stored in the survey table. The columns are set up as question1, question2, etc. in the database schema. Each survey submission is a unique row. 
        * Use google charts JS to generate graphs like in the above functionality. 
3. Password Security Tips (carousel)
    1. On the main page, as shown in the design, implement a carousel that displays the following password tips. Make sure the carousel automatically goes to the next screen.
        1. Use unique passwords for every site to minimize the risk of cascading compromised accounts
        2. Trust the place you store passwords. You’re only as secure as your password store
        3. Don’t give your passwords to anyone.
        4. Don’t input passwords on unsecure networks. Hackers can steal your password as it travels across the local network, unencrypted
        5. Don’t use information in passwords that people easily could find out about you, such as the street you live on or your name
        6. If you notice suspicious activity on any online account, change your password
        7. Don’t remain signed in to accounts on public or shared computers. Always log out!

</details>

## Database Layout

<details>
<summary>Click to Expand!</summary>
<!-- Database Design Information Here -->

 ### Table Name: words
 Purpose: stores words that’ll be used for generating simple and moderate passwords
 |   Column      |  Datatype     |  Primary Key  | Autoincrement | comment |
 | :-----------: | :-----------: | :-----------: | :-----------: | ------- |
 | id          |    integer    |       ✅      |       ✅      |         |
 | word_type   |    text       |       ❌      |       ❌      | Noun or Adjective |
 | word        |    text       |       ❌      |       ❌      | The actual word   |
 
 ### Table Name: statistics
 Purpose: provide statistics on what settings users are requesting when they generate passwords. *Never actually stores passwords or user information
 |   Column      |  Datatype     |  Primary Key  | Autoincrement | comment |
 | :-----------: | :-----------: | :-----------: | :-----------: | ------- |
 | id                  |    integer    |       ✅      |       ✅      |         |
 | timestamp           |    text       |       ❌      |       ❌      | date/time row was entered       |
 | password_type       |    text       |       ❌      |       ❌      | stores either “simple”, “moderate”, or “strong”, what the user’s password complexity level was |
 | number_of_passwords |    text       |       ❌      |       ❌      | how many passwords the user requested at that instance |
 | password_length     |    text       |       ❌      |       ❌      | stores the length of password setting, if provided by the user |
 | min_symbols         |    text       |       ❌      |       ❌      | stores the minimum number of symbols password setting, if provided by the user |
 | max_numbers         |    text       |       ❌      |       ❌      | stores the maximum number of numeric characters password setting, if provided by the user |
 
 ### Table Name: survey
  Purpose: provide a table to store survey responses. Reminder, this is a bonus feature Structure:
 |   Column      |  Datatype     |  Primary Key  | Autoincrement | comment |
 | :-----------: | :-----------: | :-----------: | :-----------: | ------- |
 |  id           |    integer    |         ✅        |         ✅    |                                 |
 |  question1    |    text       |         ❌        |         ❌    | response to the first question  |
 |  question2    |    text       |         ❌        |         ❌    | response to the second question |
 |  question3    |    text       |         ❌        |         ❌    | response to the third question  |
 |  question4    |    text       |         ❌        |         ❌    | response to the fourth question |
 |  question5    |    text       |         ❌        |         ❌    | response to the fifth question  |
 
</details>



## Requirements
- Latest [Python 3](https://www.python.org/downloads/) Version as of the start of the internship
- Update PIP to the latest version
   - Windows: `pip install --upgrade pip`
   - Mac/Linux `pip3 install --upgrade pip`
- [Pipenv](https://pypi.org/project/pipenv/)
  - Windows: `pip install --user pipenv`
  - Mac/Linux: `pip3 install --user pipenv`
- [Lastest Version of GIT](https://git-scm.com/downloads)
- [Github CLI](https://cli.github.com/): Used for Authentication
- Colorama: only if you get the error that says it is not installed
  - Windows: `pip install colorama`
  - Mac/Linux: `pip3 install coloram`  

## First Time Setup
- Perform the following from the root project director
- Install Project Dependencies: `pipenv install --dev`

## How to start the Flask Server
- Perform the following from the root project director
- Drop into virtual environment `pipenv shell`
- Set FLASK_ENV variable for page html reloading. Only need to set once per terminal session.
  - Windows CMD: `set FLASK_ENV=development`
  - Bash: `export FLASK_ENV=development`
- Start flask server: `flask --debug run`
- Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser

## Useful Commands
- Lists all options and commands for flask: `flask --help`
- Create the database: `flask db:create`
- Drop the tables in the database: `flask db:drop`
- Seeding the database: `flask db:seed`
  - This will add placeholder data to the database to make development easier. You can update the seed data in the `seed.py` file.
- Reset the database with seed data: `flask db:reset`

- Start Flask repl: `flask shell`
  - This allows you to interact with the database directly. You can import models, create, edit, and save data from the command line. You can learn more [here](https://flask.palletsprojects.com/en/2.1.x/cli/#open-a-shell).
- To run tests: `python -m pytest`

## Need more help?
- For help with making Sqlalchemy models you can checkout the models doc [here](models/models.md).
- For help making templates click [here](templates/templates.md)
- For help writing blueprints click [here](blueprints/blueprints.md)
- For help writing tests click [here](tests/pytest.md)
- For help creating a template [macro](templates/macros/macros.md)

## Additional Resources
- Flask SQLAlchemy can be located [here](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
- Great tutorial that walks through a simple flask app can be located [here](https://pythonbasics.org/flask-sqlalchemy/). 
- Documentation how how to [override bootstrap theme using css variables](https://getbootstrap.com/docs/5.2/customize/css-variables/)
- Learn how to use [bootstrap and its components](https://getbootstrap.com/docs/5.2/getting-started/introduction/).
- Using the [bootstrap grid system](https://getbootstrap.com/docs/5.2/layout/grid/).
- Learn how to use [Google Charts](https://developers.google.com/chart/interactive/docs/quick_start).
- View a list of all available [Material Icons](https://fonts.google.com/icons)
- [Github CLI Commands](https://cli.github.com/manual/)
- [Learn more about Github Discussions](https://docs.github.com/en/discussions)

