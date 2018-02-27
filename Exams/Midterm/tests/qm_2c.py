test = {

    'name': '2C',
    'points': 3,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'mask_places' should be present
                    >>> 'mask_places' in vars()
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
                    >>> # mask_places should be a binary array mask
                    >>> mask_places.dtype == 'bool'
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