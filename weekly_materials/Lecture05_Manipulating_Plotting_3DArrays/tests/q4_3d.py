test = {

    'name': '3D',
    'points': 1,
    'suites': [
        {
            'cases': [              
                {
                    'code': r"""
                    >>> # after this part, the name `cortex_volume` should exist
                    >>> 'cortex_volume' in vars()
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