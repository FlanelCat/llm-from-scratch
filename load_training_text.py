# Based on https://github.com/rasbt/LLMs-from-scratch/blob/main/ch02/01_main-chapter-code/ch02.ipynb
# with verbose comments added by ChatGPT
# 2026-11-25
import os                                                   # Import the os module for interacting with the operating system
import requests                                             # Import the requests module for making HTTP requests

if not os.path.exists("the-verdict"):                       # Check if the directory "the-verdict" does not exist
    url = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"
    file_path = "the-verdict.txt"                           # Path to save the downloaded file
    response = requests.get(url, timeout=30)                # Set a timeout of 30 seconds for the request
    response.raise_for_status()                             # Raise an error if the request was unsuccessful
    with open(file_path, "wb") as f:                        # Open the file in binary write mode
        f.write(response.content)                           # Write the content of the response to the file