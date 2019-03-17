ezcolor
========

.. image:: https://api.codacy.com/project/badge/Grade/5384da344156447daa23f588fc8fbae6
        :target: https://app.codacy.com/app/0x0ptim0us/ezcolor?utm_source=github.com&utm_medium=referral&utm_content=0x0ptim0us/ezcolor&utm_campaign=Badge_Grade_Dashboard

Python colorizing strings library

A lightweight library for applying color and HTML text styles to the strings
that uses the builder pattern for configuration. The ezcolor lets you have nice
colorized output with extra HTML text styles like bold/italic/underline.
compatible with bash/sh/zsh.

Features
--------
- A simple to use API
- lightweight and written in pure python
- Tested on python 3.6+ (not compatible with python2.x)
- Not compatible with windows OS (command prompt, powershell)

Usage
--------

.. code-block:: bash

 $ pip install ezcolor

.. code-block:: python

 from ezcolor import Style
 style = Style()
 cp = style.add.foreground('green').apply()
 cp('hello world')

.. image:: https://github.com/0x0ptim0us/images/raw/master/ezcolor_simple_output.png

Adding more attributes
----------------------

.. code-block:: python

 cp = style.add.foreground('green').background('dark_gray').bold.italic.underline.apply()
 cp('hello world')

.. image:: https://github.com/0x0ptim0us/images/raw/master/ezcolor_more_attribute.png

Adding prefix for beautiful logging
-----------------------------------

.. code-block:: python

 cp = style.add.foreground('green').prefix('done').bold.italic.apply()
 cp('Job is done!')
 cp_error = style.add.foreground('red').prefix('error').bold.italic.apply()
 cp_error('Error occurred!')

.. image:: https://github.com/0x0ptim0us/images/raw/master/ezcolor_prefix_done.png
.. image:: https://github.com/0x0ptim0us/images/raw/master/ezcolor_prefix_error.png

Use as decorator
----------------

.. code-block:: python

 @cp.decorate
 def my_name(name, lastname):
     return f"my name is {name} {lastname}"

 print(my_name('Fardin', 'Allahverdinazhand'))

.. csv-table:: Supported colors and prefix (log level)
    :header: "Color", "prefix"
    :widths: 20, 20

    "black", "done"
    "red", "info"
    "green", "warning"
    "yellow", "error"
    "blue",
    "magenta",
    "cyan",
    "light_gray",
    "dark_gray",
    "light_red",
    "light_green",
    "light_yellow",
    "light_blue",
    "light_magenta",
    "light_cyan",
    "white",

Meta
----
Fardin Allahverdinazhand - `@0x0ptim0us <https://twitter.com/0x0ptim0us>`_  - 0x0ptim0us@gmail.com
Distributed under the MIT license. see `LICENSE.txt <https://github.com/0x0ptim0us/ezcolor/blob/master/LICENSE.txt>`_ for more information.

https://github.com/0x0ptim0us/ezcolor