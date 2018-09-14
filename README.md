# localWiki

Description
It's a local wiki clone, that is getting data from online wikipedia for the first search.
after the first search, it stores searched keyword in localDB, so next search for same item will be fast.

Installation instruction
1) install python 3.6 and virtualenv
2) mkdir localWiki
3) virtualenv -p python3.6 venv
4) clone git repo - 
	git clone https://github.com/Shapboyz13/localWiki.git
5) activate virtual env from localWiki(project Directory) dir- 
	. ./venv/bin/activate

6) change to cloned dir
7) install all dependency of project
	pip install -r requirements.txt
8) once, installed. start server with below command
	python manage.py runserver
9) viola.... 

API :

start server with default port or port of your choice

Default

python manage.py runserver


or on port xxxx
python manage.py runserver xxxx

then hit API -

localhost:port<xxxx/8000(default)>/get/<searchkeyword>

e.g.

localhost:8000/get/wikipedia


return status :- 
code = 0	: No Data
code = 1	: Coming from Local DB
code = 2	: Coming from wikipedia
code = 3	: Suggestions, too many option to search
