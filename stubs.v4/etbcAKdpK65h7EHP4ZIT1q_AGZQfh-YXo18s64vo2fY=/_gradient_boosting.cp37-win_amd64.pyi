import builtins as _mod_builtins
import numpy as _mod_numpy
import scipy.sparse.csr as _mod_scipy_sparse_csr

__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\sklearn\\ensemble\\_gradient_boosting.cp37-win_amd64.pyd'
__name__ = 'sklearn.ensemble._gradient_boosting'
__package__ = 'sklearn.ensemble'
def __pyx_unpickle_Enum():
    pass

__test__ = _mod_builtins.dict()
def _predict_regression_tree_stages_sparse():
    'Predicts output for regression tree inplace and adds scaled value to ``out[i, k]``.\n\n    The function assumes that the ndarray that wraps ``X`` is csr_matrix.\n    '
    pass

def _random_sample_mask():
    'Create a random sample mask where ``n_total_in_bag`` elements are set.\n\n     Parameters\n     ----------\n     n_total_samples : int\n         The length of the resulting mask.\n\n     n_total_in_bag : int\n         The number of elements in the sample mask which are set to 1.\n\n     random_state : RandomState\n         A numpy ``RandomState`` object.\n\n     Returns\n     -------\n     sample_mask : np.ndarray, shape=[n_total_samples]\n         An ndarray where ``n_total_in_bag`` elements are set to ``True``\n         the others are ``False``.\n     '
    pass

csr_matrix = _mod_scipy_sparse_csr.csr_matrix
def issparse(x):
    'Is x of a sparse matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a sparse matrix\n\n    Returns\n    -------\n    bool\n        True if x is a sparse matrix, False otherwise\n\n    Notes\n    -----\n    issparse and isspmatrix are aliases for the same function.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix\n    >>> isspmatrix(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import isspmatrix\n    >>> isspmatrix(5)\n    False\n    '
    pass

np_bool = _mod_builtins.bool
np_float32 = _mod_numpy.float32
np_float64 = _mod_numpy.float64
def np_ones(shape, dtype, order):
    "\n    Return a new array of given shape and type, filled with ones.\n\n    Parameters\n    ----------\n    shape : int or sequence of ints\n        Shape of the new array, e.g., ``(2, 3)`` or ``2``.\n    dtype : data-type, optional\n        The desired data-type for the array, e.g., `numpy.int8`.  Default is\n        `numpy.float64`.\n    order : {'C', 'F'}, optional, default: C\n        Whether to store multi-dimensional data in row-major\n        (C-style) or column-major (Fortran-style) order in\n        memory.\n\n    Returns\n    -------\n    out : ndarray\n        Array of ones with the given shape, dtype, and order.\n\n    See Also\n    --------\n    ones_like : Return an array of ones with shape and type of input.\n    empty : Return a new uninitialized array.\n    zeros : Return a new array setting values to zero.\n    full : Return a new array of given shape filled with value.\n\n\n    Examples\n    --------\n    >>> np.ones(5)\n    array([1., 1., 1., 1., 1.])\n\n    >>> np.ones((5,), dtype=int)\n    array([1, 1, 1, 1, 1])\n\n    >>> np.ones((2, 1))\n    array([[1.],\n           [1.]])\n\n    >>> s = (2,2)\n    >>> np.ones(s)\n    array([[1.,  1.],\n           [1.,  1.]])\n\n    "
    pass

def np_zeros():
    "zeros(shape, dtype=float, order='C')\n\n    Return a new array of given shape and type, filled with zeros.\n\n    Parameters\n    ----------\n    shape : int or tuple of ints\n        Shape of the new array, e.g., ``(2, 3)`` or ``2``.\n    dtype : data-type, optional\n        The desired data-type for the array, e.g., `numpy.int8`.  Default is\n        `numpy.float64`.\n    order : {'C', 'F'}, optional, default: 'C'\n        Whether to store multi-dimensional data in row-major\n        (C-style) or column-major (Fortran-style) order in\n        memory.\n\n    Returns\n    -------\n    out : ndarray\n        Array of zeros with the given shape, dtype, and order.\n\n    See Also\n    --------\n    zeros_like : Return an array of zeros with shape and type of input.\n    empty : Return a new uninitialized array.\n    ones : Return a new array setting values to one.\n    full : Return a new array of given shape filled with value.\n\n    Examples\n    --------\n    >>> np.zeros(5)\n    array([ 0.,  0.,  0.,  0.,  0.])\n\n    >>> np.zeros((5,), dtype=int)\n    array([0, 0, 0, 0, 0])\n\n    >>> np.zeros((2, 1))\n    array([[ 0.],\n           [ 0.]])\n\n    >>> s = (2,2)\n    >>> np.zeros(s)\n    array([[ 0.,  0.],\n           [ 0.,  0.]])\n\n    >>> np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype\n    array([(0, 0), (0, 0)],\n          dtype=[('x', '<i4'), ('y', '<i4')])"
    pass

def predict_stage():
    'Add predictions of ``estimators[stage]`` to ``out``.\n\n    Each estimator in the stage is scaled by ``scale`` before\n    its prediction is added to ``out``.\n    '
    pass

def predict_stages():
    'Add predictions of ``estimators`` to ``out``.\n\n    Each estimator is scaled by ``scale`` before its prediction\n    is added to ``out``.\n    '
    pass

