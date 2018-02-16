test = {

    'name': '1B',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # after this part, the name `raw_data` should exist
                    >>> 'raw_data' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # after this part, the name `data` should exist
                    >>> 'data' in vars()
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