# Stubs for torch.optim.adagrad (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .optimizer import Optimizer
from typing import Any, Optional

class Adagrad(Optimizer):
    def __init__(self, params: Any, lr: float = ..., lr_decay: int = ..., weight_decay: int = ..., initial_accumulator_value: int = ...) -> None: ...
    def share_memory(self) -> None: ...
    def step(self, closure: Optional[Any] = ...): ...
