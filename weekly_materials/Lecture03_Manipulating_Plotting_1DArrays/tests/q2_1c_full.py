test = {

    'name': '1C',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # If noise was sampled from a Gaussian, then its mean should very probably
                    >>> # be within [-.6, .6]: The probability for that is >99.98%
                    >>> m = noise.mean()
                    >>> (-.6 < m) & (m < .6)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # If noise was sampled from a Gaussian, then its variance should very probably
                    >>> # be within [.4, 2.]: The probability for that is >99.98%
                    >>> v = noise.var()
                    >>> (.4 < v) & (v < 2.)
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
                    >>> # noise should be of the same shape as signal
                    >>> noise.shape == signal.shape
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
                    >>> # timeseries should be of the same shape as signal
                    >>> timeseries.shape == signal.shape
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
                    >>> # timeseries should be equal to signal + noise
                    >>> np.allclose(timeseries, signal + noise)
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