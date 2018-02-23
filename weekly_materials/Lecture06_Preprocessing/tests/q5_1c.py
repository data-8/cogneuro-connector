test = {

    'name': '1C',
    'points': 0.5,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'data1' should be present
                    >>> 'data1' in vars()
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'data2' should be present
                    >>> 'data2' in vars()
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'same1' should be present
                    >>> 'same1' in vars()
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        }
        
        

]}