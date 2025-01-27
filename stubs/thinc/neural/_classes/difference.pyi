# Stubs for thinc.neural._classes.difference (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .. import Model
from ...api import layerize
from ...describe import Dimension, Gradient, Synapses
from typing import Any

def inverse(total: Any): ...
def Siamese(layer: Any, similarity: Any): ...
def unit_init(W: Any, ops: Any) -> None: ...

class CauchySimilarity(Model):
    nO: Any = ...
    def __init__(self, length: Any) -> None: ...
    def begin_update(self, vec1_vec2: Any, drop: float = ...): ...
