# Adrestia
Course planning tool for CU Boulder Students. First create an account (which will save your settings and course selection for future access), and login. You can then add classes to your spring 2018 or fall 2019 semesters. This tool will let you see the total challenge level and the total hours per week you will need to spend on studying and homework for that semester. Additionally you can change two sliders to set limits to these two statistics. If a semester exceeds one of the limits it will highlight red to notify you. Data for these statistics are drawn from the CU Boulder FCQ data found here: https://fcq.colorado.edu/UCBdata.htm. For this site a weighted average (by # of responses) is used from the last six years (six years was arbitrarily chosen as "recent enough" so that very old classes, professors, and curiculums don't skew the numbers). Because we only look at the fall and spring semesters, data from summer classes (which are accelerated and have higher hours per week numbers) is excluded.


You can use this tool here:
https://adrestia2.herokuapp.com/

During the course of this project we encountered issues with eventually merging all our independant bits of code, our project was also in desperate need of a rebuild from what we had learned over the course of the project especially in regard to how all the django bits fit together. To achieve this with minimal headache I used a second repo here https://github.com/Sisyphus192/Adrestia2 where I put together the different contributions from our team members on their different branches. The website.old folder contains all the previous code.

Credit goes to https://simpleisbetterthancomplex.com/ for their excellent django tutorials which helped us create this project.