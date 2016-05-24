#bare-travel-api
[![Build Status](https://travis-ci.org/garybutton/bare-travel-api.svg?branch=master)](https://travis-ci.org/garybutton/bare-travel-api)

Django REST API. Check out the project's [documentation](http://garybutton.github.io/bare-travel-api/).

# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [postgresql](http://www.postgresql.org/)
- [redis](http://redis.io/)
- [travis cli](http://blog.travis-ci.com/2013-01-14-new-client/)
- [heroku toolbelt](https://toolbelt.heroku.com/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements/local.txt
```
Create the database:

```bash
createdb bare-travel
```
Initialize the git repository

```
git init
git remote add origin git@github.com:garybutton/bare-travel-api.git
```

Migrate, create a superuser, and run the server:
```bash
python bare-travel/manage.py migrate
python bare-travel/manage.py createsuperuser
python bare-travel/manage.py runserver
```

# Create Servers
By default the included fabfile will setup three environments:

- dev -- The bleeding edge of development
- qa -- For quality assurance testing
- prod -- For the live application

Create these servers on Heroku with:

```bash
fab init
```

# Automated Deployment
Deployment is handled via Travis. When builds pass Travis will automatically deploy that branch to Heroku. Enable this with:
```bash
travis encrypt $(heroku auth:token) --add deploy.api_key
```
