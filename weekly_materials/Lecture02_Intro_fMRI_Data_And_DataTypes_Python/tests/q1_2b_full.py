test = {

    'name': '2B_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The output stored in f should be of type float
                    >>> type(f)
                    <class 'float'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in i should be of type int
                    >>> type(i)
                    <class 'int'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in f_divide_i should be of type float
                    >>> type(f_divide_i)
                    <class 'float'>
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in f should be 5.0
                    >>> f
                    5.0
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in i should be 5
                    >>> i
                    5
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # The output stored in f_divide_i should be 1.0
                    >>> f_divide_i
                    1.0
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