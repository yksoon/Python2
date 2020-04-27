import builtins as _mod_builtins

PyJPClass = _mod_builtins.type
class _JArray(_JObject):
    __class__ = _JArray
    def __del__(self):
        return None
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    def __getitem__(self, index):
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    __module__ = '_jpype'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _JArrayPrimitive(_JArray):
    __class__ = _JArrayPrimitive
    def __del__(self):
        return None
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_jpype'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _JBoolean(_mod_builtins.int):
    __class__ = _JBoolean
    def __del__(self):
        return None
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __float__(self):
        'float(self)'
        return 0.0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = '_jpype'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def from_bytes(cls, type, bytes, byteorder):
        "Return the integer represented by the given array of bytes.\n\n  bytes\n    Holds the array of bytes to convert.  The argument must either\n    support the buffer protocol or be an iterable object producing bytes.\n    Bytes and bytearray are examples of built-in objects that support the\n    buffer protocol.\n  byteorder\n    The byte order used to represent the integer.  If byteorder is 'big',\n    the most significant byte is at the beginning of the byte array.  If\n    byteorder is 'little', the most significant byte is at the end of the\n    byte array.  To request the native byte order of the host system, use\n    `sys.byteorder' as the byte order value.\n  signed\n    Indicates whether two's complement is used to represent the integer."
        pass
    

class _JChar(_mod_builtins.int):
    __class__ = _JChar
    def __del__(self):
        return None
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __float__(self):
        'float(self)'
        return 0.0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = '_jpype'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def from_bytes(cls, type, bytes, byteorder):
        "Return the integer represented by the given array of bytes.\n\n  bytes\n    Holds the array of bytes to convert.  The argument must either\n    support the buffer protocol or be an iterable object producing bytes.\n    Bytes and bytearray are examples of built-in objects that support the\n    buffer protocol.\n  byteorder\n    The byte order used to represent the integer.  If byteorder is 'big',\n    the most significant byte is at the beginning of the byte array.  If\n    byteorder is 'little', the most significant byte is at the end of the\n    byte array.  To request the native byte order of the host system, use\n    `sys.byteorder' as the byte order value.\n  signed\n    Indicates whether two's complement is used to represent the integer."
        pass
    

_JClass = PyJPClass
class _JException(_mod_builtins.Exception,_JObject):
    __class__ = _JException
    def __del__(self):
        return None
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    __dict__ = {}
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_jpype'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _JField(_mod_builtins.object):
    __class__ = _JField
    def __delete__(self, instance):
        'Delete an attribute of instance.'
        pass
    
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        return _JField()
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_jpype'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __set__(self, instance, value):
        'Set an attribute of instance to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _JMethod(_mod_builtins.function):
    @property
    def __annotations__(self):
        return {}
    
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = _JMethod
    @property
    def __closure__(self):
        pass
    
    @property
    def __code__(self):
        return object()
    
    @property
    def __defaults__(self):
        pass
    
    __dict__ = {}
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        return _JMethod()
    
    @property
    def __globals__(self):
        return {}
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @property
    def __kwdefaults__(self):
        pass
    
    __module__ = '_jpype'
    __name__ = '_JMethod'
    __qualname__ = '_JMethod'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @property
    def __self__(self):
        pass
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def dump(self):
        pass
    
    def isBeanAccessor(self):
        pass
    
    def isBeanMutator(self):
        pass
    
    def matchReport(self):
        pass
    

class _JMonitor(_mod_builtins.object):
    __class__ = _JMonitor
    def __enter__(self):
        return self
    
    def __exit__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_jpype'
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _JNumberFloat(_mod_builtins.float,_JObject):
    __class__ = _JNumberFloat
    def __del__(self):
        return None
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __float__(self):
        'float(self)'
        return 0.0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    @classmethod
    def __getformat__(cls, type, typestr):
        "You probably don't want to use this function.\n\n  typestr\n    Must be 'double' or 'float'.\n\nIt exists mainly to be used in Python's test suite.\n\nThis function returns whichever of 'unknown', 'IEEE, big-endian' or 'IEEE,\nlittle-endian' best describes the format of floating point numbers used by the\nC type named by typestr."
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = '_jpype'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __set_format__(cls, type, typestr, fmt):
        "You probably don't want to use this function.\n\n  typestr\n    Must be 'double' or 'float'.\n  fmt\n    Must be one of 'unknown', 'IEEE, big-endian' or 'IEEE, little-endian',\n    and in addition can only be one of the latter two if it appears to\n    match the underlying C reality.\n\nIt exists mainly to be used in Python's test suite.\n\nOverride the automatic determination of C-level floating point type.\nThis affects how floats are converted to and from binary strings."
        pass
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def fromhex(cls, type, string):
        "Create a floating-point number from a hexadecimal string.\n\n>>> float.fromhex('0x1.ffffp10')\n2047.984375\n>>> float.fromhex('-0x1p-1074')\n-5e-324"
        pass
    

class _JNumberLong(_mod_builtins.int,_JObject):
    __class__ = _JNumberLong
    def __del__(self):
        return None
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __float__(self):
        'float(self)'
        return 0.0
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __int__(self):
        'int(self)'
        return 0
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = '_jpype'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def from_bytes(cls, type, bytes, byteorder):
        "Return the integer represented by the given array of bytes.\n\n  bytes\n    Holds the array of bytes to convert.  The argument must either\n    support the buffer protocol or be an iterable object producing bytes.\n    Bytes and bytearray are examples of built-in objects that support the\n    buffer protocol.\n  byteorder\n    The byte order used to represent the integer.  If byteorder is 'big',\n    the most significant byte is at the beginning of the byte array.  If\n    byteorder is 'little', the most significant byte is at the end of the\n    byte array.  To request the native byte order of the host system, use\n    `sys.byteorder' as the byte order value.\n  signed\n    Indicates whether two's complement is used to represent the integer."
        pass
    

class _JObject(_mod_builtins.object):
    __class__ = _JObject
    def __del__(self):
        return None
    
    def __delattr__(self, name):
        'Implement delattr(self, name).'
        return None
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = '_jpype'
    def __setattr__(self, name, value):
        'Implement setattr(self, name, value).'
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class _JProxy(_mod_builtins.object):
    __class__ = _JProxy
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @property
    def __javaclass__(self):
        pass
    
    __module__ = '_jpype'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def toString(self):
        pass
    

__doc__ = 'jpype module'
__file__ = 'c:\\users\\user\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\_jpype.cp37-win_amd64.pyd'
__name__ = '_jpype'
__package__ = ''
__version__ = '0.7.2'
def _getClass():
    pass

def _hasClass():
    pass

def _newArrayType():
    pass

def attach():
    pass

def attachThreadAsDaemon():
    pass

def attachThreadToJVM():
    pass

def convertToDirectBuffer():
    pass

def detachThreadFromJVM():
    pass

def dumpJVMStats():
    pass

def examine():
    pass

def isStarted():
    pass

def isThreadAttachedToJVM():
    pass

def shutdown():
    pass

def startup():
    pass

