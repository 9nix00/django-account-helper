# -*- coding: utf-8 -*-


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


class LoginDispatchMixin(object):
    @method_decorator(login_required)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(LoginDispatchMixin, self).dispatch(*args, **kwargs)

    pass
