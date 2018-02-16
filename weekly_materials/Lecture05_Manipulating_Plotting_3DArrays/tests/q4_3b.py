test = {

    'name': '3B',
    'points': 1,
    'suites': [
        {
            'cases': [              
                {
                    'code': r"""
                    >>> # after this part, the name `fig_sagittal_mask` should exist
                    >>> 'fig_sagittal_mask' in vars()
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