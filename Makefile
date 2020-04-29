install_require:
	pip install -r requirements/requirements.txt

install_test:
	python -m pip install --upgrade pip
	pip install -r requirements/requirements-test.txt

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

test:
	python manage.py test

coverage:
	coverage run manage.py test
	coverage report

run:
	python manage.py runserver
