debian-virtualenv-skeleton
==========================

Skeleton for debian python packages, using virtualenv for deployment (e.g. django projects)

What do we have here?
---------------------

This is a collection of a debian control files with a Makefile script that helps you to create debian packages
for your python projects (especially Django) which are distributed in a separate virtualenv's.

This script uses brilliant [dh-virtualenv](https://github.com/spotify/dh-virtualenv) written by spotify team.

How to use it?
--------------

First of all you should check Makefile and set `PROJECT` package to the name of your django project (or leave it as-is) and *change* `PACKAGE` to the name of your debian package.

You can use pre-created Django project structure with a project name "project" or create your own project under `project` directory.

Then you should update `debian/changelog` with the information about changes in your package and relevant version and set the same version in `VERSION` in Makefile.

After that type:

   make builddeb

This should update control files in `debian` directory with correct project and package name and start the process of packaging. If it is successfull you should see your brand new package in the parent directory.

What should it do?
------------------

Installation scripts prepare a new directory for your package in `/var/lib/<your-package>` with `virtualenv` installed. After that your project is unpacked into `/var/lib/<your-package>/project` and all the files under `docs` directory are unpacked to `/usr/share/doc/<your-package>`. Then `/usr/share/doc/<your-pacjkage>/requirements.txt` file is processed to install necessary dependencies into your virtual environment (you should update them in `docs/requirements.txt` when needed). By default it installs Django and South (database migration tool).

If it happens that you are using uwsgi then installation script will create `reload` file in  `/var/lib/<your-package>` to signal that project is updated.

Directory structure
-------------------
 * root directory contains setup.py and requirements file
 * `debian` directory contains all the needed initial debian scripts. You should only update `changelog` file here.
 If you want to add custom logic to install scripts see `preinst`, `postinst` or `prerm` files.
 * `docs` contains example uwsgi and Apache2 WSGI configuration for your project
 * `project` is where your django project should be. Example project is created with Django 1.6.1 and has `settings.py` set to import `local_settings.py` which is treated as configuration file (so it would not be rewritten with new installation). If you intend to recreate project, you should take care of updating default `settings.py` with the same logic.
