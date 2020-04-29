install_require:
	pip install -r requirements.txt

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

test:
	coverage run python manage.py test
	coverage report

run:
	python manage.py runserver
