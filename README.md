# Adrestia
Course planning tool for CU Boulder Students. First create an account (which will save your settings and course selection for future access), and login. You can then add classes to your spring 2018 or fall 2019 semesters. This tool will let you see the total challenge level and the total hours per week you will need to spend on studying and homework for that semester. Additionally you can change two sliders to set limits to these two statistics. If a semester exceeds one of the limits it will highlight red to notify you. Data for these statistics are drawn from the CU Boulder FCQ data found here: https://fcq.colorado.edu/UCBdata.htm. For this site a weighted average (by # of responses) is used from the last six years (six years was arbitrarily chosen as "recent enough" so that very old classes, professors, and curiculums don't skew the numbers). Because we only look at the fall and spring semesters, data from summer classes (which are accelerated and have higher hours per week numbers) is excluded.


You can use this tool here:
https://adrestia2.herokuapp.com/

During the course of this project we encountered issues with eventually merging all our independant bits of code, our project was also in desperate need of a rebuild from what we had learned over the course of the project especially in regard to how all the django bits fit together. To achieve this with minimal headache I used a second repo here https://github.com/Sisyphus192/Adrestia2 where I put together the different contributions from our team members on their different branches. The website.old folder contains all the previous code.

Credit goes to https://simpleisbetterthancomplex.com/ for their excellent django tutorials which helped us create this project.

REPO Structure:
All code related to the running of the website is in the folder "website/" (a previous iteration is accesible under "website.old/"). Procfile, requirements.txt, and runtime.txt are necessary for lauching on heroku. The data folder contains csv files for our FCQ data. Documents and the Milestone folders contain misc classwork. migrate.py contains the code we use to preprocess and upload our fcq data to the heroku postgres database.

For those unfamiliar with how Django works the structure under "website/" is thus:
-- website/
-- main/
-- accounts/
-- templates/
-- static/
-- manage.py

manage.py is created by django to manage the whole django project and run the website.
website/ (django requires it to have the same name as the parent folder, or we would have given it a more appropriate name (like "settings")) contains the site wide django settings
main/ contains the code to run our site
static/ contains static files like boostrap.css, our own .css files, .js files, etc
templates/ contains all the .html templates that django builds off of
accounts/ contains the code to facilitate our user account login system
