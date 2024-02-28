from setuptools import setup

python_classifiers = ['Programming Language :: Python :: %s' % version for version in ['3.12', '3.13']]

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='pyasyncore',
    version='1.0.4',
    description='Make asyncore available for Python 3.12 onwards',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Simon Robinson',
    author_email='simon@robinson.ac',
    url='https://github.com/simonrob/pyasyncore',

    platforms='any',
    packages=['asyncore'],

    license='Python Software Foundation License Version 2',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: Python Software Foundation License'] + python_classifiers,
)
