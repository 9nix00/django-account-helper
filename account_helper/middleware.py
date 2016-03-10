# -*- coding: utf-8 -*-

from threading import local

_user = local()


class CurrentUserMiddleware(object):
    def process_request(self, request):
        _user.value = request.user


def get_current_user():
    return _user.value if hasattr(_user, 'value') else None


def get_current_user_id():
    return _user.value.id if hasattr(_user, 'value') else 0
