# Based on https://github.com/rasbt/LLMs-from-scratch/blob/main/ch02/01_main-chapter-code/ch02.ipynb (chapters 2.2 and 2.3)
# with verbose comments added by ChatGPT
# 2026-11-25
import os                                                                   # Import the os module for interacting with the operating system
import re                                                                   # Import the re module for regular expressions

#
# Load the text data
#
with open("the-verdict.txt", "r", encoding="utf-8") as f:                   # Open the file in read mode with UTF-8 encoding
    raw_text = f.read()                                                     # Read the entire content of the file into the variable 'text'
print(f"Length of text: {len(raw_text):,} characters")                      # Print the length of the text with thousands separator
#print(f"First 99 characters:\n{raw_text[:99]}")                             # Print the first 99 characters of the text

#
# Preprocess the text
#
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)                # Split the text into tokens based on punctuation and whitespace using a regular expression
preprocessed = [token.strip() for token in preprocessed if token.strip()]   # Filter out any empty tokens or tokens that are just whitespace
#print('preprocessed = ', preprocessed[:99])                                 # Print the first 99 tokens of the preprocessed list

#
# Prepare the vocabulary
#
all_tokens = sorted(set(preprocessed))                                      # Create a sorted set of unique tokens from the preprocessed list
vocabulary_size = len(all_tokens)                                           # Calculate the size of the vocabulary (number of unique tokens)
print(f"Vocabulary size: {vocabulary_size:,} tokens")                       # Print the vocabulary size with thousands separator

#
# Create a mapping from tokens to integers
#
vocabulary = {token:integer for integer, token in enumerate(all_tokens)}    # Create a dictionary mapping each unique token to a unique integer index
#for i, token in enumerate(vocabulary.items()):                              # Loop through the vocabulary items (token, integer pairs) with an index
#    if i < 50:                                                              # Limit the output to the first 50 items
#        print(token)                                                        # Print each token and its corresponding integer index
