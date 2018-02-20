test = {

    'name': '1A',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The value of TR should be 2
                    >>>  TR == 2
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
                    >>> # The first value of `time` should be 0
                    >>>  np.abs(time[0]) < 1e-6
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The last value of `time` should be 98
                    >>>  np.abs(time[-1] - 98) < .9 * TR
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
                    >>> # The step size of `time` should be TR
                    >>>  np.allclose(np.diff(time), TR)
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
                    >>> # The data type of time should be `float64`
                    >>>  time.dtype == 'float64'
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