test = {

    'name': '5A',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # 'mean_first_5' should contain the mean of `first_5`
                    >>> np.allclose(mean_first_5, np.mean(first_5))
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
                    >>> # 'mean_remaining' should contain the mean of the remaining TRs
                    >>> np.allclose(mean_remaining, even_timeseries_clean.mean())
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
                    >>> # 'means' should contain the mean of first_5 and the mean
                    >>> # of the remaining TRs
                    >>> np.allclose(means[0], mean_first_5) and np.allclose(means[1], mean_remaining)
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