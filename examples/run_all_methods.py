code_a = """
def compute_stats(values):
    total = 0
    product = 1
    count = 0
    running_max = values[0]
    for v in values:
        total += v
        product *= v
        count += 1
        if v > running_max:
            running_max = v
    total -= 10
    product //= 2
    count *= 1
    average = total / count
    return total, product, average, running_max
"""
code_b = """
def compute_stats(values):
    total = 0
    product = 1
    count = 0
    running_max = values[0]
    for v in values:
        total = total + v
        product = product * v
        count = count + 1
        if v > running_max:
            running_max = v
    total = total - 10
    product = product // 2
    count = count * 1
    average = total / count
    return total, product, average, running_max
"""
# code_a uses augmented assignments (+=, *=, //=, ...); code_b spells the
# same operations out (x = x + v, ...). Semantically identical - csim's
# ANTLR visitor explicitly rewrites augmented assignments into the expanded
# form before comparing (see PythonParserVisitorExtended.visitAssignment in
# the csim package), so it scores this pair 1.0. The other methods compare
# tokens/AST nodes as-is - "+=" and "= ... +" are literally different tokens
# (mdiff, trs, lf, gst) or different ast node types, AugAssign vs Assign+BinOp
# (ted) - so none of them recognize the equivalence, landing well below 1.0.

from scsc import Compare

similarity_index = Compare(code_a, code_b, method="ted")
print(f"Similarity Index (ted): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="mdiff")
print(f"Similarity Index (mdiff): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="trs")
print(f"Similarity Index (trs): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="csim")
print(f"Similarity Index (csim): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="gst")
print(f"Similarity Index (gst): {similarity_index}")

similarity_index = Compare(code_a, code_b, method="lf")
print(f"Similarity Index (lf): {similarity_index}")