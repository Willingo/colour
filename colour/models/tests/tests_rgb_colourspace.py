#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**tests_rgb_colourspace.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines units tests for :mod:`colour.models.rgb_colourspace` module.

**Others:**

"""

from __future__ import unicode_literals

import sys

if sys.version_info[:2] <= (2, 6):
    import unittest2 as unittest
else:
    import unittest

from colour.models import RGB_Colourspace

__author__ = "Colour Developers"
__copyright__ = "Copyright (C) 2013 - 2014 - Colour Developers"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Colour Developers"
__email__ = "colour-science@googlegroups.com"
__status__ = "Production"

__all__ = ["TestRGB_Colourspace"]


class TestRGB_Colourspace(unittest.TestCase):
    """
    Defines :class:`colour.colour.models.RGB_Colourspace` class units
    tests methods.
    """

    def test_required_attributes(self):
        """
        Tests presence of required attributes.
        """

        required_attributes = ("name",
                               "primaries",
                               "whitepoint",
                               "to_XYZ",
                               "from_XYZ",
                               "transfer_function",
                               "inverse_transfer_function",)

        for attribute in required_attributes:
            self.assertIn(attribute, dir(RGB_Colourspace))


if __name__ == "__main__":
    unittest.main()
