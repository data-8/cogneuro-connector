test = {

    'name': '3',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The name figure2 should exist
                    >>> 'figure2' in vars()
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
                    >>> # The number of bins in the histogram should be 20
                    >>> len(a.patches) == 20
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '>>> a = figure2.axes[0]',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # The heights of the rectangles of the histogram
                    >>> # should correspond to the following histogram
                    >>> nbins = len(a.patches)
                    >>> c, b, p = plt.hist(timeseries, nbins)
                    >>> rect_heights = np.array([r.get_height() for r in a.patches])
                    >>> np.allclose(rect_heights, c)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '>>> a = figure2.axes[0]',
            'teardown': '',
            'type': 'doctest'
        },

]}