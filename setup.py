import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()
def read_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name='languapedia',
    version='0.0.1',
    description='Languapedia',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=read_requirements(),
    entry_points={
        'paste.app_factory': [
            'main = languapedia:main',
        ],
        'console_scripts': [
            'initialize_languapedia_db=languapedia.scripts.initialize_db:main',
        ],
    },
)
