# -*- coding: utf-8 -*-
"""
Colour Blindness Plotting
=========================

Defines the colour blindness plotting objects:

-   :func:`cvd_simulation_Machado2009_plot`
"""

from __future__ import division

from colour.blindness import cvd_matrix_Machado2009
from colour.plotting import DEFAULT_PLOTTING_ENCODING_CCTF, image_plot
from colour.utilities import dot_vector

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['cvd_simulation_Machado2009_plot']


def cvd_simulation_Machado2009_plot(RGB,
                                    deficiency='Protanomaly',
                                    severity='0.5',
                                    M_a=None,
                                    **kwargs):
    """
    Parameters
    ----------
    RGB : array_like
        *RGB* colourspace array.
    deficiency : unicode, optional
        {'Protanomaly', 'Deuteranomaly', 'Tritanomaly'}
        Colour blindness / vision deficiency type.
    severity : numeric, optional
        Severity of the colour vision deficiency in domain [0, 1].
    M_a : array_like, optional
        Anomalous trichromacy matrix to use instead of Machado (2010)
        pre-computed matrix.
    \*\*kwargs : \*\*
        Keywords arguments.

    Notes
    -----
    -   *RGB* input array is expected to represent *linear* values.

    Returns
    -------
    bool
        Definition success.

    Examples
    --------
    >>> import numpy as np
    >>> RGB = np.random.rand(32, 32, 3)
    >>> cvd_simulation_Machado2009_plot(RGB)   # doctest: +SKIP
    True
    """

    if M_a is None:
        M_a = cvd_matrix_Machado2009(deficiency, severity)

    label = 'Deficiency: {0} - Severity: {1}'.format(deficiency, severity)

    settings = {'label': None if M_a is None else label}
    settings.update(kwargs)

    return image_plot(
        DEFAULT_PLOTTING_ENCODING_CCTF(dot_vector(M_a, RGB)), **settings)
