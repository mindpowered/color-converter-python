
colorconverter
==============
Converter to convert between various color systems such as RGB, CIELAB, CMYK, HEX, RGB, and XYZ

![Build Status](https://mindpowered.dev/assets/images/github-badges/build-passing.svg)

Contents
========

* [Source Code and Documentation](#source-code-and-documentation)
* [About](#about)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Support](#support)
* [Licensing](#licensing)

# Source Code and Documentation
- Source Code: [https://github.com/mindpowered/color-converter-python](https://github.com/mindpowered/color-converter-python)
- Documentation: [https://mindpowered.github.io/color-converter-python](https://mindpowered.github.io/color-converter-python)

# About
Defining a color is difficult. The first challenge is finding a way to describe a color. One way is to describe color based on constituent colors. We can describe constituent colors by adding them, like in RGB, or subtracting them, like in CMYK. Gamut is the range of all colors that are representable in a color system. RGB trades a limited gamut for performance. LAB trades performance for the full gamut of visible colors. CMYK represents the gamut used in color printing.

The second challenge to defining a color is that it depends on the observer. Viewing the same color will look different when:
- printed on paper or displayed on a screen
- seen in daylight or under fluorescent lighting
- positioned at a close or far distance
Standard references such as the Pantone Matching System refer to specific colors. We lose information when converting from a reference color to a color system. Printing or rendering an RGB or CMYK color equivalent to a reference color may not match. We can avoid information loss during conversion by using an unlimited gamut such as LAB. We must also take into account the effect of the observer and illumination.

This package aims to provide tools to perform:
- Color conversion between color systems
- A way of searching for similar standardized reference colors

# Requirements
- Requires Python 3.x. Due to security fixes and new features Python 3.7 or later is recommended.
- pip


Third-party dependencies may have additional requirements.

# Installation
You can retrieve the colorconverter package from the Python Package Index https://pypi.org/ using pip. First make sure you have python3 and python3-pip installed. Then you can start by making a `requirements.txt` file in your working directory with the colorconverter requirement in it. You can add any other packages to your requirements here, each as a separate line.

requirements.txt:
```
mindpowered-colorconverter>0
```
Now you can use pip to install the colorconverter package: `python3 -m pip install -r requirements.txt`
If you would like to update the package, simply run the above command again.


# Usage
```python
from mindpowered_colorconverter import *

cc = ColorConverter()
colors = cc.FromHEX("#336699")

```


# Support
We are here to support using this package. If it doesn't do what you're looking for, isn't working, or you just need help, please [Contact us][contact].

There is also a public [Issue Tracker][bugs] available for this package.

# Licensing
This package is released under the MIT License.



[bugs]: https://github.com/mindpowered/color-converter-python/issues
[contact]: https://mindpowered.dev/support/?ref=color-converter-python/
[docs]: https://mindpowered.github.io/color-converter-python/
[licensing]: https://mindpowered.dev/?ref=color-converter-python
[purchase]: https://mindpowered.dev/purchase/
