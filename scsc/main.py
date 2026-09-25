import argparse
from .file_utils import process_files, get_file, get_threshold
from .similarity import similarity_checker
from .constants import SUPPORTED_METHODS

def main():
    """
    Main function to parse command-line arguments and execute the similarity checker.
    Arguments:
        --path, -p (str): Path to the directory containing the source code files.
        --files, -f (str, nargs=2): The input two files to compare.
        --recursive, -r (bool): Recursively search through directories.
        --threshold, -t (float): The similarity threshold (default: 0.75, range: 0.0 - 1.0).
        --method, -m (str): The method to use for similarity detection (default: ted). Pass 'all' to run every supported method.
    Returns:
        None
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description='scsc: Detect similarity between source codes.')
    
    # Create a mutually exclusive group
    group = parser.add_mutually_exclusive_group(required=True)
    
    # Add the 'path' argument to the group
    group.add_argument('--path', '-p', type=str, help='Path to the directory containing the source code files')
    
    # Add the 'files' argument to the group
    group.add_argument('--files', '-f', type=get_file, nargs=2, help='The input two files to compare')
    
    # Add the 'recursive' argument
    parser.add_argument('--recursive', '-r', action='store_true', help='Recursively search through directories')

    # Add the 'threshold' argument with range validation (0.0 - 1.0)
    parser.add_argument('--threshold', '-t', type=get_threshold, default=0.75, help='The similarity threshold (default: 0.75, range: 0.0 - 1.0)')
    
    # Add the 'method' argument
    parser.add_argument('--method', '-m', type=str, choices=SUPPORTED_METHODS + ['all'], default='ted', help="The method to use for similarity detection (default: ted). Use 'all' to run every method")

    # Add the full comparison argument
    parser.add_argument('--all', '-a', type=str, help='Compare each file with every other file and output the results to the specified CSV file')

    # Parse the arguments
    args = parser.parse_args()
    
    # Process the files
    file_names, file_contents = process_files(args)

    if len(file_names) > 1:
        try:
            results = similarity_checker(file_names, file_contents, args)
            print(results)
        except Exception as e:
            print("An error occurred during similarity checking.", e)
    else:
        print("No files to compare.")

if __name__ == "__main__":
    main()