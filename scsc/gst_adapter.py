# Original author: andresbejarano
# Original repository: https://github.com/andresbejarano/Codesight

"""
Token.java

Desarrollado por: Andres Mauricio Bejarano Posada
Construida en: NetBeans IDE 5.5

Clase que almacena la informacion correspondiente a una ficha (token).

Esta clase almacena los datos en las siguientes variables:
    -> Token: almacena el tipo de ficha a la que corresponde.
    -> Word: Almacena la palabra o simbolo a la que esta asociada la ficha.
    -> Line: Indica el numero de linea a la que pertenece la ficha.
    -> Mark: Indica si la ficha ha sido marcada para el proceso de 
        identificacion de las fichas solapadas.
"""

class Token:
    
    def __init__(self, token, word, line):
        self.Token = token
        self.Word = word
        self.Line = line
        self.Mark = False
    
    def getData(self):
        return [self.Token, self.Word, self.Line, self.Mark]
    
    def getLine(self):
        return self.Line
    
    def getMark(self):
        return self.Mark
    
    def getToken(self):
        return self.Token
    
    def getWord(self):
        return self.Word
    
    def mark(self):
        self.Mark = True
    
    def unmark(self):
        self.Mark = False
    
    def copy(self):
        copy = Token(self.Token, self.Word, self.Line)
        if self.Mark:
            copy.mark()
        return copy

"""
Signature.java

Desarrollado por: Andres Mauricio Bejarano Posada
Construida en: NetBeans IDE 5.5

Esta clase se encarga de definir una serie de tokens dependiendo del código
fuente que se le ingrese. Se denomina Signature (firma) ya que es única por
código, lo que significa que el orden de la secuencia que se genera es único
por archivo, a menos que existan otros códigos exactamente iguales.

Esta clase almacena la información de la siguiente forma:
    -> file: Objeto de la clase File que hace referencia al archivo que es analizado.
    -> totalLines: Indica el número total de líneas que tiene el archivo, esto incluye líneas en blanco y comentarios.
    -> LexicalStream: Es una cadena donde está el mismo código pero transformado en una serie de fichas (tokens).
    -> Tokens: Vector donde se almacenan las fichas.
    -> Punctuation: Vector estático donde se definene todos los simbolos que se usan en la codificación en C++.
    -> ReservedWords: Vector estatico donde se definen todas las palabras reservadas del lenguaje C++.
"""
import os

class Signature:
    
    Punctuation = [" ", "\t", ".", ",", "<", ">", "/", "?", ";", ":", "'", "\"", "~", "[", "]", "{", "}", "\\", "|", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "^"]
    ReservedWords = ["asm", "auto", "bool", "break", "case", "catch", "char", "class", "const", "continue", "default", "delete", "do", "double", "else", "enum", "extern", "float", "for", "friend", "goto", "if", "inline", "int", "long", "namespace", "new", "operator", "private", "protected", "public", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "template", "this", "throw", "try", "typedef", "union", "unsigned", "using", "virtual", "void", "volatile", "while"]
    
    def __init__(self, file_path):
        self.file = file_path
        self.LexicalStream = ""
        self.Tokens = []
        line_counter = 0
        
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line_counter += 1
                    line = self.trimComments(line.strip())
                    words = self.separateWords(line.strip())
                    if words:
                        line_tokens = self.getLexicalStream(words).split(" ")
                        for i in range(len(words)):
                            self.Tokens.append(Token(line_tokens[i], words[i], line_counter))
                            self.LexicalStream += " " + line_tokens[i]
        except Exception as e:
            print(e)
        
        self.totalLines = line_counter
        self.LexicalStream = self.LexicalStream.strip()
    
    def trimComments(self, line):
        if len(line) > 1 and line[:2] == "//":
            return ""
        # Codesight targets C++ ("//"); this project only ever feeds it
        # Python, whose comment marker is "#" (also used trailing, not just
        # full-line) - without stripping it, comment text is tokenized as
        # code and two structurally identical files with different comments
        # look artificially dissimilar.
        if "#" in line:
            line = line.split("#", 1)[0]
        return line
    
    def toString(self, vector):
        return " ".join(vector).strip()
    
    def copy(self):
        return Signature(self.file)
    
    def getFile(self):
        return self.file
    
    def getFileName(self):
        return os.path.basename(self.file)
    
    def getTotalLines(self):
        return self.totalLines
    
    def getNumTokens(self):
        return len(self.Tokens)
    
    def getLexicalStream(self):
        return self.LexicalStream
    
    def getLexicalStream(self, words):
        stream = ""
        for token in words:
            if self.isReservedWord(token):
                stream += " LITERAL_" + token
            elif self.isPunctuation(token):
                stream += " " + self.getPunctuationToken(token)
            elif self.isInt(token):
                stream += " NUM_INT"
            elif self.isFloat(token):
                stream += " NUM_FLOAT"
            elif self.isDouble(token):
                stream += " NUM_DOUBLE"
            elif self.isLong(token):
                stream += " NUM_LONG"
            else:
                stream += " IDENT"
        return stream.strip()
    
    def getWords(self):
        return [token.getWord() for token in self.Tokens]
    
    def getTokens(self):
        return [token.getToken() for token in self.Tokens]
    
    def getMarks(self):
        return [token.getMark() for token in self.Tokens]
    
    def getTokenData(self):
        return [token.copy() for token in self.Tokens]
    
    def isDouble(self, word):
        try:
            float(word)
            return True
        except ValueError:
            return False
    
    def isInt(self, word):
        try:
            int(word)
            return True
        except ValueError:
            return False
    
    def isFloat(self, word):
        try:
            float(word)
            return True
        except ValueError:
            return False
    
    def isLong(self, word):
        try:
            int(word)
            return True
        except ValueError:
            return False
    
    def isPunctuation(self, letter):
        return letter in self.Punctuation
    
    def isReservedWord(self, word):
        return word in self.ReservedWords
    
    def getPunctuationToken(self, token):
        punctuation_map = {
            "(": "LPAREN", ")": "RPAREN", "{": "LCURLY", "}": "RCURLY",
            "[": "LBRACK", "]": "RBRACK", "=": "ASSIGN", "<": "LT",
            ">": "BT", "+": "PLUS", "-": "MINUS", "*": "TIMES",
            "/": "DIV", "?": "QUEST", "!": "ADMIR", ",": "COMMA",
            ".": "DOT", ";": "SEMI", ":": "TWODOT", "@": "AT",
            "#": "SHARP", "%": "PERCENT", "\"": "QUOTE", "&": "AMPERS",
            "$": "DOLLAR", "\\": "BCKSLSH", "'": "SQUOTE", "~": "TILDE",
            "^": "CARET", "|": "VERBAR"
        }
        return punctuation_map.get(token, "")
    
    def mark(self, index):
        self.Tokens[index].mark()
    
    def unmark(self, index):
        self.Tokens[index].unmark()
    
    def separateWords(self, line):
        words = []
        i = 0
        while i < len(line):
            if self.isPunctuation(line[i]):
                if i == 0:
                    words.append(line[i].strip())
                else:
                    words.append(line[:i])
                    if line[i].strip():
                        words.append(line[i])
                line = line[i + 1:].strip()
                i = 0
            else:
                i += 1
        if i == len(line) and line.strip():
            words.append(line)
        return words
    
# Signature override class, to be used as adapter
class SignatureFactory(Signature):
    def __init__(self, file_content):
        self.file = file_content
        self.LexicalStream = ""
        self.Tokens = []
        line_counter = 0
        
        # file_content is a string with the code lines
        for line in file_content.splitlines():
            line_counter += 1
            line = self.trimComments(line.strip())
            words = self.separateWords(line.strip())
            if words:
                line_tokens = self.getLexicalStream(words).split(" ")
                for i in range(len(words)):
                    self.Tokens.append(Token(line_tokens[i], words[i], line_counter))
                    self.LexicalStream += " " + line_tokens[i]
        
        self.totalLines = line_counter
        self.LexicalStream = self.LexicalStream.strip()

"""
Match.java

Desarrollado por: Andres Mauricio Bejarano Posada
Construida en: NetBeans IDE 5.5

Almacena los datos de la comparación de los archivos y se encarga de
mostrarlos de una forma ordenada dependiendo del metodo invocado.

Esta clase almacena la información de la siguiente manera:
    -> Code1 y Code2: Almacenan los indices de inicio de las secuencias similares en ambos archivos respectivamente.
    -> Count: Almacena por indice la cantidad de fichas que tiene de longitud la secuencia que está en comun en ambos archivos.
    -> Checked: Vector de datos booleanos donde se indica si la secuencia ha sido marcada como valida o no para ser mostrada.
    -> Threshold: Almacena el valor del umbral de comparación.
    -> Sig1 y Sig2: Hacen referencias a las firmas (Signatures) de los archivos que son comparados.
    -> Color: Matriz donde se almacenan los colores con los que van a ser mostradas las lineas que aparecen como copiadas.
"""

class Match:
    
    colors = [
        [143, 231, 37], [244, 24, 181], [76, 148, 192], [173, 180, 88],
        [212, 160, 56], [246, 22, 70], [120, 92, 176], [165, 215, 53],
        [165, 121, 103], [231, 37, 143], [24, 181, 244], [148, 192, 76],
        [180, 88, 173], [160, 56, 212], [22, 70, 246], [92, 176, 120],
        [215, 53, 165], [121, 103, 165], [231, 143, 37], [24, 244, 181],
        [148, 76, 192], [180, 173, 88], [160, 212, 56], [22, 246, 70],
        [92, 120, 176], [215, 165, 53], [121, 165, 103], [37, 143, 231],
        [181, 244, 24], [192, 76, 148], [88, 173, 180], [56, 212, 160],
        [70, 246, 22], [176, 120, 92], [53, 165, 215], [103, 165, 121]
    ]
    
    def __init__(self, sig1, sig2, tokens1, tokens2, threshold):
        self.Sig1 = sig1
        self.Sig2 = sig2
        self.Tokens1 = tokens1
        self.Tokens2 = tokens2
        self.Threshold = threshold
        self.Code1 = []
        self.Code2 = []
        self.Count = []
        self.Checked = []
    
    def add(self, i, j, k):
        self.Code1.append(i)
        self.Code2.append(j)
        self.Count.append(k)
        self.Checked.append(False)
    
    def getSize(self):
        return len(self.Code1)
    
    def getData(self):
        return [[self.Code1[i], self.Code2[i], self.Count[i]] for i in range(len(self.Code1))]
    
    def getIntegerData(self):
        return [[self.Code1[i], self.Code2[i], self.Count[i]] for i in range(len(self.Code1)) if self.Checked[i]]
    
    def getObjectData(self):
        return [[j + 1, self.Code1[i], self.Code2[i], self.Count[i], ""] for j, i in enumerate(range(len(self.Code1))) if self.Checked[i]]
    
    def countChecked(self):
        return sum(self.Checked)
    
    def getTokenData(self, select):
        data = []
        tokens = self.Tokens1 if select == 1 else self.Tokens2
        for i, token in enumerate(tokens):
            data.append([i, token.getToken(), token.getWord(), token.getLine(), token.getMark()])
        return data
    
    def switchPosition(self, i, j):
        self.Code1[i], self.Code1[j] = self.Code1[j], self.Code1[i]
        self.Code2[i], self.Code2[j] = self.Code2[j], self.Code2[i]
        self.Count[i], self.Count[j] = self.Count[j], self.Count[i]
    
    def Sort(self, type):
        for i in range(len(self.Count)):
            for j in range(i + 1, len(self.Count)):
                if type == 1 and self.Code1[j] > self.Code1[i]:
                    self.switchPosition(i, j)
                elif type == 2 and self.Code2[j] > self.Code2[i]:
                    self.switchPosition(i, j)
                elif type == 3 and self.Count[j] > self.Count[i]:
                    self.switchPosition(i, j)
    
    def mark(self):
        for i in range(self.getSize()):
            a = self.Code1[i]
            b = self.Code2[i]
            count = self.Count[i]
            ini = 0
            while ini < count and not self.Tokens1[a + ini].getMark() and not self.Tokens2[b + ini].getMark():
                ini += 1
            if ini == count:
                for ini in range(count):
                    self.Tokens1[a + ini].mark()
                    self.Tokens2[b + ini].mark()
                self.Checked[i] = True
    
    def getTokensLength(self, id):
        return len(self.Tokens1) if id == 1 else len(self.Tokens2)
    
    def getSignature(self, num):
        return self.Sig1 if num == 1 else self.Sig2
    
"""
Codesight.java

Desarrollado por: Andres Mauricio Bejarano Posada
Construida en: NetBeans IDE 5.5

Esta clase es la principal en la aplicación pues es la que maneja la lógica
de analisis, transformación, comparación y medición del código copiado.

La clase almacena la información en las siguientes referencias:
    -> Files: Vector donde se guardan los objetos File correspondiente a cada uno de los archivos leidos en la carpeta pasada por parámetro.
    -> Signatures: Vector de objetos de la clase Signature que contienen las secuencias de fichas (tokens) de los diferentes archivos.
"""

class GstAdapter:
    """
    Greedy String Tiling (GST) method adapter.
    Original tool: Codesight by Andres Mauricio Bejarano Posada
    Repository: https://github.com/andresbejarano/Codesight
    """
    
    def get_similarity_coefficient(self, proccesed_code1, proccesed_code2):
        similarity_coefficient = 0.0

        # arguments for the codesight method
        args = {
            "Threshold": 10,
        }

        SignatureA = proccesed_code1
        SignatureB = proccesed_code2

        # greedyStringTiling
        A = SignatureA.getTokenData()
        B = SignatureB.getTokenData()
        matches = Match(SignatureA, SignatureB, A, B, args["Threshold"])
        maxmatch = args["Threshold"]
        for a in range(SignatureA.getNumTokens()):
            for b in range(SignatureB.getNumTokens()):
                j = 0
                while ((a + j) < SignatureA.getNumTokens()) and ((b + j) < SignatureB.getNumTokens()) and (A[a + j].getToken() == B[b + j].getToken()) and not A[a + j].getMark() and not B[b + j].getMark():
                    j += 1
                if j > 0 and j >= maxmatch:
                    matches.add(a,b,j)
        if matches.getSize() > 0:
            matches.Sort(3)
            matches.mark()
		
        # getPercentMatch
        percent = 1
        coverage = 0
        total = 0
        copiedSequences = matches.countChecked()
        data = matches.getIntegerData()
        for i in range(copiedSequences):
            coverage += data[i][2]
        total = matches.getTokensLength(1) + matches.getTokensLength(2)
        # Both files tokenize to nothing (empty / whitespace-only content):
        # there is no basis for a match, so treat them as 0% similar instead
        # of dividing by zero.
        percent = (2 * coverage) / total if total > 0 else 0.0
        similarity_coefficient = round(percent, 2)
        
        return similarity_coefficient