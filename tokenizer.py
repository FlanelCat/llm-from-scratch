# Based on https://github.com/rasbt/LLMs-from-scratch/blob/main/ch02/01_main-chapter-code/ch02.ipynb (chapters 2.2 and 2.3)
# with verbose comments added by ChatGPT
# 2026-11-25
import os                                                                                   # Import the os module for interacting with the operating system
import re                                                                                   # Import the re module for regular expressions

class SimpleTokenizerV1:                                                                    # Define a simple tokenizer class named SimpleTokenizerV1
    #
    # Initialize the tokenizer with a vocabulary mapping
    #
    def __init__(self, vocabulary):                                                         # Define the constructor method that takes a vocabulary mapping as an argument
        self.str_to_int = vocabulary                                                        # Store the provided vocabulary mapping from strings to integers
        self.int_to_str = {i:s for s, i in vocabulary.items()}                              # Create a reverse mapping from integers to strings

    #
    # Encode a given text into a list of integer tokens
    #
    def encode(self, text):                                                                 # Define a method to encode a given text into a list of integer tokens
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)                            # Split the input text into tokens based on punctuation and whitespace using a regular expression
        preprocessed = [token.strip() for token in preprocessed if token.strip()]           # Filter out any empty tokens or tokens that are just whitespace
        ids = [self.str_to_int[token] for token in preprocessed]                            # Convert each token to its corresponding integer ID using the vocabulary mapping
        return ids                                                                          # Return the list of integer IDs representing the encoded text

    #
    # Decode a list of integer tokens back into text
    #
    def decode(self, ids):                                                                  # Define a method to decode a list of integer tokens back into text
        text = " ".join([self.int_to_str[i] for i in ids])                                  # Convert each integer ID back to its corresponding token and join them into a single string
        text = re.sub(r'\s([,.:;?_!"()\'])', r'\1', text)                                   # Remove any unnecessary spaces before punctuation using a regular expression
        return text                                                                         # Return the decoded text

#
# Load the text data
#
with open("the-verdict.txt", "r", encoding="utf-8") as f:                                   # Open the file in read mode with UTF-8 encoding
    raw_text = f.read()                                                                     # Read the entire content of the file into the variable 'text'

#
# Preprocess the text
#
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)                                # Split the text into tokens based on punctuation and whitespace using a regular expression
preprocessed = [token.strip() for token in preprocessed if token.strip()]                   #Filter out any empty tokens or tokens that are just whitespace

#
# Prepare the vocabulary
#
all_tokens = sorted(set(preprocessed))                                                      # Create a sorted set of unique tokens from the preprocessed list

#
# Create a mapping from tokens to integers
#
vocabulary = {token:integer for integer, token in enumerate(all_tokens)}                    # Create a dictionary mapping each unique token to a unique integer index

#
# Create an instance of the SimpleTokenizerV1 class using the provided vocabulary mapping
#
tokenizer = SimpleTokenizerV1(vocabulary)                                                   # Create an instance of the SimpleTokenizerV1 class using the provided vocabulary mapping
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride.""" # Define a sample text to be encoded and decoded
ids = tokenizer.encode(text)                                                                # Encode the given text into a list of integer tokens using the tokenizer
print(ids)                                                                                  # Print the list of integer tokens