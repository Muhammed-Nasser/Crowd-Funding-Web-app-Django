# CrowdFunding App

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
      <p>DB_NAME = <span style="color:blue;">your database name</span></p>
      <p>DB_USER = <span style="color:blue;">your database user_</span></p>
      <p>DB_PASS = <span style="color:blue;">your database password</span></p>
      <br/>
      <p>EMAIL_HOST_USER = <span style="color:blue;"> your email</span></p>
      <p>EMAIL_HOST_PASSWORD =<span style="color:blue;">your email password</span></p>
   </blockquote>
3. Run the django app

   ```bash
   python3 manage.py runserver [port]
   ```

---

## Technologies

- Django Framework
- Django-Rest Framework
