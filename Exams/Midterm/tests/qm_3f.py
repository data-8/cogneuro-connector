test = {

    'name': '3F',
    'points': 6,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'pycortex_contrast_volume' should be present
                    >>> 'pycortex_contrast_volume' in vars()
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
                    >>> # The name 'fig_contrast' should be present
                    >>> 'fig_contrast' in vars()
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
                    >>> # The name 'fig_contrast' should be a figure
                    >>> import matplotlib
                    >>> isinstance(fig_contrast, matplotlib.figure.Figure)
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