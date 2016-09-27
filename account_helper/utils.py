# -*- coding: utf-8 -*-

import random
import string


def create_cipher(length=6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
