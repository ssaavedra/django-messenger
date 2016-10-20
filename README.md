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


Preparing for deployment
========================

The development process expects node running in the background, so
that hot patches to React files can be propgated to the browser
immediately. However, that is preferrably not wanted on a formal
deployment. In that case, run:

    npm run build

That will create a bundle bundle in assets/bundles. Now you can run
./manage.py runserver or whichever delopyment method you use on your
server.

Keep in mind you need to access the static files at /bundles, /static
and so on in order to enjoy the full functionality. To make it easy,
Django is configured to serve those files too, in case you don't put a
frontend server.


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

