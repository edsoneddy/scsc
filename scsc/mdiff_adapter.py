from collections import namedtuple
from .constants import ADD_HIGHLIGHT_COLOR, DELETE_HIGHLIGHT_COLOR, END_COLOR

class MdiffAdapter():
    """
    Myers Diff Algorithm (MDIFF) method adapter.
    Original tool: pysimchecker
    """
    Keep = namedtuple('Keep', ['item'])
    Insert = namedtuple('Insert', ['item'])
    Remove = namedtuple('Remove', ['item'])
    Frontier = namedtuple('Frontier', ['x', 'history'])

    def __init__(self):
        self.frontier = {}
        self.history = []

    def compare(self, element_a, element_b):
        return element_a[0] == element_b[0]

    def calculate_edit_distance(self, sequence_a, sequence_b):
        len_a = len(sequence_a)
        len_b = len(sequence_b)
        max_length = len_a + len_b

        if max_length == 0:
            # Both sequences empty: nothing to edit, and v below would only
            # have room for index 0, one short of the v[1] seed it needs.
            return 0

        v = [0] * (2 * max_length + 1)
        v[1] = 0
        for d in range(max_length + 1):
            for k in range(-d, d + 1, 2):
                if k == -d or (k != d and v[k - 1] < v[k + 1]):
                    x = v[k + 1]
                else:
                    x = v[k - 1] + 1
                y = x - k
                while x < len_a and y < len_b and self.compare(sequence_a[x], sequence_b[y]):
                    x += 1
                    y += 1
                v[k] = x
                if x >= len_a and y >= len_b:
                    return d
        return max_length

    def get_similarity_coefficient(self, proccesed_code1, proccesed_code2):
        edit_distance = self.calculate_edit_distance(proccesed_code1, proccesed_code2)
        len_a = len(proccesed_code1)
        len_b = len(proccesed_code2)

        if len_a + len_b == 0:
            # Both files tokenize to nothing: no basis for a match.
            return 0.0
        return (1 - edit_distance / (len_a + len_b))