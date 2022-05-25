
from os.path import join, dirname
from json import load


__VERSION__ = '0.0.1'
__BRANCH__ = 'heroku'
__CONFIG__ = 'config.json'

with open(join(dirname(__file__), __CONFIG__), 'r') as file:
    CONFIG = load(file)
