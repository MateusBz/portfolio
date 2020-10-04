import environ

from portfolio.settings.base import *

env = environ.Env(DEBUG=(bool, True))

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': env.db(),
}