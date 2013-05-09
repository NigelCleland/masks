=====
masks
=====

Additions to the Python-Pandas library which provide syntactic sugar for
selecting data instead of the current (imo) unwieldy syntax.

Installation
============

masks may be installed using pip or by cloning the current source.

    pip install masks
    
It can be installed in a virtual environment or however you wish.

Features
========

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
    
Development
===========

masks is currently in semi active development.
It is mainly intended for my own usage but other people may wish to use it as well.
Hopefully it is of use to anyone. Feel free to use/modify/distribute as you want.

License: MIT

    
