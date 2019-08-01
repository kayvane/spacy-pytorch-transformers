# Stubs for torch._thnn.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .._utils_internal import get_file_path
from typing import Any

THNN_H_PATH: Any
THCUNN_H_PATH: Any

class THNNBackendBase:
    methods: Any = ...
    def __init__(self) -> None: ...
    def __getattr__(self, name: Any): ...
    def register_method(self, name: Any, ctypes_fn: Any) -> None: ...
    @property
    def library_state(self): ...
    def __reduce__(self): ...

class Function:
    name: Any = ...
    arguments: Any = ...
    def __init__(self, name: Any) -> None: ...
    def add_argument(self, arg: Any) -> None: ...

class Argument:
    type: Any = ...
    name: Any = ...
    is_optional: Any = ...
    def __init__(self, _type: Any, name: Any, is_optional: Any) -> None: ...

def parse_header(path: Any): ...
def load_backend(t: Any, lib: Any, generic_functions: Any, mixins: Any = ...): ...