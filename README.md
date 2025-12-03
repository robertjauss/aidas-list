Aida's List - aidaslist.xyz
===================

Overview
--------

A task tracking web app, built for simplicity. Originally designed to help a long-time client who needs computer assistance
every now and then to keep track of what she needs help with, letting me see what tasks she has for me before we even connect.

Technologies Used
------------------

- Python
- Django
- Web Awesome component library
- Docker
- Docker Compose

Getting Started
---------------

- Local development
  1. Ensure Python is installed
  2. Clone the repository: `git clone <repository_url>`
  3. Navigate to the project directory and create a virtual environment: `python -m venv venv && source venv/bin/activate`
  4. Install the project's dependencies: `pip install -r requirements.txt`
  5. Start the development server: `python manage.py runserver`
- Production deployment
  1. Clone repo
  2. Build docker image: `docker build -t aidaslist .`
  3. Start container: `docker run -d aidaslist`
  4. Point web server (NGINX, Apache, etc.) at localhost:8000

License
-------

This project is licensed under [Apache-2.0 license](LICENSE).