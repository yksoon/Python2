import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\sklearn\\metrics\\cluster\\_expected_mutual_info_fast.cp37-win_amd64.pyd'
__name__ = 'sklearn.metrics.cluster._expected_mutual_info_fast'
__package__ = 'sklearn.metrics.cluster'
__test__ = _mod_builtins.dict()
def expected_mutual_information():
    'Calculate the expected mutual information for two labelings.'
    pass

def gammaln(x, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True, signature=None, extobj=None):
    "gammaln(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])\n\ngammaln(x, out=None)\n\nLogarithm of the absolute value of the Gamma function.\n\nDefined as\n\n.. math::\n\n   \\ln(\\lvert\\Gamma(x)\\rvert)\n\nwhere :math:`\\Gamma` is the Gamma function. For more details on\nthe Gamma function, see [dlmf]_.\n\nParameters\n----------\nx : array_like\n    Real argument\nout : ndarray, optional\n    Optional output array for the function results\n\nReturns\n-------\nscalar or ndarray\n    Values of the log of the absolute value of Gamma\n\nSee Also\n--------\ngammasgn : sign of the gamma function\nloggamma : principal branch of the logarithm of the gamma function\n\nNotes\n-----\nIt is the same function as the Python standard library function\n:func:`math.lgamma`.\n\nWhen used in conjunction with `gammasgn`, this function is useful\nfor working in logspace on the real axis without having to deal\nwith complex numbers via the relation ``exp(gammaln(x)) =\ngammasgn(x) * gamma(x)``.\n\nFor complex-valued log-gamma, use `loggamma` instead of `gammaln`.\n\nReferences\n----------\n.. [dlmf] NIST Digital Library of Mathematical Functions\n          https://dlmf.nist.gov/5\n\nExamples\n--------\n>>> import scipy.special as sc\n\nIt has two positive zeros.\n\n>>> sc.gammaln([1, 2])\narray([0., 0.])\n\nIt has poles at nonpositive integers.\n\n>>> sc.gammaln([0, -1, -2, -3, -4])\narray([inf, inf, inf, inf, inf])\n\nIt asymptotically approaches ``x * log(x)`` (Stirling's formula).\n\n>>> x = np.array([1e10, 1e20, 1e40, 1e80])\n>>> sc.gammaln(x)\narray([2.20258509e+11, 4.50517019e+21, 9.11034037e+41, 1.83206807e+82])\n>>> x * np.log(x)\narray([2.30258509e+11, 4.60517019e+21, 9.21034037e+41, 1.84206807e+82])"
    pass

