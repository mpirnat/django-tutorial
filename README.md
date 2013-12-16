django-tutorial
===============

This repository contains the code for the "Web Development with Python and
Django" tutorial session run by Mike Pirnat and David Stanek.

In this tutorial we'll build a full-featured website step by step using the
Django web framework.

Getting Started
---------------

If you're attending the tutorial in person, **please** make sure you install
these prerequisites **before the class begins** so that we can make the most of
our time together in the session.  You and your fellow attendees will thank you
for your preparedness!

You'll need to install:

 1. [Python][python]

  Django is written in the Python programming language; you'll need to install
  Python in order to make anything work.

  You should install either Python 2.7 or Python 3.3.

 2. [Git][git]

  You will need the Git version control system in order to work with the
  exercises in this repository.  If you're new to Git, don't panic--we won't be
  doing anything too weird, and we'll walk through all of it in the session.

 3. [Pip][pip]

  Pip is a tool for installing Python packages.  You will need it to install
  the Python dependencies for this tutorial.

 4. [Virtualenv][virtualenv]

  Virutalenv is a tool for creating isolated Python environments on your
  system.  This allows you to work on multiple projects that might have
  conflicts in the versions of libraries they depend on.  It also keeps your
  base system installation of Python nice and clean.

Once you have installed these basics, let's get the working environment set up
for the project.

 1. Create a new virtual environment ("virtualenv") and activate it

 On Linux or Mac OS X:

    $ virtualenv django-precompiler
    $ cd django-precompiler
    $ source bin/activate

 On Windows:

    > python virtualenv django-precompiler
    > cd django-precompiler
    > Scripts/activate.bat

 2. Clone this repository

 In the django-precompiler directory from the previous step:

    $ git clone https://github.com/mpirnat/django-tutorial.git ./src

 3. Install Django and any other Python dependencies

 In the django-precompiler directory from the previous step:

    $ cd src
    $ pip install -r requirements.txt

 4. Check to make sure everything's in good shape

 In the src directory from the previous step:

    $ python prerequisites.py

 5. Rewind the repository to the start of our exercises

 In the src directory form the previous step:

    $ git reset --hard ex00


[python]: http://python.org/download/
[git]: http://git-scm.com
[pip]: http://www.pip-installer.org/en/latest/installing.html
[virtualenv]: http://www.virtualenv.org/en/latest/virtualenv.html
