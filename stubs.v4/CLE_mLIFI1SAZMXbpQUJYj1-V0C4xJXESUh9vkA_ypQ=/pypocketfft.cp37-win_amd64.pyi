__doc__ = 'Fast Fourier and Hartley transforms.\n\nThis module supports\n- single, double, and long double precision\n- complex and real-valued transforms\n- multi-dimensional transforms\n\nFor two- and higher-dimensional transforms the code will use SSE2 and AVX\nvector instructions for faster execution if these are supported by the CPU and\nwere enabled during compilation.\n'
__file__ = 'c:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\scipy\\fft\\_pocketfft\\pypocketfft.cp37-win_amd64.pyd'
__name__ = 'scipy.fft._pocketfft.pypocketfft'
__package__ = 'scipy.fft._pocketfft'
def c2c(a: array, axes: object=None, forward: bool=True, inorm: int=0, out: object=None, nthreads: int=1):
    "c2c(a: array, axes: object = None, forward: bool = True, inorm: int = 0, out: object = None, nthreads: int = 1) -> array\n\nPerforms a complex FFT.\n\nParameters\n----------\na : numpy.ndarray (any complex or real type)\n    The input data. If its type is real, a more efficient real-to-complex\n    transform will be used.\naxes : list of integers\n    The axes along which the FFT is carried out.\n    If not set, all axes will be transformed.\nforward : bool\n    If `True`, a negative sign is used in the exponent, else a positive one.\ninorm : int\n    Normalization type\n      0 : no normalization\n      1 : divide by sqrt(N)\n      2 : divide by N\n    where N is the product of the lengths of the transformed axes.\nout : numpy.ndarray (same shape as `a`, complex type with same accuracy as `a`)\n    May be identical to `a`, but if it isn't, it must not overlap with `a`.\n    If None, a new array is allocated to store the output.\nnthreads : int\n    Number of threads to use. If 0, use the system default (typically governed\n    by the `OMP_NUM_THREADS` environment variable).\n\nReturns\n-------\nnumpy.ndarray (same shape as `a`, complex type with same accuracy as `a`)\n    The transformed data.\n\n"
    pass

def c2r(a: array, axes: object=None, lastsize: int=0, forward: bool=True, inorm: int=0, out: object=None, nthreads: int=1):
    'c2r(a: array, axes: object = None, lastsize: int = 0, forward: bool = True, inorm: int = 0, out: object = None, nthreads: int = 1) -> array\n\nPerforms an FFT whose output is strictly real.\n\nParameters\n----------\na : numpy.ndarray (any complex type)\n    The input data\naxes : list of integers\n    The axes along which the FFT is carried out.\n    If not set, all axes will be transformed in ascending order.\nlastsize : the output size of the last axis to be transformed.\n    If the corresponding input axis has size n, this can be 2*n-2 or 2*n-1.\nforward : bool\n    If `True`, a negative sign is used in the exponent, else a positive one.\ninorm : int\n    Normalization type\n      0 : no normalization\n      1 : divide by sqrt(N)\n      2 : divide by N\n    where N is the product of the lengths of the transformed output axes.\nout : numpy.ndarray (real type with same accuracy as `a`)\n    For the required shape, see the `Returns` section.\n    Must not overlap with `a`.\n    If None, a new array is allocated to store the output.\nnthreads : int\n    Number of threads to use. If 0, use the system default (typically governed\n    by the `OMP_NUM_THREADS` environment variable).\n\nReturns\n-------\nnumpy.ndarray (real type with same accuracy as `a`)\n    The transformed data. The shape is identical to that of the input array,\n    except for the axis that was transformed last, which has now `lastsize`\n    entries.\n\n'
    pass

def dct(a: array, type: int, axes: object=None, inorm: int=0, out: object=None, nthreads: int=1):
    "dct(a: array, type: int, axes: object = None, inorm: int = 0, out: object = None, nthreads: int = 1) -> array\n\nPerforms a discrete cosine transform.\n\nParameters\n----------\na : numpy.ndarray (any real type)\n    The input data\ntype : integer\n    the type of DCT. Must be in [1; 4].\naxes : list of integers\n    The axes along which the transform is carried out.\n    If not set, all axes will be transformed.\ninorm : int\n    Normalization type\n      0 : no normalization\n      1 : make transform orthogonal and divide by sqrt(N)\n      2 : divide by N\n    where N is the product of n_i for every transformed axis i.\n    n_i is 2*(<axis_length>-1 for type 1 and 2*<axis length>\n    for types 2, 3, 4.\n    Making the transform orthogonal involves the following additional steps\n    for every 1D sub-transform:\n      Type 1 : multiply first and last input value by sqrt(2)\n               divide first and last output value by sqrt(2)\n      Type 2 : divide first output value by sqrt(2)\n      Type 3 : multiply first input value by sqrt(2)\n      Type 4 : nothing\nout : numpy.ndarray (same shape and data type as `a`)\n    May be identical to `a`, but if it isn't, it must not overlap with `a`.\n    If None, a new array is allocated to store the output.\nnthreads : int\n    Number of threads to use. If 0, use the system default (typically governed\n    by the `OMP_NUM_THREADS` environment variable).\n\nReturns\n-------\nnumpy.ndarray (same shape and data type as `a`)\n    The transformed data\n\n"
    pass

def dst(a: array, type: int, axes: object=None, inorm: int=0, out: object=None, nthreads: int=1):
    "dst(a: array, type: int, axes: object = None, inorm: int = 0, out: object = None, nthreads: int = 1) -> array\n\nPerforms a discrete sine transform.\n\nParameters\n----------\na : numpy.ndarray (any real type)\n    The input data\ntype : integer\n    the type of DST. Must be in [1; 4].\naxes : list of integers\n    The axes along which the transform is carried out.\n    If not set, all axes will be transformed.\ninorm : int\n    Normalization type\n      0 : no normalization\n      1 : make transform orthogonal and divide by sqrt(N)\n      2 : divide by N\n    where N is the product of n_i for every transformed axis i.\n    n_i is 2*(<axis_length>+1 for type 1 and 2*<axis length>\n    for types 2, 3, 4.\n    Making the transform orthogonal involves the following additional steps\n    for every 1D sub-transform:\n      Type 1 : nothing\n      Type 2 : divide first output value by sqrt(2)\n      Type 3 : multiply first input value by sqrt(2)\n      Type 4 : nothing\nout : numpy.ndarray (same shape and data type as `a`)\n    May be identical to `a`, but if it isn't, it must not overlap with `a`.\n    If None, a new array is allocated to store the output.\nnthreads : int\n    Number of threads to use. If 0, use the system default (typically governed\n    by the `OMP_NUM_THREADS` environment variable).\n\nReturns\n-------\nnumpy.ndarray (same shape and data type as `a`)\n    The transformed data\n\n"
    pass

def genuine_hartley(a: array, axes: object=None, inorm: int=0, out: object=None, nthreads: int=1):
    "genuine_hartley(a: array, axes: object = None, inorm: int = 0, out: object = None, nthreads: int = 1) -> array\n\nPerforms a full Hartley transform.\nA full Fourier transform is carried out over the requested axes, and the\nsum of real and imaginary parts of the result is stored in the output\narray. For a single transformed axis, this is identical to `separable_hartley`,\nbut when transforming multiple axes, the results are different.\n\nParameters\n----------\na : numpy.ndarray (any real type)\n    The input data\naxes : list of integers\n    The axes along which the transform is carried out.\n    If not set, all axes will be transformed.\ninorm : int\n    Normalization type\n      0 : no normalization\n      1 : divide by sqrt(N)\n      2 : divide by N\n    where N is the product of the lengths of the transformed axes.\nout : numpy.ndarray (same shape and data type as `a`)\n    May be identical to `a`, but if it isn't, it must not overlap with `a`.\n    If None, a new array is allocated to store the output.\nnthreads : int\n    Number of threads to use. If 0, use the system default (typically governed\n    by the `OMP_NUM_THREADS` environment variable).\n\nReturns\n-------\nnumpy.ndarray (same shape and data type as `a`)\n    The transformed data\n\n"
    pass

def good_size():
    'Returns a good length to pad an FFT to.\n\nParameters\n----------\nn : int\n    Minimum transform length\nreal : bool, optional\n    True if either input or output of FFT should be fully real.\n\nReturns\n-------\nout : int\n    The smallest fast size >= n\n\n'
    pass

def r2c(a: array, axes: object=None, forward: bool=True, inorm: int=0, out: object=None, nthreads: int=1):
    'r2c(a: array, axes: object = None, forward: bool = True, inorm: int = 0, out: object = None, nthreads: int = 1) -> array\n\nPerforms an FFT whose input is strictly real.\n\nParameters\n----------\na : numpy.ndarray (any real type)\n    The input data\naxes : list of integers\n    The axes along which the FFT is carried out.\n    If not set, all axes will be transformed in ascending order.\nforward : bool\n    If `True`, a negative sign is used in the exponent, else a positive one.\ninorm : int\n    Normalization type\n      0 : no normalization\n      1 : divide by sqrt(N)\n      2 : divide by N\n    where N is the product of the lengths of the transformed input axes.\nout : numpy.ndarray (complex type with same accuracy as `a`)\n    For the required shape, see the `Returns` section.\n    Must not overlap with `a`.\n    If None, a new array is allocated to store the output.\nnthreads : int\n    Number of threads to use. If 0, use the system default (typically governed\n    by the `OMP_NUM_THREADS` environment variable).\n\nReturns\n-------\nnumpy.ndarray (complex type with same accuracy as `a`)\n    The transformed data. The shape is identical to that of the input array,\n    except for the axis that was transformed last. If the length of that axis\n    was n on input, it is n//2+1 on output.\n\n'
    pass

def r2r_fftpack(a: array, axes: object, real2hermitian: bool, forward: bool, inorm: int=0, out: object=None, nthreads: int=1):
    "r2r_fftpack(a: array, axes: object, real2hermitian: bool, forward: bool, inorm: int = 0, out: object = None, nthreads: int = 1) -> array\n\nPerforms a real-valued FFT using the FFTPACK storage scheme.\n\nParameters\n----------\na : numpy.ndarray (any real type)\n    The input data\naxes : list of integers\n    The axes along which the FFT is carried out.\n    If not set, all axes will be transformed.\nreal2hermitian : bool\n    if True, the input is purely real and the output will have Hermitian\n    symmetry and be stored in FFTPACK's halfcomplex ordering, otherwise the\n    opposite.\nforward : bool\n    If `True`, a negative sign is used in the exponent, else a positive one.\ninorm : int\n    Normalization type\n      0 : no normalization\n      1 : divide by sqrt(N)\n      2 : divide by N\n    where N is the length of `axis`.\nout : numpy.ndarray (same shape and data type as `a`)\n    May be identical to `a`, but if it isn't, it must not overlap with `a`.\n    If None, a new array is allocated to store the output.\nnthreads : int\n    Number of threads to use. If 0, use the system default (typically governed\n    by the `OMP_NUM_THREADS` environment variable).\n\nReturns\n-------\nnumpy.ndarray (same shape and data type as `a`)\n    The transformed data. The shape is identical to that of the input array.\n\n"
    pass

def separable_hartley(a: array, axes: object=None, inorm: int=0, out: object=None, nthreads: int=1):
    "separable_hartley(a: array, axes: object = None, inorm: int = 0, out: object = None, nthreads: int = 1) -> array\n\nPerforms a separable Hartley transform.\nFor every requested axis, a 1D forward Fourier transform is carried out, and\nthe real and imaginary parts of the result are added before the next axis is\nprocessed.\n\nParameters\n----------\na : numpy.ndarray (any real type)\n    The input data\naxes : list of integers\n    The axes along which the transform is carried out.\n    If not set, all axes will be transformed.\ninorm : int\n    Normalization type\n      0 : no normalization\n      1 : divide by sqrt(N)\n      2 : divide by N\n    where N is the product of the lengths of the transformed axes.\nout : numpy.ndarray (same shape and data type as `a`)\n    May be identical to `a`, but if it isn't, it must not overlap with `a`.\n    If None, a new array is allocated to store the output.\nnthreads : int\n    Number of threads to use. If 0, use the system default (typically governed\n    by the `OMP_NUM_THREADS` environment variable).\n\nReturns\n-------\nnumpy.ndarray (same shape and data type as `a`)\n    The transformed data\n\n"
    pass

