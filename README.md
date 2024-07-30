# YOUR PROJECT TITLE
#### Video Demo:  <https://youtu.be/HiFIeM0ZPMQ?si=Y0OxaDDCC04a8WX5>
#### Description:
Its a web app that uses javascript, Python and SQL which gives Diode model based on your given specifications.As I am from electrical engineering background, I mostly come across selecting diode bridge by given specification, but everyime it gives problem for getting proper model based on specification. So, i have devoloped a database cotaining specifications and model number.
Then i created html pages, named home, layout,table and news html pages. In which layout gives layout html.
News page gives latest news about electronics in the world about components
In contact us page gives details about contact adresses. in which i have used bootstrap card format and a picture.
In app.py file the all the flask code available.
In layout page all the navigation from one page to other pages are mentioned. and in app.py the route to all pages defined.
In layout page i have used navbar type bootstrap to show all other page names.
layout page also include jquery scripts adddition of bootstrap and script and style of bootstrap.
And i also have included styles sheet of my own for some changes in colour of my choice and background image of my choice.
The background image of pic is saved in the static folder.
and i also added favicon.ico to my web app. which saved in static page.
For data base i have created rectifier.db database from the csv file whihch include specifications of the diode and diode models.
In the main part of the my web app the page i want to show default is home page. In which Three input text fields are used named average rectifier current , reverse peak voltage current, peak rectifier current as place holders. Once these input fields filled you can click submit button to vies the results.
I have mentioned textfield as numbers and number should be minimum 0. so that it will warn you if you type any alphabet or negative numbers and it won't receive your input.
if You wanted to view all the database just leave the input fields as blanks, it will gives you the table containing all the diode model numbers and specifications.
As you may have seen the table will created on the home page it self without refreshing the page.
For this to be done i have used ajax.
The procedure is as follows:
1) first the data from the input field is values stored in the jquery variables.
2) from the jquery variables the data postd to the variable created in the app.py "/" route.
3) From the variables received from the jquery script we execute the command and save it to the variable called table.
4) the data from the table variable is returned to the jquery script. this jquery script data is given to the blank html worksheet which will create the table nd further added to the home page.
5) the execution of this made in app.py and sql in the route of "update_table".
so here is the brief introduction to the my CS50 final project.
 when the table created the User can take the model number and search in the google to buy it.
