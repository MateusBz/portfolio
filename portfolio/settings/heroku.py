import environ

from portfolio.settings.base import *

env = environ.Env(DEBUG=(bool, False))

DEBUG = env('DEBUG')

SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': env.db(),
}