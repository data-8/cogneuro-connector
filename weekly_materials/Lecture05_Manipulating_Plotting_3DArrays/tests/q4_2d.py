test = {

    'name': '2D',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # after this part, the name `quarter_sagittal` should exist
                    >>> 'quarter_sagittal' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },                 
                {
                    'code': r"""
                    >>> # after this part, the name `threequarter_sagittal` should exist
                    >>> 'threequarter_sagittal' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },                 
                {
                    'code': r"""
                    >>> # after this part, the name `fig_quartiles` should exist
                    >>> 'fig_quartiles' in vars()
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