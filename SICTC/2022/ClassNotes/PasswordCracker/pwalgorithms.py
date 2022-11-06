# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    print(w)
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

# analyze a one-word password
def two_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    for w2 in words:
      guesses += 1
      if (w+w2 == password or w2+w == password):
        return True, guesses
  return False, guesses

# analyze a one-word password
def two_word_and_digit(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    for w2 in words:
      guesses += 1
      if (w+w2 == password or w2+w == password):
        return True, guesses
      for i in range(10):
        i = str(i)
        guesses += 1
        if (w+w2+i == password or w2+w+i == password or i+w+w2 == password or i+w2+w == password):
          return True, guesses
  return False, guesses