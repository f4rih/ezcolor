
# ezcolor

A lightweight lib for adding extra attributes to text

## Installation

```
git clone https://github.com/0x0ptim0us/ezcolor.git
cd ezcolor
python setup.py install
```
OR:
```
pip3 install ezcolor
```

## Simple Usage

```python
from ezcolor import Style
# create style object
style = Style()
# create your own style
cp = style.add.foreground('green').apply()
cp('hello world')
```

Screenshot: 
![alt text](https://github.com/0x0ptim0us/images/raw/master/ezcolor_simple_output.png "ezcolor v2 simple")

## Adding more attribute

```python
cp = style.add.foreground('green').background('dark_gray').bold.italic.underline.apply()
cp('hello world')
```

Screenshot: 
![alt text](https://github.com/0x0ptim0us/images/raw/master/ezcolor_more_attribute.png "ezcolor v2 more")

## Adding prefix for beautiful logging

```python
cp = style.add.foreground('green').prefix('done').bold.italic.apply()
cp('Job is done!')
cp_error = style.add.foreground('red').prefix('error').bold.italic.apply()
cp_error('Error occurred!')
```

Screenshot: 
![alt text](https://github.com/0x0ptim0us/images/raw/master/ezcolor_prefix_done.png "ezcolor v2 prefix_done")
![alt text](https://github.com/0x0ptim0us/images/raw/master/ezcolor_prefix_error.png "ezcolor v2 prefix_error")

## Supported colors

| Foreground and Background|
| ------------- |
|black| 
|red| 
|green|
|yellow|
|blue|
|magenta|
|cyan|
|light_gray|
|dark_gray|
|light_red|
|light_green|
|light_yellow|
|light_blue|
|light_magenta|
|light_cyan|
|white|


| Prefix|
| ------------- |
|done|
|info| 
|error| 
|warning|
 
## Credits

Author : Fardin Allahverdinazhand

## License

Copyright 2017-2019 EZCOLOR

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ezcolor), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

