test = {

    'name': '3E',
    'points': 1,
    'suites': [
        {
            'cases': [              
                {
                    'code': r"""
                    >>> # after this part, the name `fig_cortex` should exist
                    >>> 'fig_cortex' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },                 
            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        },

]}