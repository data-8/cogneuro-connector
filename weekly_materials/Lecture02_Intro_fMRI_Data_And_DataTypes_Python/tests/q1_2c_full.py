test = {

    'name': '2C_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The output stored in s should be of type string
                    >>> type(s)
                    <class 'str'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in i should be of type int
                    >>> type(i)
                    <class 'int'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in si should be of type string
                    >>> type(si)
                    <class 'str'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in s should be '5'
                    >>> s
                    '5'
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in si should be '55555'
                    >>> si
                    '55555'
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