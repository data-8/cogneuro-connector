test = {

    'name': '3A',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # after this part, `cortex` should be imported
                    >>> 'cortex' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },                 
                {
                    'code': r"""
                    >>> # after this part, the name `mask` should exist
                    >>> 'mask' in vars()
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