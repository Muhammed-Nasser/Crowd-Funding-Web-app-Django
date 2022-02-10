# CrowdFunding App

## Installation

1. Start a virtual environment

   - "venv"

   ```bash
   c
   $ pip3 install virtualenv
   $ python3 -m venv env
   $ source env/bin/activate

   $ deactivate # to exit from it
   ```

   - you can also use "pipenv" **[recommended]**

   ```bash
    c
   $ pip3 install pipenv
   $ pipenv install #to install the required depenedencies
   $ pipenv shell # to enter the virtual envirornment

   $ exit # to exit from the environment
   ```

2. Run the django app

   ```bash
   python3 manage.py runserver [port]
   ```

___

## Technologies

- Django Framework
- Django Rest-Framework
