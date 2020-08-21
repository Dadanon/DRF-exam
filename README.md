A simple app containing RESTful API with `swagger` and `docs`.

**Here are the main urls:**

`127.0.0.1:8000/docs` - API documentation

`127.0.0.1:8000/swagger` - API online _`interactive`_ scheme

Instruction for local development:

`git clone https://github.com/dadanon/drf-exam.git` - Copy project to your compuer

`cd drf-exam` - Go to the project folder

`pipenv install` - Install all dependencies

##### If it has an error `failed to create virtual environment` - #####
##### copy `Pipfile` information, delete `Pipfile` and `Pipfile.lock`, #####
##### run `pipenv shell` and copy pipfile content into newly created pipfile. #####
 

`pipenv shell` - Enter the virtual environment

`python manage.py runserver` - RUN!