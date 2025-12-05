FROM python:3.13-alpine
LABEL authors="Robert Jauss"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV DJANGO_SUPERUSER_EMAIL=robert@jauss.dev
ENV DJANGO_SUPERUSER_USERNAME=demouser
ENV DJANGO_SUPERUSER_PASSWORD=demouser

RUN python manage.py migrate
RUN python manage.py loaddata fixtures/default_data.json
RUN python manage.py createsuperuser --noinput

CMD ["gunicorn", "-k", "gthread", "--bind", "0.0.0.0:8000", "AidasTasks.wsgi:application"]