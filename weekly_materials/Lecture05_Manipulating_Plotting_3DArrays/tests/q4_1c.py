test = {

    'name': '1C',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # after this part, the name `raw_voxel_shape` should exist
                    >>> 'raw_voxel_shape' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # after this part, the name `voxel_shape` should exist
                    >>> 'voxel_shape' in vars()
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