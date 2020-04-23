import builtins as _mod_builtins

__builtins__ = {}
__doc__ = None
__file__ = 'c:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\sklearn\\utils\\_openmp_helpers.cp37-win_amd64.pyd'
__name__ = 'sklearn.utils._openmp_helpers'
__package__ = 'sklearn.utils'
__test__ = _mod_builtins.dict()
def _openmp_effective_n_threads():
    'Determine the effective number of threads to be used for OpenMP calls\n\n    - For ``n_threads = None``,\n      - if the ``OMP_NUM_THREADS`` environment variable is set, return\n        ``openmp.omp_get_max_threads()``\n      - otherwise, return the minimum between ``openmp.omp_get_max_threads()``\n        and the number of cpus, taking cgroups quotas into account. Cgroups \n        quotas can typically be set by tools such as Docker.\n      The result of ``omp_get_max_threads`` can be influenced by environment\n      variable ``OMP_NUM_THREADS`` or at runtime by ``omp_set_num_threads``.\n\n    - For ``n_threads > 0``, return this as the maximal number of threads for\n      parallel OpenMP calls.\n\n    - For ``n_threads < 0``, return the maximal number of threads minus\n      ``|n_threads + 1|``. In particular ``n_threads = -1`` will use as many\n      threads as there are available cores on the machine.\n\n    - Raise a ValueError for ``n_threads = 0``.\n\n    If scikit-learn is built without OpenMP support, always return 1.\n    '
    pass

def _openmp_parallelism_enabled():
    'Determines whether scikit-learn has been built with OpenMP\n    \n    It allows to retrieve at runtime the information gathered at compile time.\n    '
    pass

def cpu_count():
    'Return the number of CPUs.'
    pass

