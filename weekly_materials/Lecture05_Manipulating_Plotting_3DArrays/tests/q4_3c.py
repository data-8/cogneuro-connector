test = {

    'name': '3C',
    'points': 1,
    'suites': [
        {
            'cases': [              
                {
                    'code': r"""
                    >>> # after this part, the name `masked_voxels` should exist
                    >>> 'masked_voxels' in vars()
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