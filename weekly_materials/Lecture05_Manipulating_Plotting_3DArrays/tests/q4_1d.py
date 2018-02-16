test = {

    'name': '1D',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # after this part, the name `mean_volume` should exist
                    >>> 'mean_volume' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # mean_volume should be a numpy array
                    >>> import numpy as np
                    >>> isinstance(mean_volume, np.ndarray)
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # mean_volume should be 3-D
                    >>> mean_volume.ndim == 3
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