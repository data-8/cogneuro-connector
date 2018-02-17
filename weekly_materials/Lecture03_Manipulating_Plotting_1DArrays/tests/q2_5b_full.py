test = {

    'name': '5B',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # There should be two bars on figure3
                    >>> len(a.patches) == 2
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '''
                    >>> a = figure3.axes[0]
            ''',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # the tick labels should contain the words 'scan', 'onset', 'rest'
                    >>> 'scan' in ticklabels and 'onset' in ticklabels and 'rest' in ticklabels
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '''
                    >>> a = figure3.axes[0]
                    >>> ticklabels = "".join([l.get_text().lower().replace(" ", "") for l in a.get_xticklabels()])
                    ''',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # xtick positions should be where bars are
                    >>> xticks = a.get_xticks()
                    >>> bar_positions = np.array([p.get_x() + p.get_width() / 2 for p in a.patches])
                    >>> np.allclose(xticks, bar_positions)
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '''
                    >>> a = figure3.axes[0]
            ''',
            'teardown': '',
            'type': 'doctest'
        },
        {
            'cases': [
                {
                    'code': r"""
                    >>> # bar heights should correspond to means
                    >>> bar_heights = np.array([p.get_height() for p in a.patches])
                    >>> (bar_heights[:, np.newaxis] == means.ravel()).any(axis=1).all()
                    True
                    """,
                    'hidden': False,
                    'locked': False
                },
            ],
            'scored': True,
            'setup': '''
                    >>> a = figure3.axes[0]
            ''',
            'teardown': '',
            'type': 'doctest'
        },

]}