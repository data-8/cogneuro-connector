test = {

    'name': '1D',
    'points': 3,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name 'fig_sixth_volume' should be present
                    >>> 'sixth_volume' in vars()
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
                    >>> # fig_sixth_volume should be a figure
                    >>> import matplotlib
                    >>> isinstance(fig_sixth_volume, matplotlib.figure.Figure)
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