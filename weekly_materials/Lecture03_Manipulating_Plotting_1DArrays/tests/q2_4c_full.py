test = {

    'name': '4C',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # first_5 should have the length 5
                    >>> len(first_5) == 5
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
                    >>> # first_5 should have the same entries as
                    >>> # even_timeseries[:5]
                    >>> np.allclose(first_5, even_timeseries[:5])
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
                    >>> # first_5 should *not* be a slice of even_timeseries
                    >>> even_timeseries[:5].ctypes.data != first_5.ctypes.data
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