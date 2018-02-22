test = {

    'name': '2B',
    'points': 0.5,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'cw' should be present
                    >>> 'cw' in vars()
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
                    >>> # The name 'fig_complex_wave' should be present
                    >>> 'fig_complex_wave' in vars()
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