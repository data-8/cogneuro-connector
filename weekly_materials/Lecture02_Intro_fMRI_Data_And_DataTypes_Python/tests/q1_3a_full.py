test = {

    'name': '3A_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The class of `tup` should be `tuple`.
                    >>> type(tup)
                    <class 'tuple'>
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
                    >>> # The content of `tup` should be `('I', 'love', 'data', 'science')`.
                    >>> tup == ('I', 'love', 'data', 'science')
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
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The class of `tup` should be `tuple`.
                    >>> type(tup)
                    <class 'tuple'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # 'I' should be in tup.
                    >>> 'I' in tup
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
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The class of `tup` should be `tuple`.
                    >>> type(tup)
                    <class 'tuple'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # 'love' should be in tup.
                    >>> 'love' in tup
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
        {
            'cases': [
                {
                    'code': r"""
                    >>> # 'data' should be in tup.
                    >>> 'data' in tup
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
        {
            'cases': [
                {
                    'code': r"""
                    >>> # 'science' should be in tup.
                    >>> 'science' in tup
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