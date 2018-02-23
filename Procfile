web: gunicorn config.wsgi:application
worker: celery worker --app=simple_file_uploader.taskapp --loglevel=info
