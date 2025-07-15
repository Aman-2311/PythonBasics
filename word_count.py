import string
from collections import Counter
print("WORD COUNTER")
text = input("Enter the words of your choice : ").lower()
text= text.translate(str.maketrans("","",string.punctuation))
words =text.split()
total_words=len(words)
word_freq = Counter(words)
print("Word Counter Result--")
print(f"Total Words = {total_words}")
print("Word Frequency:")
for word, count in word_freq.items():
  print(f"{word}:{count}")

#str.maketrans(from_chars,to_chars,delete_chars)
