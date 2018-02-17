test = {

    'name': '2',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name figure1 should exist
                    >>> 'figure1' in vars()
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
                    >>> # The xlabel should contain the words 'time' and 'second'
                    >>> xlabel = a.get_xlabel().lower().replace(" ", "")
                    >>> 'time' in xlabel and 'second' in xlabel
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '>>> a = figure1.axes[0]',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The ylabel should contain the words 'bold' and 'signal'
                    >>> ylabel = a.get_ylabel().lower().replace(" ", "")
                    >>> 'bold' in ylabel and 'signal' in ylabel
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '>>> a = figure1.axes[0]',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The plot x data should be `time`
                    >>> xdata = l.get_xdata()
                    >>> np.allclose(xdata, time)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '''
                        >>> a = figure1.axes[0]
                        >>> l = a.lines[0]
                     ''',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The plot y data should be `timeseries`
                    >>> ydata = l.get_ydata()
                    >>> np.allclose(ydata, timeseries)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '''
                        >>> a = figure1.axes[0]
                        >>> l = a.lines[0]
                     ''',
            'teardown': '',
            'type': 'doctest'
        },


]}