# Stubs for torch.autograd (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .function import Function as Function
from .variable import Variable as Variable
from typing import Any, Optional

def backward(tensors: Any, grad_tensors: Optional[Any] = ..., retain_graph: Optional[Any] = ..., create_graph: bool = ..., grad_variables: Optional[Any] = ...) -> None: ...

# Names in __all__ with no definition:
#   grad_mode
