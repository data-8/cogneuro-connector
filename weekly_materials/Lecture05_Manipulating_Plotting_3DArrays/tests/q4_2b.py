test = {

    'name': '2B',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # after this part, the name `middle_sagittal` should exist
                    >>> 'middle_sagittal' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },                 
                {
                    'code': r"""
                    >>> # after this part, the name `sagittal_aspect` should exist
                    >>> 'sagittal_aspect' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },                 
                {
                    'code': r"""
                    >>> # after this part, the name `fig_middle_sagittal` should exist
                    >>> 'fig_middle_sagittal' in vars()
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