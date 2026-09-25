def process_word(word):
  word = ''.join(c for c in word if c.isalpha() or c == '-')
  return word.lower()

def get_words(text):
  words = set()
  current_word = ""

  lines = text.split('\n')
  for i, line in enumerate(lines):
      words_in_line = line.strip().split()

      for j, word in enumerate(words_in_line):
          if current_word:
              if current_word.endswith('-'):
                  current_word = current_word[:-1] + word
              else:
                  processed_word = process_word(current_word)
                  if processed_word:
                      words.add(processed_word)
                  current_word = word
          else:
              current_word = word
          if j == len(words_in_line) - 1:
              if word.endswith('-'):
                  continue
              else:
                  processed_word = process_word(current_word)
                  if processed_word:
                      words.add(processed_word)
                  current_word = ""
  if current_word:
      processed_word = process_word(current_word)
      if processed_word:
          words.add(processed_word)

  return sorted(list(words))


text = ""
try:
  while True:
      line = input()
      text += line + "\n"
except EOFError:
  pass

result = get_words(text)
for word in result:
  print(word)
