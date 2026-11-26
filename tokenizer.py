# Based on https://github.com/rasbt/LLMs-from-scratch/blob/main/ch02/01_main-chapter-code/ch02.ipynb (chapters 2.2 to 2.6)
# with verbose comments added by ChatGPT
# 2026-11-25 - 2026-11-26
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

class SimpleTokenizerV2:                                                                    # Define a simple tokenizer class named SimpleTokenizerV2
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
        ids = [self.str_to_int.get(token, self.str_to_int["|<unk>|"]) for token in preprocessed]  # Convert each token to its corresponding integer ID using the vocabulary mapping, using "|<unk>|" for unknown tokens
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
all_tokens = sorted(list(set(preprocessed)))                                                # Create a sorted set of unique tokens from the preprocessed list
all_tokens.extend(["<|endoftext|>","<|unk|>"])                                              # Add special tokens for end of text and unknown tokens to the vocabulary

#
# Create a mapping from tokens to integers
#
vocabulary = {token:integer for integer, token in enumerate(all_tokens)}                    # Create a dictionary mapping each unique token to a unique integer index
#print(len(vocabulary.items()))                                                              # Print the number of unique tokens in the vocabulary
#for token, index in list(vocabulary.items())[-5:]:                                          # Loop through the first 50 items in the vocabulary mapping
#    print(f"'{token}': {index}")

#
# Create an instance of the SimpleTokenizerV1 class using the provided vocabulary mapping
#
tokenizer = SimpleTokenizerV1(vocabulary)                                                   # Create an instance of the SimpleTokenizerV1 class using the provided vocabulary mapping
text = """"It's the last he painted, you know," Mrs. Gisburn said with pardonable pride.""" # Define a sample text to be encoded and decoded
ids = tokenizer.encode(text)                                                                # Encode the given text into a list of integer tokens using the tokenizer
#print(ids)                                                                                  # Print the list of integer tokens
#print(tokenizer.decode(ids))                                                                # Print the decoded text

#
# Create an instance of the SimpleTokenizerV2 class using the provided vocabulary mapping
#
text1 = "Hello, do you like tea?"                                                           # Define a sample text to be encoded and decoded
text2 = "In the sunlit terraces of the palace."                                             # Define a sample text to be encoded and decoded
text = "<|endoftext|> ".join([text1, text2])                                                 # Join the two sample texts with the end of text token
#print(text)                                                                                 # Print the combined text
tokenizer = SimpleTokenizerV2(vocabulary)                                                   # Create an instance of the SimpleTokenizerV2
#print(tokenizer.encode(text))                                                               # Encode the combined text into a list of integer tokens using the tokenizer
#print(tokenizer.decode(tokenizer.encode(text)))                                             # Decode the list of integer tokens back into text and print it

#
# Check the version of the tiktoken module
#
from importlib.metadata import version                                                      # Import the version function from the importlib.metadata module
import tiktoken                                                                             # Import the tiktoken module for tokenization
#print(f"tiktoken version: {version('tiktoken')}")                                           # Print the version of the tiktoken module

#
# Create a tokenizer using the tiktoken module
#
tokenizer = tiktoken.get_encoding("gpt2")                                                   # Get the tokenizer encoding for "gpt2" from the tiktoken module
#text = "Hello, do you like tea? <|endoftext|> In the sunlit terraces of someunknownPlace."  # Define a sample text to be encoded and decoded
#integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})                        # Encode the text into a list of integer tokens, allowing the special token "<|endoftext|>"
#print(integers)                                                                             # Print the list of integer tokens
#strings = tokenizer.decode(integers)                                                        # Decode the list of integer tokens back into text
#print(strings)                                                                              # Print the decoded text
#text = "Akwirw ier"                                                                         # Define a sample text to be encoded and decoded
#integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})                        # Encode the text into a list of integer tokens, allowing the special token "<|endoftext|>"
#print(integers)                                                                             # Print the list of integer tokens
#strings = tokenizer.decode(integers)                                                        # Decode the list of integer tokens back into text
#print(strings)                                                                              # Print the decoded text

#
# Load the text data and encode it using the tokenizer
#
with open("the-verdict.txt", "r", encoding="utf-8") as f:                                   # Open the file in read mode with UTF-8 encoding
    raw_text = f.read()                                                                     # Read the entire content of the file into the variable 'text'
encoded_text = tokenizer.encode(raw_text)                                                   # Encode the raw text into a list of integer tokens
#print(f"Length of encoded text: {len(encoded_text):,} tokens")                              # Print the length of the encoded text with thousands separator
encoded_sample = encoded_text[50:]                                                          # Get a sample of the encoded text starting from the 50th token

context_size = 4                                                                            # Define the context size for the model (number of tokens to consider for context)
x = encoded_sample[:context_size]                                                           # Get the first 'context_size' tokens from the encoded sample as input
y = encoded_sample[1:context_size+1]                                                        # Get the next 'context_size' tokens from the encoded sample as target output
#print(f"x: {x}")                                                                            # Print the input tokens
#print(f"y:      {y}")                                                                      # Print the target output tokens

#
# Create a context and desired token pairs for training
#
for i in range(1, context_size+1):                                                         # Loop through the range from 1 to 'context_size'
    context = encoded_sample[:i]                                                           # Get the first 'i' tokens from the encoded sample as context
    desired = encoded_sample[i]                                                            # Get the desired token at the ith position
    #print(context, "---->", desired)                                                       # Print the context tokens and the corresponding desired token for each iteration

#
# Decode the context and desired token pairs for better readability
#
for i in range(1, context_size+1):                                                         # Loop through the range from 1 to 'context_size'
    context = encoded_sample[:i]                                                           # Get the first 'i' tokens from the encoded sample as context
    desired = encoded_sample[i]                                                            # Get the desired token at the ith position
    #print(tokenizer.decode(context), "---->", tokenizer.decode([desired]))                 # Print the decoded context tokens and the corresponding decoded desired token for each iteration

#
# Create a custom dataset class for training a GPT model
#
import torch                                                                               # Import the PyTorch library for tensor operations
from torch.utils.data import Dataset, DataLoader                                           # Import Dataset and DataLoader classes from torch.utils.data for creating custom datasets and loading data in batches

class GPTDatasetV1(Dataset):                                                               # Define a custom dataset class named GPTDatasetV1 that inherits from the PyTorch Dataset class
    def __init__(self, text, tokenizer, max_length, stride):                               # Define the constructor method that takes text, tokenizer, max_length, and stride as arguments
        self.input_ids = []                                                                # Create an empty list to store input token IDs
        self.target_ids = []                                                               # Create an empty list to store target token IDs

        token_ids = tokenizer.encode(text)                                                 # Encode the input text into a list of integer token IDs using the provided tokenizer
        for i in range(0, len(token_ids) - max_length, stride):                            # Loop through the token IDs with a step size of 'stride' to create overlapping sequences of tokens
            input_chunk = token_ids[i:i + max_length]                                      # Get a chunk of input tokens of size 'max_length'
            target_chunk = token_ids[i + 1:i + max_length + 1]                             # Get the corresponding target tokens by shifting the input chunk by one position
            self.input_ids.append(torch.tensor(input_chunk))                               # Append the input chunk to the list of input token IDs
            self.target_ids.append(torch.tensor(target_chunk))                             # Append the target chunk to the list of target token IDs

    def __len__(self):                                                                     # Define a method to return the length of the dataset
        return len(self.input_ids)                                                         # Return the length of the input IDs list

    def __getitem__(self, idx):                                                            # Define a method to get an item from the dataset at a given index
        x = self.input_ids[idx]                                                            # Get the input tokens (context) for the given index
        y = self.target_ids[idx]                                                           # Get the target tokens (desired output) for the given index
        return x, y                                                                        # Return the input and target tokens as PyTorch tensors of type long

#
# Create a DataLoader for the GPTDatasetV1 dataset
#
def create_dataloader_v1(text, batch_size=4, max_length=256, stride=128, shuffle=True, drop_last=True, num_workers=0):      # Define a function to create a DataLoader for the GPTDatasetV1 dataset with specified parameters
    tokenizer = tiktoken.get_encoding("gpt2")                                                                               # Get the tokenizer encoding for "gpt2" from the tiktoken module
    dataset = GPTDatasetV1(text, tokenizer, max_length, stride)                                                             # Create an instance of the GPTDatasetV1 with the provided text and tokenizer with specified max_length and stride
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, drop_last=drop_last, num_workers=num_workers)  # Create a DataLoader for the dataset with specified parameters
    return dataloader                                                                                                       # Return the created DataLoader to be used for training the GPT model

#
# Load the text data and create a DataLoader for training
#
with open("the-verdict.txt", "r", encoding="utf-8") as f:                                                                   # Open the file in read mode with UTF-8 encoding
    raw_text = f.read()                                                                                                     # Read the entire content of the file into the variable 'text'

#dataloader = create_dataloader_v1(raw_text, batch_size=1, max_length=8, stride=3, shuffle=False)                            # Create a DataLoader for the GPTDatasetV1 with specified parameters for batch size, max length, stride, and shuffle option
#data_iterator = iter(dataloader)                                                                                            # Create an iterator for the DataLoader to iterate through the batches of data
#first_batch = next(data_iterator)                                                                                           # Get the first batch of data from the DataLoader iterator
#print(first_batch)                                                                                                          # Print the first batch of data, which contains input and target token tensors
#second_batch = next(data_iterator)                                                                                          # Get the second batch of data from the DataLoader iterator
#print(second_batch)                                                                                                         # Print the second batch of data, which contains input and target token tensors

dataloader = create_dataloader_v1(raw_text, batch_size=8, max_length=4, stride=4, shuffle=False)                            # Create a DataLoader for the GPTDatasetV1 with specified parameters for batch size, max length, stride, and shuffle option
data_iterator = iter(dataloader)                                                                                            # Create an iterator for the DataLoader to iterate through the batches of data
inputs, targets = next(data_iterator)                                                                                       # Get the first batch of data from the DataLoader iterator and unpack it into inputs and targets
print("Inputs:\n", inputs)                                                                                                  # Print the input token tensors for the first batch
print("\nTargets:\n", targets)                                                                                              # Print the target token tensors for the first batch
