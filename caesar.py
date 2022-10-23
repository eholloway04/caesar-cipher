import string
from nltk.tokenize import word_tokenize
from english_words import english_words_set

def count_matches(text):
  text = word_tokenize(text)
  return sum(i in english_words_set for i in text)

def encode(alphabet, text, shifts):
  # check if shifts is a number...
  try:
    shifts = int(shifts)
  except Exception:
    print("shifts must be an integer!")
    encode(alphabet, input("text: "), input("shifts: "))

  # simplify the number of shifts...
  multiplier = -1 if shifts < 0 else 1
  shifts %= (multiplier * len(alphabet))

  # cipher
  output = ""
  for letter in text:
    # ignore non-alphabetical letters
    if letter.isalpha():
      to_index = alphabet.find(letter) + shifts
      if to_index > (len(alphabet) - 1):
        to_index -= len(alphabet)
      elif to_index < 0:
        to_index += len(alphabet)
      output += alphabet[to_index]
    else:
      output += letter
  return output

def decode(alphabet, text, search_range):
  # check if search range is a number...
  try:
    search_range = int(search_range)
  except Exception:
    print("range must be an integer!")
    decode(alphabet, input("text: "), input("range: "))

  best = ["", 0, 0] # [text, shift, number of matches]
  search_range = abs(search_range)
  for i in range(search_range):
    positive_s = encode(alphabet, text, i)
    negative_s = encode(alphabet, text, -i)

    # process the shifted text...
    cm_p = count_matches(positive_s.lower())
    cm_n = count_matches(negative_s.lower())

    if cm_p >= best[2]:
      best = [positive_s, i, cm_p]
      print(f"new best: {best}")
    if cm_n >= best[2]:
      best = [negative_s, -i, cm_n]
      print(f"new best: {best}")

  return best

# encode(alphabet, input("text: "), input("shifts: "))
# decode(alphabet, input("text: "), input("range: "))