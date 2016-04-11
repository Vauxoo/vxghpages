========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |coveralls| |codecov|
        | |codeclimate|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/vxghpages/badge/?style=flat
    :target: https://readthedocs.org/projects/vxghpages
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/Vauxoo/vxghpages.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/Vauxoo/vxghpages

.. |requires| image:: https://requires.io/github/Vauxoo/vxghpages/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/Vauxoo/vxghpages/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/Vauxoo/vxghpages/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/Vauxoo/vxghpages

.. |codecov| image:: https://codecov.io/github/Vauxoo/vxghpages/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/Vauxoo/vxghpages

.. |codeclimate| image:: https://codeclimate.com/github/Vauxoo/vxghpages/badges/gpa.svg
   :target: https://codeclimate.com/github/Vauxoo/vxghpages
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/vxghpages.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/vxghpages

.. |downloads| image:: https://img.shields.io/pypi/dm/vxghpages.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/vxghpages

.. |wheel| image:: https://img.shields.io/pypi/wheel/vxghpages.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/vxghpages

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/vxghpages.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/vxghpages

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/vxghpages.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/vxghpages


.. end-badges

A simple configurator helper to help you to magically configure your repository to publich the content in a doc file to
gh-pages using sphinx.

* Free software: BSD license

Installation
============

::

    pip install vxghpages

Documentation
=============

https://vxghpages.readthedocs.org/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
