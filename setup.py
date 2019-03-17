import codecs
from distutils.core import setup

EZCOLOR_VERSION = '0.7'
EZCOLOR_DOWNLOAD = ('https://github.com/0x0ptim0us/ezcolor/tarball/' + EZCOLOR_VERSION)

def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, 'r', 'utf8') as f:
        return f.read()


setup(
	name='ezcolor',
	packages=['ezcolor'],
	version=EZCOLOR_VERSION,
	description='A lightweight pure python library for applying color and HTML text styles to the strings',
	long_description=read_file('README.rst'),
	license='MIT',
	author='Fardin Allahverdinazhand',
	author_email='0x0ptim0us@gmail.com',
	url='https://github.com/0x0ptim0us/ezcolor',
	download_url=EZCOLOR_DOWNLOAD,
	keywords=['python3', 'colorize', 'ezcolor', 'output attribute', 'output colorize', 'text color', 'color'],
	classifiers=[
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Natural Language :: English',
	],
)
