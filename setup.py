import os

from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(ROOT, 'README.rst')).read()
CHANGELOG = open(os.path.join(ROOT, 'CHANGELOG.rst')).read()

setup(
    name='promflask',
    version='0.0.1',
    description='Web development made easy',
    long_description=README + '\n\n' + CHANGELOG,
    # Get classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    # classifiers=[c.strip() for c in """
    #     Development Status :: 4 - Beta
    #     License :: OSI Approved :: MIT License
    #     Operating System :: OS Independent
    #     Programming Language :: Python :: 2.6
    #     Programming Language :: Python :: 2.7
    #     Programming Language :: Python :: 3
    #     Topic :: Software Development :: Libraries :: Python Modules
    #     """.split('\n') if c.strip()],
    # ],
    keywords='',
    author='Marco Chomut "Pewpewarrows"',
    author_email='marco.chomut@gmail.com',
    url='http://prometheus-kiln.com/',
    license='MIT',  # TODO: 'LICENSE.txt' instead?
    packages=find_packages('promflask'),
    package_dir={'': 'promflask'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    tests_require=[
        'nose',
    ],
)
