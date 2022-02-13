.PHONY: setup
setup:
	pip install -r requirements.freeze.txt
	cd src && python manage.py migrate --settings=flamingo.settings
	cd src && python manage.py loaddata flamingo/fixtures/*.json
	cd src && python manage.py createsuperuser
        
.PHONY: server
server:
	cd src && python manage.py runserver --settings=flamingo.settings

.PHONY: test
test:
	cd src && python manage.py test --settings=flamingo.settings

.PHONY: gen-migrate
gen-migrate:
	cd src && python manage.py makemigrations

.PHONY: do-migrate
do-migrate:
	cd src && python manage.py migrate --settings=flamingo.settings

.PHONY: pip-freeze
pip-freeze:
	pip freeze > requirements.freeze.txt

