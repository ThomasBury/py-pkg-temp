import os.path
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# get key package details from pkgtemp/__version__.py
ABOUT = {}  # type: ignore
with open(os.path.join(HERE, 'pkgtemp', '__version__.py')) as f:
    exec(f.read(), ABOUT)

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

with open(os.path.join(HERE, "requirements.txt")) as req:
    REQUIREMENTS = req.read().splitlines()


EXTRAS_REQUIRE = {'plotting': ['matplotlib>=3.3.0', 'jupyter'], 'setup': ['pytest-runner', 'flake8'], 'test': ['pytest']}

KEYWORDS = "template, python, package"

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
    name=ABOUT['__title__'],
    description=ABOUT['__description__'],
    long_description=README,
    long_description_content_type='text/markdown',
    version=ABOUT['__version__'],
    author=ABOUT['__author__'],
    author_email=ABOUT['__author_email__'],
    url=ABOUT['__url__'],
    packages=['pkgtemp'],
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS_REQUIRE,
    license=ABOUT['__license__'],
    zip_safe=False,
    #package_data={'': ['data/*.png']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=KEYWORDS
)