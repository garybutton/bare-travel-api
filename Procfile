web: newrelic-admin run-program gunicorn --pythonpath="$PWD/bare-travel" wsgi:application
worker: python bare-travel/manage.py rqworker default