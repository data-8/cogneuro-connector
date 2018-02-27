test = {

    'name': '3A',
    'points': 3,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'faces_volumes' should be present
                    >>> 'faces_volumes' in vars()
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
                    >>> # faces_volumes should be 60 volumes
                    >>> len(faces_volumes) == 60
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
                    >>> # faces_volumes should be of shape (60, 30, 100, 100)
                    >>> faces_volumes.shape == (60, 30, 100, 100)
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