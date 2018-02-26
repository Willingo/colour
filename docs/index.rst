Colour Science for Python
=========================

..  image:: _static/Logo_Medium_001.png

`Colour <https://github.com/colour-science/colour>`_ is a
`Python <https://www.python.org/>`_ colour science package implementing a
comprehensive number of colour theory transformations and algorithms.

It is open source and freely available under the
`New BSD License <http://opensource.org/licenses/BSD-3-Clause>`_ terms.

Features
--------

`Colour <https://github.com/colour-science/colour>`_ features a rich dataset
and collection of objects, please see the
`features <http://colour-science.org/features/>`_ page for more information.

Installation
------------

`Anaconda <https://www.continuum.io/downloads>`_ from *Continuum Analytics*
is the Python distribution we use to develop **Colour**:
it ships all the scientific dependencies we require and is easily deployed
cross-platform:

.. code-block:: bash

    $ conda create -y -n python-colour
    $ source activate python-colour
    $ conda install -y -c conda-forge colour-science

**Colour** can be easily installed from the `Python Package Index <https://pypi.python.org/pypi/colour-science/>`_ by issuing this command in a shell:

.. code-block:: bash

    $ pip install colour-science

The detailed installation procedure is described in the
`Installation Guide <http://colour-science.org/installation-guide/>`_.

Usage
-----

The two main references for `Colour <https://github.com/colour-science/colour>`_
usage are the `Colour Manual <https://colour.readthedocs.io/en/latest/manual.html>`_
and the `Jupyter Notebooks <http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/blob/master/notebooks/colour.ipynb>`_
with detailed historical and theoretical context and images.

.. toctree::
    :maxdepth: 4

    manual

Examples
~~~~~~~~

Chromatic Adaptation
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> XYZ = [0.07049534, 0.10080000, 0.09558313]
    >>> A = colour.ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['A']
    >>> D65 = colour.ILLUMINANTS['CIE 1931 2 Degree Standard Observer']['D65']
    >>> colour.chromatic_adaptation(
    ...     XYZ, colour.xy_to_XYZ(A), colour.xy_to_XYZ(D65))
    array([ 0.08398225,  0.11413379,  0.28629643])
    >>> sorted(colour.CHROMATIC_ADAPTATION_METHODS.keys())
    ['CIE 1994', 'CMCCAT2000', 'Fairchild 1990', 'Von Kries']

Algebra
^^^^^^^

Kernel Interpolation
********************

.. code-block:: python

    >>> import colour
    >>> y = [5.9200, 9.3700, 10.8135, 4.5100, 69.5900, 27.8007, 86.0500]
    >>> x = range(len(y))
    >>> colour.KernelInterpolator(x, y)([0.25, 0.75, 5.50])
    array([  6.18062083,   8.08238488,  57.85783403])

Sprague (1880) Interpolation
****************************

.. code-block:: python

    >>> import colour
    >>> y = [5.9200, 9.3700, 10.8135, 4.5100, 69.5900, 27.8007, 86.0500]
    >>> x = range(len(y))
    >>> colour.SpragueInterpolator(x, y)([0.25, 0.75, 5.50])
    array([  6.72951612,   7.81406251,  43.77379185])

Spectral Computations
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> colour.spectral_to_XYZ(colour.LIGHT_SOURCES_RELATIVE_SPDS['Neodimium Incandescent'])
    array([ 36.94726204,  32.62076174,  13.0143849 ])
    >>> sorted(colour.SPECTRAL_TO_XYZ_METHODS.keys())
    [u'ASTM E308-15', u'Integration', u'astm2015']

Blackbody Spectral Radiance Computation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> colour.blackbody_spd(5000)
    SpectralPowerDistribution([[  3.60000000e+02,   6.65427827e+12],
                               [  3.61000000e+02,   6.70960528e+12],
                               [  3.62000000e+02,   6.76482512e+12],
                               ...
                               [  7.78000000e+02,   1.06068004e+13],
                               [  7.79000000e+02,   1.05903327e+13],
                               [  7.80000000e+02,   1.05738520e+13]],
                              interpolator=SpragueInterpolator,
                              interpolator_args={},
                              extrapolator=Extrapolator,
                              extrapolator_args={u'right': None, u'method': u'Constant', u'left': None})

Dominant, Complementary Wavelength & Colour Purity Computation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> xy = [0.26415, 0.37770]
    >>> xy_n = [0.31270, 0.32900]
    >>> colour.dominant_wavelength(xy, xy_n)
    (array(504.0),
     array([ 0.00369694,  0.63895775]),
     array([ 0.00369694,  0.63895775]))

Lightness Computation
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> colour.lightness(10.08)
    24.902290269546651
    >>> sorted(colour.LIGHTNESS_METHODS.keys())
    [u'CIE 1976',
     u'Fairchild 2010',
     u'Glasser 1958',
     u'Lstar1976',
     u'Wyszecki 1963']

Luminance Computation
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> colour.luminance(37.98562910)
    10.080000001314646
    >>> sorted(colour.LUMINANCE_METHODS.keys())
    [u'ASTM D1535-08',
     u'CIE 1976',
     u'Fairchild 2010',
     u'Newhall 1943',
     u'astm2008',
     u'cie1976']

Whiteness Computation
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> colour.whiteness(xy=[0.3167, 0.3334], Y=100, xy_n=[0.3139, 0.3311])
    array([ 93.85 ,  -1.305])
    >>> sorted(colour.WHITENESS_METHODS.keys())
    [u'ASTM E313',
     u'Berger 1959',
     u'CIE 2004',
     u'Ganz 1979',
     u'Stensby 1968',
     u'Taube 1960',
     u'cie2004']

Yellowness Computation
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> XYZ = [95.00000000, 100.00000000, 105.00000000]
    >>> colour.yellowness(XYZ)
    11.065000000000003
    >>> sorted(colour.YELLOWNESS_METHODS.keys())
    [u'ASTM D1925', u'ASTM E313']

Luminous Flux, Efficiency & Efficacy Computation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Luminous Flux
*************

.. code-block:: python

    >>> import colour
    >>> spd = colour.LIGHT_SOURCES_RELATIVE_SPDS['Neodimium Incandescent']
    >>> colour.luminous_flux(spd)
    3807.655527367202

Luminous Efficiency
*******************

.. code-block:: python

    >>> import colour
    >>> spd = colour.LIGHT_SOURCES_RELATIVE_SPDS['Neodimium Incandescent']
    >>> colour.luminous_efficiency(spd)
    0.19943935624521045

Luminous Efficacy
*****************

.. code-block:: python

    >>> import colour
    >>> spd = colour.LIGHT_SOURCES_RELATIVE_SPDS['Neodimium Incandescent']
    >>> colour.luminous_efficacy(spd)
    136.21708031547874

Colour Models
^^^^^^^^^^^^^

CIE xyY Colourspace
*******************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_xyY([0.07049534, 0.10080000, 0.09558313])
    array([ 0.26414772,  0.37770001,  0.1008    ])

CIE L*a*b* Colourspace
**********************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_Lab([0.07049534, 0.10080000, 0.09558313])
    array([ 37.9856291 , -23.62907688,  -4.41746615])

CIE L*u*v* Colourspace
**********************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_Luv([0.07049534, 0.10080000, 0.09558313])
    array([ 37.9856291 , -28.80219593,  -1.35800706])

CIE 1960 UCS Colourspace
************************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_UCS([0.07049534, 0.10080000, 0.09558313])
    array([ 0.04699689,  0.1008    ,  0.1637439 ])

CIE 1964 U*V*W* Colourspace
***************************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_UVW([0.07049534, 0.10080000, 0.09558313])
    array([ 4.0680797 ,  0.12787175, -5.36516614])

Hunter L,a,b Colour Scale
*************************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_Hunter_Lab([7.049534, 10.080000, 9.558313])
    array([ 31.74901573, -15.11462629,  -2.78660758])

Hunter Rd,a,b Colour Scale
**************************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_Hunter_Rdab([7.049534, 10.080000, 9.558313])
    array([ 10.08      , -18.67653764,  -3.44329925])

CAM02-LCD, CAM02-SCD, and CAM02-UCS Colourspaces - Luo, Cui and Li (2006)
*************************************************************************

.. code-block:: python

    >>> import colour
    >>> XYZ = np.array([19.01, 20.00, 21.78])
    >>> XYZ_w = np.array([95.05, 100.00, 108.88])
    >>> L_A = 318.31
    >>> Y_b = 20.0
    >>> surround = colour.CIECAM02_VIEWING_CONDITIONS['Average']
    >>> specification = colour.XYZ_to_CIECAM02(
            XYZ, XYZ_w, L_A, Y_b, surround)
    >>> JMh = (specification.J, specification.M, specification.h)
    >>> colour.JMh_CIECAM02_to_CAM02UCS(JMh)
    array([ 54.90433134,  -0.08442362,  -0.06848314])

CAM16-LCD, CAM16-SCD, and CAM16-UCS Colourspaces - Li et al. (2017)
*******************************************************************

.. code-block:: python

    >>> import colour
    >>> XYZ = np.array([19.01, 20.00, 21.78])
    >>> XYZ_w = np.array([95.05, 100.00, 108.88])
    >>> L_A = 318.31
    >>> Y_b = 20.0
    >>> specification = colour.XYZ_to_CAM16(
            XYZ, XYZ_w, L_A, Y_b, surround)
    >>> JMh = (specification.J, specification.M, specification.h)
    >>> colour.JMh_CAM16_to_CAM16UCS(JMh)
    array([ 54.89102616,  -9.42910274,  -5.52845976])

IPT Colourspace
***************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_IPT([0.07049534, 0.10080000, 0.09558313])
    array([ 0.36571124, -0.11114798,  0.01594746])

hdr-CIELAB Colourspace
**********************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_hdr_CIELab([0.07049534, 0.10080000, 0.09558313])
    array([ 24.90206646, -46.83127607, -10.14274843])

hdr-IPT Colourspace
*******************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_hdr_IPT([0.07049534, 0.10080000, 0.09558313])
    array([ 25.18261761, -22.62111297,   3.18511729])

RGB Colourspace and Transformations
***********************************

.. code-block:: python

    >>> import colour
    >>> XYZ = [0.07049534, 0.10080000, 0.09558313]
    >>> illuminant_XYZ = [0.34570, 0.35850]
    >>> illuminant_RGB = [0.31270, 0.32900]
    >>> chromatic_adaptation_transform = 'Bradford'
    >>> XYZ_to_RGB_matrix = [
             [3.24062548, -1.53720797, -0.49862860],
             [-0.96893071, 1.87575606, 0.04151752],
             [0.05571012, -0.20402105, 1.05699594]]
    >>> colour.XYZ_to_RGB(
             XYZ,
             illuminant_XYZ,
             illuminant_RGB,
             XYZ_to_RGB_matrix,
             chromatic_adaptation_transform)
    array([ 0.01100154,  0.12735048,  0.11632713])

RGB Colourspace Derivation
**************************

.. code-block:: python

    >>> import colour
    >>> p = [0.73470, 0.26530, 0.00000, 1.00000, 0.00010, -0.07700]
    >>> w = [0.32168, 0.33767]
    >>> colour.normalised_primary_matrix(p, w)
    array([[  9.52552396e-01,   0.00000000e+00,   9.36786317e-05],
           [  3.43966450e-01,   7.28166097e-01,  -7.21325464e-02],
           [  0.00000000e+00,   0.00000000e+00,   1.00882518e+00]])

Y'CbCr Colour Encoding
**********************

.. code-block:: python

    >>> import colour
    >>> colour.RGB_to_YCbCr([1.0, 1.0, 1.0])
    array([ 0.92156863,  0.50196078,  0.50196078])

YCoCg Colour Encoding
***************s******

.. code-block:: python

    >>> import colour
    >>> colour.RGB_to_YCoCg([0.75, 0.75, 0.0])
    array([ 0.5625,  0.375 ,  0.1875])

ICTCP Colour Encoding
*********************

.. code-block:: python

    >>> import colour
    >>> colour.RGB_to_ICTCP([0.35181454, 0.26934757, 0.21288023])
    array([ 0.09554079, -0.00890639,  0.01389286])

JzAzBz Colourspace
******************

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_JzAzBz(XYZ)
    array([ 0.00357804, -0.00295507,  0.00038998])

HSV Colourspace
***************

.. code-block:: python

    >>> import colour
    >>> colour.RGB_to_HSV([0.49019608, 0.98039216, 0.25098039])
    array([ 0.27867383,  0.744     ,  0.98039216])

Prismatic Colourspace
*********************

.. code-block:: python

    >>> import colour
    >>> colour.RGB_to_Prismatic([0.25, 0.50, 0.75])
    array([ 0.75      ,  0.16666667,  0.33333333,  0.5       ])

RGB Colourspaces
^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> sorted(colour.RGB_COLOURSPACES.keys())
    [u'ACES2065-1',
     u'ACEScc',
     u'ACEScct',
     u'ACEScg',
     u'ACESproxy',
     u'ALEXA Wide Gamut',
     u'Adobe RGB (1998)',
     u'Adobe Wide Gamut RGB',
     u'Apple RGB',
     u'Best RGB',
     u'Beta RGB',
     u'CIE RGB',
     u'Cinema Gamut',
     u'ColorMatch RGB',
     u'DCI-P3',
     u'DCI-P3+',
     u'DRAGONcolor',
     u'DRAGONcolor2',
     u'Don RGB 4',
     u'ECI RGB v2',
     u'ERIMM RGB',
     u'Ekta Space PS 5',
     u'ITU-R BT.2020',
     u'ITU-R BT.470 - 525',
     u'ITU-R BT.470 - 625',
     u'ITU-R BT.709',
     u'Max RGB',
     u'NTSC',
     u'Pal/Secam',
     u'ProPhoto RGB',
     u'Protune Native',
     u'REDWideGamutRGB',
     u'REDcolor',
     u'REDcolor2',
     u'REDcolor3',
     u'REDcolor4',
     u'RIMM RGB',
     u'ROMM RGB',
     u'Russell RGB',
     u'S-Gamut',
     u'S-Gamut3',
     u'S-Gamut3.Cine',
     u'SMPTE 240M',
     u'V-Gamut',
     u'Xtreme RGB',
     'aces',
     'adobe1998',
     'prophoto',
     u'sRGB']

OETFs
^^^^^

.. code-block:: python

    >>> import colour
    >>> sorted(colour.OETFS.keys())
    ['ARIB STD-B67',
     'DCI-P3',
     'DICOM GSDF',
     'ITU-R BT.2020',
     'ITU-R BT.2100 HLG',
     'ITU-R BT.2100 PQ',
     'ITU-R BT.601',
     'ITU-R BT.709',
     'ProPhoto RGB',
     'RIMM RGB',
     'ROMM RGB',
     'SMPTE 240M',
     'ST 2084',
     'sRGB']

EOTFs
^^^^^

.. code-block:: python

    >>> import colour
    >>> sorted(colour.EOTFS.keys())
    ['DCI-P3',
     'DICOM GSDF',
     'ITU-R BT.1886',
     'ITU-R BT.2020',
     'ITU-R BT.2100 HLG',
     'ITU-R BT.2100 PQ',
     'ProPhoto RGB',
     'RIMM RGB',
     'ROMM RGB',
     'SMPTE 240M',
     'ST 2084']

OOTFs
^^^^^

.. code-block:: python

    >>> import colour
    >>> sorted(colour.OOTFS.keys())
    ['ITU-R BT.2100 HLG', 'ITU-R BT.2100 PQ']

Log Encoding / Decoding Curves
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> sorted(colour.LOG_ENCODING_CURVES.keys())
    ['ACEScc',
     'ACEScct',
     'ACESproxy',
     'ALEXA Log C',
     'Canon Log',
     'Canon Log 2',
     'Canon Log 3',
     'Cineon',
     'ERIMM RGB',
     'Log3G10',
     'Log3G12',
     'PLog',
     'Panalog',
     'Protune',
     'REDLog',
     'REDLogFilm',
     'S-Log',
     'S-Log2',
     'S-Log3',
     'V-Log',
     'ViperLog']

Chromatic Adaptation Models
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> XYZ = [0.07049534, 0.10080000, 0.09558313]
    >>> XYZ_w = [1.09846607, 1.00000000, 0.35582280]
    >>> XYZ_wr = [0.95042855, 1.00000000, 1.08890037]
    >>> colour.chromatic_adaptation_VonKries(XYZ, XYZ_w, XYZ_wr)
    array([ 0.08397461,  0.11413219,  0.28625545])

Colour Appearance Models
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> XYZ = [19.01, 20.00, 21.78]
    >>> XYZ_w = [95.05, 100.00, 108.88]
    >>> L_A = 318.31
    >>> Y_b = 20.0
    >>> colour.XYZ_to_CIECAM02(XYZ, XYZ_w, L_A, Y_b)
    CIECAM02_Specification(J=41.731091132513917, C=0.10470775717103062, h=219.04843265831178, s=2.3603053739196032, Q=195.37132596607671, M=0.10884217566914849, H=278.06073585667758, HC=None)

Colour Difference
^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> Lab_1 = [100.00000000, 21.57210357, 272.22819350]
    >>> Lab_2 = [100.00000000, 426.67945353, 72.39590835]
    >>> colour.delta_E(Lab_1, Lab_2)
    94.035649026659485
    >>> sorted(colour.DELTA_E_METHODS.keys())
    ['CAM02-LCD',
     'CAM02-SCD',
     'CAM02-UCS',
     'CAM16-LCD',
     'CAM16-SCD',
     'CAM16-UCS',
     'CIE 1976',
     'CIE 1994',
     'CIE 2000',
     'CMC',
     'cie1976',
     'cie1994',
     'cie2000']

Colour Notation Systems
^^^^^^^^^^^^^^^^^^^^^^^

Munsell Value
*************

.. code-block:: python

    >>> import colour
    >>> colour.munsell_value(10.1488096782)
    3.7462971142584354
    >>> sorted(colour.MUNSELL_VALUE_METHODS.keys())
    [u'ASTM D1535-08',
     u'Ladd 1955',
     u'McCamy 1987',
     u'Moon 1943',
     u'Munsell 1933',
     u'Priest 1920',
     u'Saunderson 1944',
     u'astm2008']

Munsell Colour
**************

.. code-block:: python

    >>> import colour
    >>> colour.xyY_to_munsell_colour([0.38736945, 0.35751656, 0.59362000])
    u'4.2YR 8.1/5.3'
    >>> colour.munsell_colour_to_xyY('4.2YR 8.1/5.3')
    array([ 0.38736945,  0.35751656,  0.59362   ])

Colour Blindness
^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> cmfs = colour.LMS_CMFS['Stockman & Sharpe 2 Degree Cone Fundamentals']
    >>> colour.anomalous_trichromacy_cmfs_Machado2009(cmfs, np.array([15, 0, 0]))[450]
    array([ 0.08912884,  0.0870524 ,  0.955393  ])
    >>> primaries = colour.DISPLAYS_RGB_PRIMARIES['Apple Studio Display']
    >>> d_LMS = (15, 0, 0)
    >>> colour.anomalous_trichromacy_matrix_Machado2009(cmfs, primaries, d_LMS)
    array([[-0.27774652,  2.65150084, -1.37375432],
           [ 0.27189369,  0.20047862,  0.52762768],
           [ 0.00644047,  0.25921579,  0.73434374]])

Optical Phenomena
^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> colour.rayleigh_scattering_spd()
    SpectralPowerDistribution([[  3.60000000e+02,   5.99101337e-01],
                               [  3.61000000e+02,   5.92170690e-01],
                               [  3.62000000e+02,   5.85341006e-01],
                               ...
                               [  7.78000000e+02,   2.55208377e-02],
                               [  7.79000000e+02,   2.53887969e-02],
                               [  7.80000000e+02,   2.52576106e-02]],
                              interpolator=SpragueInterpolator,
                              interpolator_args={},
                              extrapolator=Extrapolator,
                              extrapolator_args={u'right': None, u'method': u'Constant', u'left': None})

Light Quality
^^^^^^^^^^^^^

Colour Rendering Index
**********************

.. code-block:: python

    >>> import colour
    >>> colour.colour_quality_scale(colour.ILLUMINANTS_RELATIVE_SPDS['F2'])
    64.686416902221609

Colour Quality Scale
********************

.. code-block:: python

    >>> import colour
    >>> colour.colour_rendering_index(colour.ILLUMINANTS_RELATIVE_SPDS['F2'])
    64.151520202968015

Reflectance Recovery
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> colour.XYZ_to_spectral([0.07049534, 0.10080000, 0.09558313])
    SpectralPowerDistribution([[  3.60000000e+02,   7.96361498e-04],
                               [  3.65000000e+02,   7.96489667e-04],
                               [  3.70000000e+02,   7.96543669e-04],
                               ...
                               [  8.20000000e+02,   1.71014294e-04],
                               [  8.25000000e+02,   1.71621924e-04],
                               [  8.30000000e+02,   1.72026883e-04]],
                              interpolator=SpragueInterpolator,
                              interpolator_args={},
                              extrapolator=Extrapolator,
                              extrapolator_args={u'right': None, u'method': u'Constant', u'left': None})
    >>> sorted(colour.REFLECTANCE_RECOVERY_METHODS.keys())
    ['Meng 2015', 'Smits 1999']

Correlated Colour Temperature Computation Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> import colour
    >>> colour.uv_to_CCT([0.1978, 0.3122])
    array([  6.50751282e+03,   3.22335875e-03])
    >>> sorted(colour.UV_TO_CCT_METHODS.keys())
    [u'Ohno 2013', u'Robertson 1968', u'ohno2013', u'robertson1968']
    >>> sorted(colour.UV_TO_CCT_METHODS.keys())
    [u'Krystek 1985',
     u'Ohno 2013',
     u'Robertson 1968',
     u'ohno2013',
     u'robertson1968']
     >>> sorted(colour.XY_TO_CCT_METHODS.keys())
     [u'Hernandez 1999', u'McCamy 1992', u'hernandez1999', u'mccamy1992']
     >>> sorted(colour.CCT_TO_XY_METHODS.keys())
     [u'CIE Illuminant D Series', u'Kang 2002', su'cie_d', u'kang2002']

Volume
^^^^^^

.. code-block:: python

    >>> import colour
    >>> colour.RGB_colourspace_volume_MonteCarlo(colour.sRGB_COLOURSPACE)
    857011.5

Plotting
^^^^^^^^

Visible Spectrum
****************

.. code-block:: python

    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> visible_spectrum_plot('CIE 1931 2 Degree Standard Observer')

..  image:: _static/Examples_Plotting_Visible_Spectrum.png

Spectral Power Distribution
***************************

.. code-block:: python

    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> single_illuminant_relative_spd_plot('F1')

..  image:: _static/Examples_Plotting_Illuminant_F1_SPD.png

Blackbody
*********

.. code-block:: python

    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> blackbody_spds = [
    ...     colour.blackbody_spd(i, colour.SpectralShape(0, 10000, 10))
    ...     for i in range(1000, 15000, 1000)
    ... ]
    >>> multi_spd_plot(
    ...     blackbody_spds,
    ...     y_label='W / (sr m$^2$) / m',
    ...     use_spds_colours=True,
    ...     normalise_spds_colours=True,
    ...     legend_location='upper right',
    ...     bounding_box=(0, 1250, 0, 2.5e15))

..  image:: _static/Examples_Plotting_Blackbodies.png

Colour Matching Functions
*************************

.. code-block:: python

    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> single_cmfs_plot(
    ...     'Stockman & Sharpe 2 Degree Cone Fundamentals',
    ...     y_label='Sensitivity',
    ...     bounding_box=(390, 870, 0, 1.1))

..  image:: _static/Examples_Plotting_Cone_Fundamentals.png

Luminous Efficiency
*******************

.. code-block:: python

    >>> import colour
    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> mesopic_luminous_efficiency_function = (
    ...     colour.mesopic_luminous_efficiency_function(0.2))
    >>> multi_spd_plot(
    ...     (mesopic_luminous_efficiency_function,
    ...      colour.PHOTOPIC_LEFS['CIE 1924 Photopic Standard Observer'],
    ...      colour.SCOTOPIC_LEFS['CIE 1951 Scotopic Standard Observer']),
    ...     y_label='Luminous Efficiency',
    ...     legend_location='upper right',
    ...     y_tighten=True,
    ...     margins=(0, 0, 0, .1))

..  image:: _static/Examples_Plotting_Luminous_Efficiency.png

Colour Checker
**************

.. code-block:: python

    >>> import colour
    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> multi_spd_plot(
    ...     [
    ...         colour.COLOURCHECKERS_SPDS['BabelColor Average'][value]
    ...         for key, value in sorted(
    ...             COLOURCHECKER_INDEXES_TO_NAMES_MAPPING.items())
    ...     ],
    ...     use_spds_colours=True,
    ...     title=('BabelColor Average - '
    ...            'Relative Spectral Power Distributions'))

..  image:: _static/Examples_Plotting_BabelColor_Average.png

.. code-block:: python

    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> colour_checker_plot('ColorChecker 2005', text_display=False)

..  image:: _static/Examples_Plotting_ColorChecker_2005.png

Chromaticities Prediction
*************************

.. code-block:: python

    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> corresponding_chromaticities_prediction_plot(2, 'Von Kries', 'Bianco')

..  image:: _static/Examples_Plotting_Chromaticities_Prediction.png

Colour Temperature
******************

.. code-block:: python

    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> planckian_locus_chromaticity_diagram_plot_CIE1931(['A', 'B', 'C'])

..  image:: _static/Examples_Plotting_CCT_CIE_1976_UCS_Chromaticity_Diagram.png


Chromaticities
**************

.. code-block:: python

    >>> import numpy as np
    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> RGB = np.random.random((32, 32, 3))
    >>> RGB_chromaticity_coordinates_chromaticity_diagram_plot_CIE1931(
    ...     RGB, 'ITU-R BT.709', colourspaces=['ACEScg', 'S-Gamut', 'Pointer Gamut'])

..  image:: _static/Examples_Plotting_Chromaticities_CIE_1931_Chromaticity_Diagram.png

Colour Rendering Index
**********************

.. code-block:: python

    >>> from colour.plotting import *
    >>> colour_plotting_defaults()
    >>> single_spd_colour_rendering_index_bars_plot(
    ...     colour.ILLUMINANTS_RELATIVE_SPDS['F2'])

..  image:: _static/Examples_Plotting_CRI.png

Contributing
------------

If you would like to contribute to `Colour <https://github.com/colour-science/colour>`_,
please refer to the following `Contributing <http://colour-science.org/contributing>`_ guide.

Changes
-------

The changes are viewable on the `Releases <https://github.com/colour-science/colour/releases>`_ page.

Bibliography
------------

The bibliography is available on the `Bibliography <http://colour-science.org/bibliography/>`_ page.

It is also viewable directly from the repository in
`BibTeX <https://github.com/colour-science/colour/blob/develop/BIBLIOGRAPHY.bib>`_
format.

See Also
--------

Here is a list of notable colour science packages sorted by languages:

**Python**

- `ColorPy <http://markkness.net/colorpy/ColorPy.html>`_ by Kness, M.
- `Colorspacious <http://colorspacious.readthedocs.io/>`_ by Smith, N. J., et al.
- `python-colormath <http://python-colormath.readthedocs.io/>`_ by Taylor, G., et al.

**.NET**

- `Colourful <https://github.com/tompazourek/Colourful>`_ by Pažourek, T., et al.

**Julia**

- `Colors.jl <https://github.com/JuliaGraphics/Colors.jl>`_ by Holy, T., et al.

**Matlab & Octave**

- `COLORLAB <https://www.uv.es/vista/vistavalencia/software/colorlab.html>`_ by Malo, J., et al.
- `Psychtoolbox <http://psychtoolbox.org/>`_ by Brainard, D., et al.
- `The Munsell and Kubelka-Munk Toolbox <http://www.munsellcolourscienceforpainters.com/MunsellAndKubelkaMunkToolbox/MunsellAndKubelkaMunkToolbox.html>`_ by Centore, P.

About
-----

| **Colour** by Colour Developers - 2013-2018
| Copyright © 2013-2018 – Colour Developers – `colour-science@googlegroups.com <colour-science@googlegroups.com>`_
| This software is released under terms of New BSD License: http://opensource.org/licenses/BSD-3-Clause
| `http://github.com/colour-science/colour <http://github.com/colour-science/colour>`_
