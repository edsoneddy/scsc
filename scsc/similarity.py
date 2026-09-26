from .union_find import UnionFind
from .code_preprocessor import CodePreprocessor
from .mdiff_adapter import MdiffAdapter
from .ted_adapter import TedAdapter
from .lf_adapter import LfAdapter
from .gst_adapter import GstAdapter
from .trs_adapter import TrsAdapter
from .csim_adapter import CsimAdapter
from .constants import END_COLOR, DELETE_TEXT_COLOR, ADD_TEXT_COLOR, INFO_TEXT_COLOR, SUPPORTED_METHODS
import csv
import os

def get_similarity_method(method):
    if method == 'ted':
        return TedAdapter()
    elif method == 'mdiff':
        return MdiffAdapter()
    elif method == 'lf':
        return LfAdapter()
    elif method == 'gst':
        return GstAdapter()
    elif method == 'trs':
        return TrsAdapter()
    elif method == 'csim':
        return CsimAdapter()
    # Default method is TED
    return TedAdapter()

def generate_output(file_names, groups, percentage_groups):
    output = ""
    unique_files = []

    for file_group in groups:
        if len(file_group) > 1:
            file_name_src = file_names[file_group[0]]
            for file in file_group[1:]:
                file_name = file_names[file]
                percentage = percentage_groups[file]
                output += (
                    f"{DELETE_TEXT_COLOR}{file_name_src} is similar to {file_name} with similarity percentage: {percentage * 100:.2f}%{END_COLOR}\n"
                )
        else:
            unique_files.append(file_names[file_group[0]])

    if unique_files:
        for file in unique_files:
            output += (f"{ADD_TEXT_COLOR}File that is unique: {file}{END_COLOR}\n")

    return output

def efficient_comparison_output(file_names, file_contents, method, threshold):
    file_number = len(file_names)
    grouper = UnionFind(file_number)
    processor = CodePreprocessor(method)
    similarity_method = get_similarity_method(method)

    proccesed_files = [processor.preprocess_code(file_content, file_name) for file_content, file_name in zip(file_contents, file_names)]
    percentage_file = [0.00] * file_number

    for i in range(file_number - 1):
        if grouper.find(i) == i:
            file_a = proccesed_files[i]
            for j in range(i + 1, file_number):
                if grouper.find(j) == j:
                    file_b = proccesed_files[j]
                    similarity_percentage = similarity_method.get_similarity_coefficient(file_a, file_b)
                    if similarity_percentage > threshold:
                        grouper.union(i, j)
                        percentage_file[j] = similarity_percentage
    
    groups = {}
    
    for i in range(file_number):
        root = grouper.find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    groups = list(groups.values())
    
    return generate_output(file_names, groups, percentage_file)

def full_comparison_output(file_names, file_contents, method, csv_file):
    # Add .csv extension if not present
    if not csv_file.endswith(".csv"):
        csv_file += ".csv"

    file_number = len(file_names)
    processor = CodePreprocessor(method)
    similarity_method = get_similarity_method(method)

    proccesed_files = [processor.preprocess_code(file_content, file_name) for file_content, file_name in zip(file_contents, file_names)]
    
    # Create a matrix to store similarity percentages
    similarity_matrix = [[None for _ in range(file_number + 1)] for _ in range(file_number + 1)]
    
    # Fill the first row and first column with file names
    for i in range(file_number):
        similarity_matrix[0][i + 1] = file_names[i].split('/')[-1].replace('.py','')
        similarity_matrix[i + 1][0] = file_names[i].split('/')[-1].replace('.py','')
    
    # Calculate similarity percentages and fill the matrix
    for i in range(file_number):
        file_a = proccesed_files[i]
        for j in range(file_number):
            if similarity_matrix[i + 1][j + 1] != None:
                continue
            elif i == j:
                similarity_matrix[i + 1][j + 1] = 1.00
            else:
                file_b = proccesed_files[j]
                similarity_percentage = similarity_method.get_similarity_coefficient(file_a, file_b)
                similarity_matrix[i + 1][j + 1] = round(similarity_percentage, 2)
                similarity_matrix[j + 1][i + 1] = round(similarity_percentage, 2)
    
    # Write the matrix to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(similarity_matrix)
    
    return f"Full comparison report generated: {csv_file}"

def similarity_checker(file_names, file_contents, args):
    # Get the arguments
    csv_file = args.all
    method = args.method
    threshold = args.threshold

    methods = SUPPORTED_METHODS if method == "all" else [method]
    outputs = []

    for m in methods:
        if csv_file:
            # Run every method into its own CSV so they don't clobber
            # each other: results.csv -> results_ted.csv, results_mdiff.csv, ...
            target_csv = csv_file
            if method == "all":
                base, ext = os.path.splitext(csv_file)
                target_csv = f"{base}_{m}{ext}"
            output = full_comparison_output(file_names, file_contents, m, target_csv)
        else:
            output = efficient_comparison_output(file_names, file_contents, m, threshold)

        if method == "all":
            output = f"{INFO_TEXT_COLOR}=== {m} ==={END_COLOR}\n{output}"
        outputs.append(output)

    return "\n".join(outputs)