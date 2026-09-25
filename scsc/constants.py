from pygments.token import Token

# Single source of truth for the method names accepted by --method/-m,
# shared by the CLI, SimilarityChecker.Compare and similarity_checker so
# they can't silently drift apart.
SUPPORTED_METHODS = ["ted", "mdiff", "trs", "csim", "gst", "lf"]

# Constants for filtering irrelevant tokens
IRRELEVANT_TOKENS = {
    Token.Comment,
    # Token.Comment.Hashbang,
    # Token.Comment.Multiline,
    # Token.Comment.Preproc,
    # Token.Comment.PreprocFile,
    # Token.Comment.Single,
    # Token.Comment.Special,
    # Token.Text,
    # Token.Whitespace,
    # Token.Punctuation,
    # Token.Punctuation.Marker,
    # Token.String.Doc,
    # Token.Generic,
    # Token.Generic.Deleted,
    # Token.Generic.Emph,
    # Token.Generic.Error,
    # Token.Generic.Heading,
    # Token.Generic.Inserted,
    # Token.Generic.Output,
    # Token.Generic.Prompt,
    # Token.Generic.Strong,
    # Token.Generic.EmphStrong,
    # Token.Generic.Subheading,
    # Token.Generic.Traceback,
    # Token.Keyword.Namespace,
}

TOKENS_WITHOUT_TRANSFORMATION = {
    Token.Punctuation,
    Token.Operator,
    Token.Keyword,
    Token.Text.Whitespace,
}

# Constants for the Myers' Algorithm
KEEP = 'K'
ADD = '+'
DELETE = '-'

"""
ANSI escape codes for text formatting in the terminal.
Reference: https://en.wikipedia.org/wiki/ANSI_escape_code
"""
# highlight colors
ADD_HIGHLIGHT_COLOR = '\033[42m'
DELETE_HIGHLIGHT_COLOR = '\033[41m'
END_COLOR = '\033[0m'

# text colors
ADD_TEXT_COLOR = '\033[32m'
DELETE_TEXT_COLOR = '\033[31m'
INFO_TEXT_COLOR = '\033[33m'