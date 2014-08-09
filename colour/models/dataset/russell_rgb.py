#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**russell_rgb.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines **Colour** package *Russell RGB* colourspace.

**Others:**

"""

from __future__ import unicode_literals

import numpy as np

from  colour.colorimetry.dataset import ILLUMINANTS
from colour.models import RGB_Colourspace, get_normalised_primary_matrix

__author__ = "Colour Developers"
__copyright__ = "Copyright (C) 2013 - 2014 - Colour Developers"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Colour Developers"
__email__ = "colour-science@googlegroups.com"
__status__ = "Production"

__all__ = ["RUSSELL_RGB_PRIMARIES",
           "RUSSELL_RGB_WHITEPOINT",
           "RUSSELL_RGB_TO_XYZ_MATRIX",
           "XYZ_TO_RUSSELL_RGB_MATRIX",
           "RUSSELL_RGB_TRANSFER_FUNCTION",
           "RUSSELL_RGB_INVERSE_TRANSFER_FUNCTION",
           "RUSSELL_RGB_COLOURSPACE"]

# http://www.russellcottrell.com/photo/RussellRGB.htm
RUSSELL_RGB_PRIMARIES = np.array(
    [0.6900, 0.3100,
     0.1800, 0.7700,
     0.1000, 0.0200]).reshape((3, 2))

RUSSELL_RGB_WHITEPOINT = ILLUMINANTS.get(
    "CIE 1931 2 Degree Standard Observer").get("D55")

RUSSELL_RGB_TO_XYZ_MATRIX = get_normalised_primary_matrix(
    RUSSELL_RGB_PRIMARIES, RUSSELL_RGB_WHITEPOINT)

XYZ_TO_RUSSELL_RGB_MATRIX = np.linalg.inv(RUSSELL_RGB_TO_XYZ_MATRIX)

RUSSELL_RGB_TRANSFER_FUNCTION = lambda x: x ** (1 / 2.2)

RUSSELL_RGB_INVERSE_TRANSFER_FUNCTION = lambda x: x ** 2.2

RUSSELL_RGB_COLOURSPACE = RGB_Colourspace(
    "Russell RGB",
    RUSSELL_RGB_PRIMARIES,
    RUSSELL_RGB_WHITEPOINT,
    RUSSELL_RGB_TO_XYZ_MATRIX,
    XYZ_TO_RUSSELL_RGB_MATRIX,
    RUSSELL_RGB_TRANSFER_FUNCTION,
    RUSSELL_RGB_INVERSE_TRANSFER_FUNCTION)
