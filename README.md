# ezcolor

A lightweight lib for adding extra attributes to text

## Installation

```text
git clone https://github.com/0x0ptim0us/ezcolor.git
cd ezcolor
python setup.py install
```
OR:
```text
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

| Foreground and Background |
| ------------------------- |
| black                     | 
| red                       | 
| green                     |
| yellow                    |
| blue                      |
| magenta                   |
| cyan                      |
| light_gray                |
| dark_gray                 |
| light_red                 |
| light_green               |
| light_yellow              |
| light_blue                |
| light_magenta             |
| light_cyan                |
| white                     |


| Prefix   |
| ---------|
| done     |
| info     | 
| error    | 
| warning  |
 
## Credits

Author : Fardin Allahverdinazhand

## License

MIT