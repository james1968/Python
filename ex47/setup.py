try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Ex 47',
        'author': 'James Baker',
        'url': 'URL to get it at.',
        'download_url': 'Where to download it.',
        'author_email': 'My email.',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex47'],
        'scripts': [],
        'name': 'ex47'
}


setup(**config)

