try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description' : 'My Project',
    'author' : 'Elijah DeLee',
    'download_url' : 'https://github.com/deleeke/',
    'author_email' : 'deleek@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['Nightmare']
    'scripts' : [],
    'name' : 'Nightmare(): The Game'
]

setup(**config)
