test = {

    'name': '4C_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # `array_3d` should be of type int
                    >>> array_3d.dtype == 'int'
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
        {
            'cases': [
                {
                    'code': r"""
                    >>> # `array_3d` should be of shape (4, 5, 3)
                    >>> array_3d.shape == (4, 5, 3)
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # `array_3d` should be of value 1 everywhere
                    >>> (array_3d == 1).all()
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