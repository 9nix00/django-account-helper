from setuptools import find_packages, setup

import account_helper

setup(
    name='django-account-helper',
    version=account_helper.version,
    packages=find_packages(exclude=["tests"]),
    # install_requires=['django'],
    url='https://github.com/9nix00/django-account-helper',
    license='http://opensource.org/licenses/MIT',
    download_url='https://github.com/9nix00/django-account-helper/archive/master.zip',
    include_package_data=True,
    author='wangwenpei',
    author_email='wangwenpei@nextoa.com',
    description='django account helper utils for `django.contrib.auth`',
    keywords='django_account_helper,',
)

