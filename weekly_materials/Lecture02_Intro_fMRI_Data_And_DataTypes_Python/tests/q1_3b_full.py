test = {

    'name': '3B_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The class of `l` should be `list`.
                    >>> type(l)
                    <class 'list'>
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
                    >>> # The list `l` should not be empty
                    >>> len(l) > 0
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
                    >>> # 5 should be in l
                    >>> 5 in l
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
                    >>> # [] should be in l
                    >>> [] in l
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
                    >>> # ('I', 'love', 'data', 'science') should be in l or `tup` should be in l
                    >>> ('I', 'love', 'data', 'science') in l or tup in l
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
                    >>> # The content of `l` should be `[('I', 'love', 'data', 'science'), [], 5]` or [tup, [], 5].
                    >>> l == [('I', 'love', 'data', 'science'), [], 5] or l == [tup, [], 5]
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
        }

]}