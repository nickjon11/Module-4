Module 4:
6/16/26

Release notes:
Split up the operations to a seperate folder, so functions like adding, subtracting, multiplying, and dividing are now individual python programs. 
Changed up the options in the input menu from float numbers to just the operator choice. I could probably try and fix that later on but it works at least. 
History function only works well as long as you don't do exit. Exit clears out the history cache. By having this feature be a thing, the program doesn't shutdown after being used, you have to manually do it yourself unlike Module 3

Setup:
run in terminal:
python3 -m venv venv
source venv/bin/activate
Install dependencies:
pip install pytest pytest-cov
To run it: python3 -m app.calculator.calculator in terminal
To run test: pytest
