from csim import SimilarityIndex
from csim.processing.distance_metrics import TreeEditDistance

class CsimAdapter():
    """
    Code Similarity (CSIM) method adapter.
    Combines Parse Trees and Tree Edit Distance for code structure analysis.
    """

    def get_similarity_coefficient(self, proccesed_code1, proccesed_code2):
        N1, len_N1 = proccesed_code1
        N2, len_N2 = proccesed_code2
        d = TreeEditDistance(N1, N2)
        result = SimilarityIndex(d, len_N1, len_N2)
        return result