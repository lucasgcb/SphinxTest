About index.rst file
--------------------

This file is located within the `docs` root and creates the
table of contents (TOC) for displaying next to the page.

::
    .
    ├── _build
    │   └── html
    ├── _static
    │   ├── aboutindex.rst
    │   ├── introduction.rst
    │   └── numpydocstrings.rst
    ├── _templates
    ├── conf.py
    ├── index.rst <--- the index file
    ├── make.bat
    └── Makefile


While not mandatory, this helps with navigation quite a bit.

Unfortunately, the index.rst is much more difficult to
automate as it is the basic source file of Sphinx.

If a new modules is created, its path needs to be written down in
the index.rst file for it to show up in the TOC.
