test = {

    'name': '2A',
    'points': 3,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'category_labels' should be present
                    >>> 'category_labels' in vars()
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
                    >>> # category_labels should be a 1D array
                    >>> category_labels.ndim == 1
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
]}