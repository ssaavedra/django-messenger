DjMessenger
===========

An instant-message tool written with Django REST Framework and React + Redux.


Before usage
============

Virtualenv
----------

First of all, you can (and should) create a virtualenv with

    python3 -m venv env     # to create a python3 environment
	source env/bin/activate # to activate it


Dependencies
------------

Then, download all Python-related dependencies with:

    pip install -r requirements.txt

After that (or at the same time), download all frontend-related dependencies with:

    npm install

Populating the database
-----------------------

For testing, create an embedded SQLite database with

    ./manage.py migrate


Running the development server
==============================

Then you can start the node frontend development server (which bundles the assets) with:

    npm run open:src

Finally, start the backend WSGI Django server with:

    ./manage.py runserver


License
=======

Copyright 2016 Santiago Saavedra Lopez. All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

