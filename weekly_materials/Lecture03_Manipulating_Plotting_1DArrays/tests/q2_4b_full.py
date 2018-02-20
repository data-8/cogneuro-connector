test = {

    'name': '4B',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # even_timeseries_clean should have the same length as
                    >>> # even_timeseries[5:]
                    >>> len(even_timeseries_clean) == len(even_timeseries) - 5
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
                    >>> # even_timeseries_clean should have the same entries as
                    >>> # even_timeseries[5:]
                    >>> np.allclose(even_timeseries_clean, even_timeseries[5:])
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
                    >>> # even_timeseries_clean should be a slice of even_timeseries
                    >>> even_timeseries[5:].ctypes.data == even_timeseries_clean.ctypes.data
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
                    >>> # assign partial credit to off-by-one indexing
                    >>> (even_timeseries[5:].ctypes.data - even_timeseries_clean.ctypes.data) <= even_timeseries.strides[0]
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