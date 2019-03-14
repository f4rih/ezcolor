from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'pypi-readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	name='ezcolor',
	long_description=long_description,
	long_description_content_type='text/markdown',
	packages=['ezcolor'],
	version='0.4',
	description='A lightweight lib for adding extra attributes to text',
	author='Fardin Allahverdinazhand',
	author_email='0x0ptim0us@gmail.com',
	url='https://github.com/0x0ptim0us/ezcolor',
	download_url='https://github.com/0x0ptim0us/ezcolor/archive/0.4.tar.gz',
	keywords=['python3', 'colorize', 'ezcolor', 'output attribute', 'output colorize', 'text color', 'color'],
	classifiers=[],
)
