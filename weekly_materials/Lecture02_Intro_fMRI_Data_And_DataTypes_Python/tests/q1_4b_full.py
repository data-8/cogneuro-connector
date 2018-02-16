test = {

    'name': '4B_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # numpy should be imported at this stage. Either as np or as numpy
                    >>> 'np' in vars() or 'numpy' in vars()
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
                    >>> # `seq_half_one` should be of type float
                    >>> seq_half_one.dtype == 'float64' or seq_half_one.dtype == 'float32'
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # `seq_half_one` should be of length 26
                    >>> len(seq_half_one) == 26
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # `seq_half_one` should be of step 0.02
                    >>> np.allclose(np.diff(seq_half_one), .02, rtol=1e-3)
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # `seq_half_one` should start at 0.5
                    >>> np.abs(seq_half_one[0] - .5) < 1e-4
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # `seq_half_one` should end at 1.0
                    >>> np.abs(seq_half_one[-1] - 1.0) < 1e-4
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '>>> import numpy as np',
            'teardown': '',
            'type': 'doctest'
        },

]}