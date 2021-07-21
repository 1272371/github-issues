# github-issues
Bitcast Coding Assessment


Requirements
The service must be implemented in Python, using the
Django web framework and the
Requests library for interacting
with GitHub. No Python wrappers for the GitHub API should be used. Users can
access the service through the curl command with the URL as the payload.
The repository must use git for version control and contain clear
documentation in the README file on how to get the service running under Linux.
There should also be a documented way of running unit tests that demonstrate the
functionality of the service. If you have any open source personal projects that
you would like us to look at, include links to them in the README.
Submissions should be in the form of a compressed archive as produced by


 The results should be sorted by the title of the issues using the bubble sort algorithm. 

The results should be sorted alphabetically without being case-sensitive. 

In other words, be in the order 'A', 'a', 'B', 'b' ('a', 'A', 'b', 'B' would also be valid).


git clone https://github.com/1272371/github-issues
cd to github-issues/
pip install -r requirments.txt
cd to githubIssues/Scripts
open the config.py file and paste your git access token(Which you would have done separately)
python manage.py runserver #  to start the server locally
python manage.py test #  to run test  locally

open a new terminal and curl to your repo
curl -H 'Accept: application/json' 'http://localhost:8000/issues/?repo=LibreTime/libretime'
