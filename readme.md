# CrowdFunding App

Web platform for starting fundraise projects in Egypt. 

## Installation

1. Start a virtual environment

   - "venv"

   ```bash
   $ pip3 install virtualenv
   $ python3 -m venv env
   $ source env/bin/activate

   $ deactivate # to exit from it
   ```

   - you can also use "pipenv" **[recommended]**

   ```bash
   $ pip3 install pipenv
   $ pipenv install #to install the required depenedencies
   $ pipenv shell # to enter the virtual envirornment

   $ exit # to exit from the environment
   ```

2. Add ***cred.py*** file in **Django_Project** folder
   <blockquote>
      <p>DB_NAME = _your database name_ </p>
      <p>DB_USER = _your database user_ </p>
      <p>DB_PASS = _your database password_ </p>
      <br/>
      <p>EMAIL_HOST_USER = _your email_ </p>
      <p>EMAIL_HOST_PASSWORD = _your email password_ </p>
   </blockquote>
3. Migrate the models to your database
   ```bash
   $ python manage.py makemigrations
   $ python manage.p migrate
   ```
4. Run the django app

   ```bash
   python3 manage.py runserver [port]
   ```

---

## Technologies

- Django Framework
- Django-Rest Framework
