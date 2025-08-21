release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn <ИМЯ_ТВОЕГО_МОДУЛЯ>.wsgi:application --bind 0.0.0.0:$PORT
