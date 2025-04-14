import pandas as pd
import matplotlib.pyplot as plt
import re

def extract_python_code(text):
    """
    Extracts Python code from a markdown-formatted response using regex.
    
    Args:
        text (str): The text response from Gemini.

    Returns:
        str: Extracted Python code or an empty string if no code is found.
    """
    pattern = r"```python\n(.*?)\n```"  # Captures Python code inside ```python ... ```
    match = re.search(pattern, text, re.DOTALL)
    
    return match.group(1) if match else ""  # Return extracted code or empty string








