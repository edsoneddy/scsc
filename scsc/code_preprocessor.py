from .constants import IRRELEVANT_TOKENS, TOKENS_WITHOUT_TRANSFORMATION
from pygments import lex
from pygments.token import STANDARD_TYPES
from pygments.lexers import PythonLexer
from csim import ANTLR_parse
from csim import Normalize, PruneAndHash
from .gst_adapter import SignatureFactory
import os

# Code Preprocessor, includes methods for preprocessing code
class CodePreprocessor:

    def __init__(self, method):
        self.method = method
        self.token_table = self.create_token_table()
        self.lexer = PythonLexer()

    def add_main(self, source_code):
        if ('def main():' in source_code):
            return source_code
        
        code_lines = str(source_code).split('\n')
        code_lines = ['\t' + line + '\n' for line in code_lines]
        code_fixed = ['def main():\n'] + code_lines

        return ''.join(code_fixed)
    
    def create_token_table(self):
        token_table = {}

        for type_key in STANDARD_TYPES.keys():
            token_table[type_key] = len(token_table)
        
        return token_table

    def tokenize_code(self, code_string):
        tokens = []

        for token in lex(code_string, self.lexer):
            token_type = token[0]
            token_str = token[1]
            if token_type not in IRRELEVANT_TOKENS:
                # TODO: the token table should be created based on the tokens found in the code
                if token_type in TOKENS_WITHOUT_TRANSFORMATION or not token_type in self.token_table:
                    token_content = [token_str, token_str]
                else:
                    token_content = [self.token_table[token_type], token_str]
                tokens.append(token_content)
        
        return tokens
    
    def tokenize_and_hash_code(self, code_string):
        # Tokenize the code string and hash the tokens
        tokens = self.tokenize_code(code_string)
        token_hashes = [hash(tuple(token)) for token in tokens]
        return token_hashes
    
    def normalize_code(self, file_name, code_string, lang = 'python'):
        T1 = ANTLR_parse(file_name, code_string, lang)
        normalized_tree = Normalize(T1, lang)
        pruned_tree, pruned_count = PruneAndHash(normalized_tree, lang)

        return pruned_tree, pruned_count
    
    def get_abspath_and_content(self, file_name, file_content):
        if file_name is None:
            return None, file_content
        return os.path.abspath(file_name), file_content
    
    def get_signature(self, code_string):
        return SignatureFactory(code_string)

    def preprocess_code(self, code_string, file_name = ''):
        if self.method == 'ted':
            return self.add_main(code_string)
        elif self.method == 'mdiff':
            return self.tokenize_code(code_string)
        elif self.method == 'lf':
            return self.get_abspath_and_content(file_name, code_string)
        elif self.method == 'gst':
            return self.get_signature(code_string)
        elif self.method == 'trs':
            return self.tokenize_and_hash_code(code_string)
        elif self.method == 'csim':
            return self.normalize_code(file_name, code_string)
        
        # Default method return the same code
        return self.add_main(code_string)