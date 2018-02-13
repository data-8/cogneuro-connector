test = {

    'name': '2C',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # after this part, the name `list_sagittal_slices` should exist
                    >>> 'list_sagittal_slices' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },                 
                {
                    'code': r"""
                    >>> # after this part, the name `num_sagittal_slices` should exist
                    >>> 'num_sagittal_slices' in vars()
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