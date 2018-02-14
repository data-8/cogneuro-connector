test = {

    'name': '4A_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # `seq_50_100` should be of length 26
                    >>> len(nar(seq_50_100)) == 26
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # `seq_50_100` should be of step 2
                    >>> (np.diff(nar(seq_50_100)) == 2).all()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # `seq_50_100` should start at 50
                    >>> nar(seq_50_100)[0] == 50
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # `seq_50_100` should end at 100
                    >>> nar(seq_50_100)[-1] == 100
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },

                
            ],
            'scored': True,
            'setup': '''>>> def nar(x): return np.array(x).ravel()
                        ''',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # `seq_50_100` should be a numpy array
                    >>> isinstance(seq_50_100, np.ndarray)
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # `seq_50_100` should be of type int
                    >>> seq_50_100.dtype == 'int64'
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
        }

]}