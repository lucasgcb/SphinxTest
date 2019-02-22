Docstring Format
================

Back in the day, docstrings used used to be just plain
reStructuredText inside of docstrings.

* It was very gross.
* Even for Google.

Solution
--------

Google defined a non-gross docstring format that everyone accepts
and Sphinx recognizes.

* Sphinx needs an addon called "Napoleon" to interpret it.
* It is not a problem. This is defined in the doc's conf.py.

`Numpy docstrings Example <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html>`_

conf.py:

.. code-block:: python

   extensions = [
       'sphinx.ext.autodoc',
       'sphinx.ext.intersphinx',
       'sphinx.ext.todo',
       'sphinx.ext.coverage',
       'sphinx.ext.mathjax',
       'sphinx.ext.ifconfig',
       'sphinx.ext.viewcode',
       'sphinx.ext.githubpages',
       'sphinx.ext.napoleon', # <- Here is Napoleon
   ]

See also: `Google docstrings Example <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_

The code in :py:mod:`alpha` and :py:mod:`beta` utilize this Docstring format
and are automatically generated.
