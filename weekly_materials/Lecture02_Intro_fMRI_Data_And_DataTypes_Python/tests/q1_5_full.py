test = {

    'name': '5_full',
    'points': 1,
    'suites': [
        {
            'cases': [
                {
                    'code': r"""
                    >>> # data should be a numpy array
                    >>> isinstance(data, np.ndarray)
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
## commented because instructions not clear enough.
#                {
#                    'code': r"""
#                    >>> # data should not be of shape (100, 100, 30, 120)
#                    >>> # If the shape is (100, 100, 30, 120), then data was not transposed.
#                    >>> data.shape == (100, 100, 30, 120)
#                    False
#                    """,
#                    'hidden': True,
#                    'locked': False
#                },
                {
                    'code': r"""
                    >>> # data should be of shape (120, 30, 100, 100)
                    >>> # but we are also accepting (100, 100, 30, 120) because of 
                    >>> # unclear phrasing in the text
                    >>> data.shape == (120, 30, 100, 100) or data.shape == (100, 100, 30, 120)
                    True
                    """,
                    'hidden': True,
                    'locked': False
                },
                {
                    'code': r"""
                    >>> # data should be loaded from the neuroimaging file
                    >>> # here we are giving full points even if data weren't transposed.
                    >>> import nibabel
                    >>> nii_data = nibabel.load("/data/cogneuro/fMRI/categories/s01_categories_01.nii.gz").get_data()
                    >>> np.allclose(data.ravel(), nii_data.T.ravel()) or np.allclose(data.ravel(), nii_data.ravel())
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