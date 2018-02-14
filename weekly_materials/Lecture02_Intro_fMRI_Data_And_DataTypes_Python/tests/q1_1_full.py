test = {

    'name': '1_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The numpy package should be imported, preferably as np
                    >>> 'np' in vars() or 'numpy' in vars()
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
                    >>> # The nibabel package should be imported
                    >>> 'nibabel' in vars() or 'nib' in vars()
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