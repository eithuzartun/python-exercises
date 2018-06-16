try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'My Projects',
        'author': 'My Name',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'fMy email',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['lexicon'],
        'script': [ ],
        'name': 'projectname'
        }

setup(**config)
