""" problem_generator

"""

from os.path import join, dirname
from json import load


__VERSION__ = '0.0.1'
__BRANCH__ = 'heroku'
__CONFIG__ = 'config.json'

METADATA_INIT = '---'

with open(join(dirname(__file__), __CONFIG__), 'r', encoding='utf-8') as file:
    CONFIG = load(file)
