# Task 3: Fix the function

"""

Below you'll find a function.

1. Can you work out what the function is meant to do?
2. Can you fix and run it?
3. Can you feed it your partner's data and tell us what comes out?

"""

import statistics

def mystery_function( data ):
    avg = statistics.mean( [ x[1] for x in data ] )
    return data
