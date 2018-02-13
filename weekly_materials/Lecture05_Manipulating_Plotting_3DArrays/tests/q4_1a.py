test = {

    'name': '1A',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # after this part, nibabel should be imported
                    >>> 'nibabel' in vars()
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # after this part, the name `img` should exist
                    >>> 'img' in vars()
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