test = {

    'name': '2A_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The output stored in a should be of type float
                    >>> type(a)
                    <class 'float'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in a should be 3.0
                    >>> a
                    3.0
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
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The output stored in b should be of type int
                    >>> type(b)
                    <class 'int'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in b should be 3
                    >>> b
                    3
                    """,
                    'hidden': True,
                    'locked': False
                },
                

            ],
            'scored': True,
            'setup': '',
            'teardown': '',
            'type': 'doctest'
        }

]}