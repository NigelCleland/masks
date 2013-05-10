=====
masks
=====

Additions to the Python-Pandas library which provide syntactic sugar for
selecting data instead of the current (imo) unwieldy syntax.

Current Version: 0.1.3

Installation
============

masks may be installed using pip or by cloning the current source.

    pip install masks
    
It can be installed in a virtual environment or however you wish.

Features
========

Currently masks are installed for the following use cases:

- equal to
- greater than or equal to
- greater than
- less than or equal to
- less than
- not equal to
- in (e.g. multiple equal to)
- between
- top (top x%)
- bot (bottom x%)
- mid (middle x%)
- mixed equal (e.g. A = X or B = Y)
- mixed boolean (e.g. A >= X or B != Y)

Functionality is applied to both DataFrames and Series through the same syntax.
_mask has been applied to all functions to signify that it is not core pandas
functionality.
Should be noted that some series may not have all masks applied, especially multiple
column masks.

Usage
=====

Currently, masks acts as syntactic sugar to make the selection of data which
meets specific features easier.
Best demonstrated via example.

    import numpy as np
    import pandas as pd
    import masks # Will automatically update pd.DataFrame and pd.Series
    
    sample = pd.DataFrame(np.arange(30).reshape(15,2), columns=["A","B"])
    
    # Select a single row which matches the truth values
    
    sample.eq_mask("A", 16)
    
       A  B
    8 16 17
    
    # This is equivalent to the following
    
    sample[sample["A"] == 16]
    
    # Where masks becomes in handy is in multiple selection.
    # For example
    
    sample.in_eqmask("A", (12, 16, 8))

       A  B
    6 12 13
    
    8 16 17
    
    4  8  9
    
    # Which is equivalent to 
    
    sample[(sample["A"] == 12) | (sample["A"] == 16) | (sample["A"] == 8)]

    # Filters may be chained together as needed

    sample.ge_mask("A", 8).le_mask("B", 13)

       A  B
    4  8  9
    
    5 10 11
    
    6 12 13
    
    
Documentation
=============

Documentation is currently quite lacking, I'm oscilating between the fact that
all of the additional functions are very simple and evidently self documenting.
This package is mainly sugar around the existing syntax, not new functionality.
    
    
Development
===========

masks is currently in semi active development.
It is mainly intended for my own usage but other people may wish to use it as well.
Hopefully it is of use to someone. Feel free to use/modify/distribute as you want.

License: MIT

    
