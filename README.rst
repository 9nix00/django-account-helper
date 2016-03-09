django_account_helper
==========================================

django account helper utils  for `django.contrib.auth`


Requirement
-----------------------------

* Django



Install
-----------------------------------

...code::

    pip install django_acocunt_helper




Config
---------------------------------


1. check your settings.py, make sure `django.contrib.auth` in INSTALLED_APPS.

2. add `account_helper.middleware.CurrentUserMiddleware`


config finish.


How to use
-------------------------------


set current user as default value
#####################################


update your model like this:

before
...code::

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)


after
...code::

    from account_helper.middleware import get_current_user

    ... fileds definition...

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=get_current_user)


































