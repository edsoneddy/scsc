from .code_preprocessor import CodePreprocessor
from .similarity import get_similarity_method
from .constants import SUPPORTED_METHODS


def Compare(code_a, code_b, method):
    similarity_index = None
    if method in SUPPORTED_METHODS:
        processor = CodePreprocessor(method)
        similarity_method = get_similarity_method(method)

        processed_code_a = processor.preprocess_code(code_a, None)
        processed_code_b = processor.preprocess_code(code_b, None)
        similarity_index = similarity_method.get_similarity_coefficient(
            processed_code_a, processed_code_b
        )

    return similarity_index
