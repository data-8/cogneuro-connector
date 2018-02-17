test = {

    'name': '4A',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # This test is designed to assign partial credit to flipping
                    >>> # the notions of odd and even around.
                    >>> np.allclose(et, even_timeseries) or np.allclose(ot, eventimeseries)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },

            ],
            'scored': True,
            'setup': '''
                    >>> et = timeseries[::2]
                    >>> ot = timeseries[1::2]
            ''',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The even time series should start at index 0.
                    >>> np.allclose(et, even_timeseries)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },

            ],
            'scored': True,
            'setup': '''
                    >>> et = timeseries[::2]
                    >>> ot = timeseries[1::2]
            ''',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # This test is designed to assign partial credit to flipping
                    >>> # the notions of odd and even around.
                    >>> np.allclose(ot, odd_timeseries) or np.allclose(et, odd_timeseries)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },

            ],
            'scored': True,
            'setup': '''
                    >>> et = timeseries[::2]
                    >>> ot = timeseries[1::2]
            ''',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The odd time series should start at index 1.
                    >>> np.allclose(ot, odd_timeseries)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },

            ],
            'scored': True,
            'setup': '''
                    >>> et = timeseries[::2]
                    >>> ot = timeseries[1::2]
            ''',
            'teardown': '',
            'type': 'doctest'
        }
]}