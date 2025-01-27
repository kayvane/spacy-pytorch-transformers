# Stubs for pytorch_transformers.tokenization_gpt2 (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .tokenization_utils import PreTrainedTokenizer, clean_up_tokenization
from typing import Any

logger: Any
VOCAB_FILES_NAMES: Any
PRETRAINED_VOCAB_FILES_MAP: Any
PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES: Any

def bytes_to_unicode(): ...
def get_pairs(word: Any): ...

class GPT2Tokenizer(PreTrainedTokenizer):
    vocab_files_names: Any = ...
    pretrained_vocab_files_map: Any = ...
    max_model_input_sizes: Any = ...
    encoder: Any = ...
    decoder: Any = ...
    errors: Any = ...
    byte_encoder: Any = ...
    byte_decoder: Any = ...
    bpe_ranks: Any = ...
    cache: Any = ...
    pat: Any = ...
    def __init__(self, vocab_file: Any, merges_file: Any, errors: str = ..., bos_token: str = ..., eos_token: str = ..., **kwargs: Any) -> None: ...
    @property
    def vocab_size(self): ...
    def bpe(self, token: Any): ...
    def convert_tokens_to_string(self, tokens: Any): ...
    def save_vocabulary(self, save_directory: Any): ...
