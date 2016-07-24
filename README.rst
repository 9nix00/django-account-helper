django account helper
==========================================

django account helper utils  for `django.contrib.auth`


Requirement
-----------------------------

* Django1.8+



Install
-----------------------------------

.. code-block::

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

.. code-block::

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)


after

.. code-block::

    from account_helper.middleware import get_current_user

    # ... fields definition...

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, default=get_current_user, null=True)





set current user id as default value
#########################################


update your model like this:

before

.. code-block::

    owner = models.IntegerField('user id')


after

.. code-block::

    from account_helper.middleware import get_current_user_id

    # ... fields definition...

    owner = models.IntegerField('user id',default=get_current_user_id)





use session in form
#########################################


sometimes we really need handle session in form. but in django. we have to do something like this.

old style
-----------------

1. in your views. set `get_form_kwargs`

.. code-block::

    class YourFormView(FormView):
        form_class=YourForm
        def get_form_kwargs(self):
            return {'request':self.request}
            pass

        pass


2.set your form.

.. code-block::

    Class YourForm(forms.Form):
        request = None

        def __init__(self,*args,**kwargs):
            self.request = kwargs.get('request')
            if 'request' in kwargs:
                del kwargs['request']
            super (YourForm,self).__init__(*args,**kwargs)



do it in django-account-helper
-------------------------------------

.. code-block::

    from account_helper.middleware import get_current_session

    Class YourForm(forms.Form):

        def clean(self):
            session = get_current_session()
            if self.cleaned_data.get('foo') == session.get('foo'):
                # do something
                pass

            #... your code
        pass



create need authorized classed-view
#########################################

.. code-block::

    from account_helper.mixins import LoginDispatchMixin

    class GenericListingView(LoginDispatchMixin, TemplateView):
        template_name = 'accounts/profile.html'
        pass




