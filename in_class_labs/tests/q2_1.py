test = {

    'name': '2.1',
    'points': 2,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # It seems like you may be using variable name different from 'data'
                    >>> # Please use the variable name 'data' for this cell
                    >>> 'data' in vars()
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # It looks like you may have forgotten to transpose the data array
                    >>> # try using array.T
                    >>> data.shape != (100, 100, 30, 120)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # It looks like you may have forgotten to transpose the data array
                    >>> # try using array.T
                    >>> data.shape == (120, 30, 100, 100)
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
        }

]}