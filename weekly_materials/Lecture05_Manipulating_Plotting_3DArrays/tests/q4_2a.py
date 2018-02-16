test = {

    'name': '2A',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # after this part, the name `list_numbers` should exist
                    >>> 'list_numbers' in vars()
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