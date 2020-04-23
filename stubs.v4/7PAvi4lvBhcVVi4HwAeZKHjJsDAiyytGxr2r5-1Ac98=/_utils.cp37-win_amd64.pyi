import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\sklearn\\manifold\\_utils.cp37-win_amd64.pyd'
__name__ = 'sklearn.manifold._utils'
__package__ = 'sklearn.manifold'
__test__ = _mod_builtins.dict()
def _binary_search_perplexity():
    'Binary search for sigmas of conditional Gaussians.\n\n    This approximation reduces the computational complexity from O(N^2) to\n    O(uN).\n\n    Parameters\n    ----------\n    sqdistances : array-like, shape (n_samples, n_neighbors)\n        Distances between training samples and their k nearest neighbors.\n        When using the exact method, this is a square (n_samples, n_samples)\n        distance matrix. The TSNE default metric is "euclidean" which is\n        interpreted as squared euclidean distance.\n\n    desired_perplexity : float\n        Desired perplexity (2^entropy) of the conditional Gaussians.\n\n    verbose : int\n        Verbosity level.\n\n    Returns\n    -------\n    P : array, shape (n_samples, n_samples)\n        Probabilities of conditional Gaussian distributions p_i|j.\n    '
    pass

