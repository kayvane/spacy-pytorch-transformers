# Stubs for torch.backends.cudnn.rnn (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def get_cudnn_mode(mode: Any): ...

class Unserializable:
    inner: Any = ...
    def __init__(self, inner: Any) -> None: ...
    def get(self): ...

def init_dropout_state(dropout: Any, train: Any, dropout_seed: Any, dropout_state: Any): ...
